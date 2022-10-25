import requests
import os
import json
import random
import asyncio
from nonebot.log import logger
from tqdm import tqdm
import time

data_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data"
images_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "images"
tag_list: list = os.listdir(data_dir)
# print(tag_list)


async def get_setu() -> tuple[list[str], dict]: #json在add时候下载，假定存在
    tag_json_name = tag_list[random.randint(0, len(tag_list)-1)]
    with open(data_dir+os.path.sep+tag_json_name, "r", encoding="utf-8") as f:
        tag_json = json.load(f)
        f.close()
    illust_list: list = tag_json["body"]["illustManga"]["data"]
    while True:
        illust = illust_list[random.randint(0, len(illust_list)-1)]
        illust_id: str = illust["id"]
        illust_title: str = illust["title"]
        illust_userName: str = illust["userName"]
        flag, illust_pageCount = await check(illust_id)
        if flag:
            break
    illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
    if illust_pageCount == 1:
        return [illust_id+".png"], illust_info
    else:
        return [illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)], illust_info
    

async def download_setu(illust_name: str) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }
    result = False
    with open(images_dir+os.path.sep+illust_name, "wb") as f:
        try:
            logger.info(f"开始下载 {illust_name}")
            res = requests.get(
                url=f"https://pixiv.re/{illust_name}",
                headers=headers
            )
            if res.status_code != 503:
                f.write(res.content)
                result = True
                logger.success(f"下载 {illust_name} 成功")
            else:
                logger.error(f"下载 {illust_name} 失败，API速率限制")
        except:
            logger.error(f"下载 {illust_name} 失败")
        f.close()
    return result


async def download_tag_json(tag: str) -> bool:
    logger.info(f"开始下载{tag} 10000users入り.json文件")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "www.pixiv.net"
        }
        res = requests.get(
            url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
            headers=headers,
            proxies={
                "http": "http://127.0.0.1:7890",
                "https": "http://127.0.0.1:7890"
            }
        ).json()
        illust_json = res
        page_data_num = len(illust_json["body"]["illustManga"]["data"])
        illust_total = int(illust_json["body"]["illustManga"]["total"])
        if illust_total > 60:
            remain_pages = int(illust_total/page_data_num)
            for i in tqdm(range(remain_pages)):
                res = requests.get(
                    url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p={str(i+2)}&s_mode=s_tag&type=all&lang=zh"
                ).json()
                illust_json["body"]["illustManga"]["data"] += res["body"]["illustManga"]["data"]
            time.sleep(4)
        with open(data_dir+os.path.sep+f"{tag} 10000users入り.json", "w", encoding="utf-8") as f:
            json.dump(illust_json, f)
            f.close()
    except:
        logger.error(f"{tag} 10000users入り.json文件下载失败")
        return False
    logger.success(f"{tag} 10000users入り.json文件下载成功")
    return True


async def get_tag_setu(tag: str) -> tuple[list[str], dict]:
    try:
        if f"{tag} 10000users入り.json" not in tag_list:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Host": "www.pixiv.net"
            }
            res = requests.get(
                url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
                headers=headers,
                proxies={
                    "http": "http://127.0.0.1:7890",
                    "https": "http://127.0.0.1:7890"
                },
                timeout=5
            ).json()
            illust_total = int(res["body"]["illustManga"]["total"])
            page_total = int(illust_total/60) + 1
            random_page = random.randint(1, page_total)
            resp = requests.get(
                url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p="+str(random_page)+"&s_mode=s_tag&type=all&lang=zh",
                headers=headers,
                proxies={
                    "http": "http://127.0.0.1:7890",
                    "https": "http://127.0.0.1:7890"
                },
                timeout=5
            ).json()
        else:
            with open(data_dir+os.path.sep+f"{tag} 10000users入り.json", "r", encoding="utf-8") as f:
                resp = json.load(f)
                f.close()
        illust_list = resp["body"]["illustManga"]["data"]
        while True:
            illust = illust_list[random.randint(0, len(illust_list)-1)]
            illust_id: str = illust["id"]
            illust_title: str = illust["title"]
            illust_userName: str = illust["userName"]
            flag, illust_pageCount = await check(illust_id)
            if flag:
                break
        illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
        if illust_pageCount == 1:
            return [illust_id+".png"], illust_info
        else:
            return [illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)], illust_info
    except:
        logger.error(f"获取 {tag} 图片失败")
        return [], {}
            

async def check(illust_id: str) -> tuple[bool, int]:
    url = "https://www.pixiv.net/ajax/illust/" + illust_id
    res = requests.get(
        url=url,
        proxies={
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
        }
    ).json()
    if int(res["body"]["viewCount"]) >= 10000:
        logger.info(f"PID:{illust_id} 符合")
        return True, int(res["body"]["pageCount"])
    logger.warning(f"PID:{illust_id} 不符合")
    return False, -1


if __name__=="__main__":
    # illust_id = "97228344"
    # flag, illust_pageCount = asyncio.run(check(illust_id))
    # print(illust_pageCount)
    # if illust_pageCount == 1:
    #     print([illust_id+".png"])
    # else:
    #     print([illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)])
    asyncio.run(download_tag_json("オリジナル"))