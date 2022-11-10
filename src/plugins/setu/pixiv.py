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

cookie: str = "first_visit_datetime_pc=2022-07-23+01:59:44; yuid_b=EXZydVA; _im_uid.3929=h.68c0afe0720d021f; _im_vid=01GFHW4EK6917QGHMXAQDVDQ65; login_ever=yes; adr_id=1lbq0BEfhZ04Izw8gSGNx9ux7i71nxY6cwGFXFXqvTHCZA87; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; p_ab_id=3; p_ab_id_2=3; p_ab_d_id=200819305; _gid=GA1.2.1932889002.1666964309; _gat_gtag_UA_76252338_1=1; _gat=1; PHPSESSID=87378304_1iYFDoVWwClD7jJzX0q1A1htNL8qcsYR; device_token=b0a18a49a4192eb717ad706b89872a04; privacy_policy_agreement=5; _ga_MZ1NL4PHH0=GS1.1.1666964309.1.0.1666964317.0.0.0; c_type=20; privacy_policy_notification=0; a_type=0; b_type=1; __utma=235335808.2096325128.1666964309.1666964318.1666964318.1; __utmc=235335808; __utmz=235335808.1666964318.1.1.utmcsr=accounts.pixiv.net|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=235335808.|3=plan=normal=1^5=gender=male=1^6=user_id=87378304=1^11=lang=zh=1; __utmt=1; _fbp=fb.1.1666964319847.792490847; __cf_bm=2ZdEZ4hxmJvlSCFbJzIALsGGyZhwNGtvhlPqon7tT.U-1666964320-0-AdOFboP/lqh13d3coYVTWmDYBlnmCj2hkdz1fQSldtIwdl/4AoMsU34eIkeySPNSSvCz6e1FX+Lrat+/QDWhushSGFXV72i4/zlF7tQK68h+snnLNUBeRRMYxP2qpgVtKRRE15H7+bBAD7mG11lIU8rOQVlShUf/YAAF1zJiwC0gCXB++/YevQdeeDR55Yi3tQ==; _ga_34B604LFFQ=GS1.1.1666963386.18.1.1666964323.45.0.0; _ga=GA1.2.2096325128.1666964309; _gat_UA-1830249-3=1; _ga_75BBYNYN9J=GS1.1.1666964319.1.1.1666964327.0.0.0; __utmb=235335808.2.10.1666964318; tag_view_ranking=RTJMXD26Ak~jH0uD88V6F~Lt-oEicbBr~RybylJRnhJ~0xsDLqCEW6~EZQqoW9r8g~-98s6o2-Rp~Bd2L9ZBE8q~py0hn8jqar~jHx40ftsLV~wKl4cqK7Gl~MsYOGWeMbK~Kw3rxm81BS~hIbSsZ4_QS~27Pk8Qa19c~_EOd7bsGyl~2R7RYffVfj~1n-RsNEFpK~uW5495Nhg-~Ie2c51_4Sp~ziiAzr_h04~q303ip6Ui5~_hSAdpN9rx~KN7uxuR89w~kXfMq859P2~xha5FQn_XC~K8esoIs2eW~zyKU3Q5L4C~SqVgDNdq49~azESOjmQSV~pnCQRVigpy~XDEWeW9f9i~jk9IzfjZ6n~3W4zqr4Xlx~qtVr8SCFs5~w8ffkPoJ_S~t-2cmV0Swf~iszjNkquhZ~YCJduqB2Ci~ecMhD_UNXf~oJAJo4VO5E~4qFCYZaetA~EGefOqA6KB~Hjx7wJwsUT~B9VsvJr9Z4~kjfJ5uXq4m~0M0zAeslDb~tgP8r-gOe_~BSlt10mdnm~fg8EOt4owo~RcahSSzeRf~DFQ_tSdhNJ~LJo91uBPz4~Xyw8zvsyR4~EUwzYuPRbU~Nbvc4l7O_x~dcBA_MI-0N~8buMDtT-ku~eVxus64GZU~yvN_bfBdr-~VN7cgWyMmg~1WiF9FWDcG~RIm1W1ofw1~iFcW6hPGPU~RAIgWz-BIv~aKhT3n4RHZ~pD0wVYlrjV~CrFcrMFJzz~c8y2glRxy1~z8HrAjAXzi~hznVYuC5dv~f4V1aCLsyM~PTyxATIsK0~i4Q_o7CyIB~7fCik7KLYi~SapL8yQw4Y~_AKBg0O8RH~ZNRc-RnkNl~nWC-P2-9TI~JL8rvDh62i~lwP9D7jsDZ~de02-GUGP5~NVZ4BKkG01~DBiiO5jGyf~HOD65YeJBA~Z870Db6zVg~LdL63dDttt~nInT2dTMR6~X_1kwTzaXt~U-RInt8VSZ~MnGbHeuS94~YRDwjaiLZn~_GuOetFMMO~j3leh4reoN~t6fkfIQnjP~dkvvzKpAOm~VMq-Vxsw8k~5oPIfUbtd6~pYlUxeIoeg~323M2YxDZa"

async def get_setu() -> tuple[list[str], dict]: #json在add时候下载，假定存在
    tag_json_name = tag_list[random.randint(0, len(tag_list)-1)]
    with open(data_dir+os.path.sep+tag_json_name, "r", encoding="utf-8") as f:
        tag_json = json.load(f)
        f.close()
    illust_list: list = tag_json["body"]["illustManga"]["data"]
    times = 0
    while times < 5:
        illust = illust_list[random.randint(0, len(illust_list)-1)]
        illust_id: str = illust["id"]
        illust_title: str = illust["title"]
        illust_userName: str = illust["userName"]
        flag, illust_info_json = await check(illust_id)
        if flag:
            break
    illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
    illust_pageCount = int(illust_info_json["body"]["pageCount"])
    illust_p0_url = str(illust_info_json["body"]["urls"]["regular"])
    return [illust_p0_url.replace("p0", f"p{str(x)}") for x in range(illust_pageCount)], illust_info
    

async def download_setu_from_pixiv(illust_url: str) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Host": "i.pximg.net",
        "Referer": "https://www.pixiv.net/"
    }
    result = False
    illust_name = illust_url.split("/")[-1]
    with open(images_dir+os.path.sep+illust_name, "wb") as f:
        try:
            logger.info(f"开始下载 {illust_name}")
            res = requests.get(
                url=illust_url,
                headers=headers,
                proxies={
                        "http": "http://127.0.0.1:7890",
                        "https": "http://127.0.0.1:7890"
                }
            )
            if res.status_code != 503:
                f.write(res.content)
                f.write(bytes("send by Alin(Bot)"+str(random.randint(0, 999)), encoding="utf-8"))
                result = True
                logger.success(f"下载 {illust_name} 成功")
            else:
                logger.error(f"下载 {illust_name} 失败，API速率限制")
        except:
            logger.error(f"下载 {illust_name} 失败")
        f.close()
    return result


async def download_setu_from_pixivre(illust_url: str) -> bool:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br"
    }
    result = False
    illust_name = illust_url.split("/")[-1]
    with open(images_dir+os.path.sep+illust_name, "wb") as f:
        try:
            logger.info(f"开始下载 {illust_name}")
            res = requests.get(
                url=illust_url,
                headers=headers,
                proxies={
                        "http": "http://127.0.0.1:7890",
                        "https": "http://127.0.0.1:7890"
                }
            )
            if res.status_code != 503:
                f.write(res.content)
                f.write(bytes("send by Alin(Bot)"+str(random.randint(0, 999)), encoding="utf-8"))
                result = True
                logger.success(f"下载 {illust_name} 成功")
            else:
                logger.error(f"下载 {illust_name} 失败，API速率限制")
        except:
            logger.error(f"下载 {illust_name} 失败")
        f.close()
    return result


async def download_tag_json(tag: str) -> bool:
    logger.info(f"开始下载{tag}.json文件")
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Host": "www.pixiv.net",
            "Cookie": cookie
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
                    url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p={str(i+2)}&s_mode=s_tag&type=all&lang=zh",
                    headers=headers,
                    proxies={
                        "http": "http://127.0.0.1:7890",
                        "https": "http://127.0.0.1:7890"
                    }
                ).json()
                illust_json["body"]["illustManga"]["data"] += res["body"]["illustManga"]["data"]
            time.sleep(2)
        with open(data_dir+os.path.sep+f"{tag}.json", "w", encoding="utf-8") as f:
            json.dump(illust_json, f)
            f.close()
    except:
        logger.error(f"{tag}.json文件下载失败")
        return False
    logger.success(f"{tag}.json文件下载成功")
    return True


async def get_tag_setu(tag: str) -> tuple[list[str], dict]:
    try:
        if f"{tag}.json" not in tag_list:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Host": "www.pixiv.net",
                "Cookie": cookie
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
            mode = "10000"
            if illust_total <= 10:
                res = requests.get(
                    url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%205000users%E5%85%A5%E3%82%8A?word="+tag+f"%205000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
                    headers=headers,
                    proxies={
                        "http": "http://127.0.0.1:7890",
                        "https": "http://127.0.0.1:7890"
                    },
                    timeout=5
                ).json()
                illust_total = int(res["body"]["illustManga"]["total"])
                mode = "5000"
            page_total = int(illust_total/60) + 1
            random_page = random.randint(1, page_total)
            resp = requests.get(
                url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%20"+mode+"users%E5%85%A5%E3%82%8A?word="+tag+f"%20"+mode+"users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p="+str(random_page)+"&s_mode=s_tag&type=all&lang=zh",
                headers=headers,
                proxies={
                    "http": "http://127.0.0.1:7890",
                    "https": "http://127.0.0.1:7890"
                },
                timeout=5
            ).json()
        else:
            with open(data_dir+os.path.sep+f"{tag}.json", "r", encoding="utf-8") as f:
                resp = json.load(f)
                f.close()
        illust_list = resp["body"]["illustManga"]["data"]
        times = 0
        while times < 5:
            illust = illust_list[random.randint(0, len(illust_list)-1)]
            illust_id: str = illust["id"]
            illust_title: str = illust["title"]
            illust_userName: str = illust["userName"]
            flag, illust_info_json = await check(illust_id)
            times += 1
            if flag:
                break
        illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
        illust_pageCount = int(illust_info_json["body"]["pageCount"])
        illust_p0_url = str(illust_info_json["body"]["urls"]["regular"])
        return [illust_p0_url.replace("p0", f"p{str(x)}") for x in range(illust_pageCount)], illust_info
    except:
        logger.error(f"获取 {tag} 图片失败")
        return [], {}
            

async def check(illust_id: str) -> tuple[bool, dict]:
    url = "https://www.pixiv.net/ajax/illust/" + illust_id
    res = requests.get(
        url=url,
        proxies={
            "http": "http://127.0.0.1:7890",
            "https": "http://127.0.0.1:7890"
        }
    ).json()
    viewCount = int(res["body"]["viewCount"])
    pageCount = int(res["body"]["pageCount"])
    illustType = int(res["body"]["illustType"])
    bookmarkCount = int(res["body"]["bookmarkCount"])
    if pageCount <= 5:
        if (viewCount >= 10000 and illustType == 0 and viewCount*0.2 >= bookmarkCount) or (viewCount >= 5000 and illustType == 0 and viewCount*0.4 >= bookmarkCount):
            logger.info(f"PID:{illust_id} 符合")
            return True, res
    logger.warning(f"PID:{illust_id} 不符合")
    return False, {}


if __name__=="__main__":
    # illust_id = "97228344"
    # flag, illust_pageCount = asyncio.run(check(illust_id))
    # print(illust_pageCount)
    # if illust_pageCount == 1:
    #     print([illust_id+".png"])
    # else:
    #     print([illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)])
    asyncio.run(download_tag_json("オリジナル"))