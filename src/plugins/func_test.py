# # # import json

# # # with open("E:\Trash\QQBot\Alin\src\plugins\pixiv\data\\arknights 10000users入り.json", "r", encoding="utf-8") as f:
# # #     tag_json = json.load(f)
# # #     f.close()

# # # illust_data: list = tag_json["body"]["illustManga"]["data"]
# # # print(len(illust_data))

# # # async def fun():
# # #     print(1)

# # # async def test():
# # #     try:
# # #         await fun()
# # #     except:
# # #         print(2)
# # # import asyncio
# # # asyncio.run(test())

# # import requests
# # import json

# # def fun(tag: str):
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
# #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
# #         "Accept-Encoding": "gzip, deflate, br",
# #         "Host": "www.pixiv.net"
# #     }
# #     res = requests.get(
# #         url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
# #         headers=headers,
# #         proxies={
# #             "http": "http://127.0.0.1:7890",
# #             "https": "http://127.0.0.1:7890"
# #         }
# #     ).json()
# #     print(res)
# #     illust_json = res
# #     page_data_num = len(illust_json["body"]["illustManga"]["data"])
# #     illust_total = int(illust_json["body"]["illustManga"]["total"])
# #     if illust_total > 60:
# #         remain_pages = int(illust_total/page_data_num)
# #         for i in range(remain_pages):
# #             res = requests.get(
# #                 url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p={str(i+2)}&s_mode=s_tag&type=all&lang=zh"
# #             ).json()
# #             illust_json["body"]["illustManga"]["data"] += res["body"]["illustManga"]["data"]
# #     print(res)
# #     with open("./test.json", "w", encoding="utf-8") as f:
# #         json.dump(illust_json, f)
# #         f.close()

# import requests
# import random
# import os

# tag_list = ["111"]
# tag = "贫乳"

# if f"{tag} 10000users入り.json" not in tag_list:
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Host": "www.pixiv.net"
#     }
#     res = requests.get(
#         url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
#         headers=headers,
#         proxies={
#             "http": "http://127.0.0.1:7890",
#             "https": "http://127.0.0.1:7890"
#         },
#         timeout=5
#     )
#     # illust_total = int(res["body"]["illustManga"]["total"])
#     # page_total = int(illust_total/60) + 1
#     # random_page = random.randint(1, page_total)
#     # resp = requests.get(
#     #     url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p="+str(random_page)+"&s_mode=s_tag&type=all&lang=zh",
#     #     headers=headers,
#     #     proxies={
#     #         "http": "http://127.0.0.1:7890",
#     #         "https": "http://127.0.0.1:7890"
#     #     }
#     # )
#     print(res.url)
#     resp = res.json()
# # illust_list = resp["body"]["illustManga"]["data"]
# # while True:
# #     illust = illust_list[random.randint(0, len(illust_list)-1)]
# #     illust_id: str = illust["id"]
# #     illust_title: str = illust["title"]
# #     illust_userName: str = illust["userName"]
# #     flag, illust_pageCount = True, 1
# #     if flag:
# #         break
# # illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
# # if illust_pageCount == 1:
# #     print([illust_id+".png"])
# # else:
# #     print([illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)])
# # print(len(illust_list))
# print(resp)

