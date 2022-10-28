# # # # import json

# # # # with open("E:\Trash\QQBot\Alin\src\plugins\pixiv\data\\arknights 10000users入り.json", "r", encoding="utf-8") as f:
# # # #     tag_json = json.load(f)
# # # #     f.close()

# # # # illust_data: list = tag_json["body"]["illustManga"]["data"]
# # # # print(len(illust_data))

# # # # async def fun():
# # # #     print(1)

# # # # async def test():
# # # #     try:
# # # #         await fun()
# # # #     except:
# # # #         print(2)
# # # # import asyncio
# # # # asyncio.run(test())

# # # import requests
# # # import json

# # # def fun(tag: str):
# # #     headers = {
# # #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
# # #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
# # #         "Accept-Encoding": "gzip, deflate, br",
# # #         "Host": "www.pixiv.net"
# # #     }
# # #     res = requests.get(
# # #         url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
# # #         headers=headers,
# # #         proxies={
# # #             "http": "http://127.0.0.1:7890",
# # #             "https": "http://127.0.0.1:7890"
# # #         }
# # #     ).json()
# # #     print(res)
# # #     illust_json = res
# # #     page_data_num = len(illust_json["body"]["illustManga"]["data"])
# # #     illust_total = int(illust_json["body"]["illustManga"]["total"])
# # #     if illust_total > 60:
# # #         remain_pages = int(illust_total/page_data_num)
# # #         for i in range(remain_pages):
# # #             res = requests.get(
# # #                 url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p={str(i+2)}&s_mode=s_tag&type=all&lang=zh"
# # #             ).json()
# # #             illust_json["body"]["illustManga"]["data"] += res["body"]["illustManga"]["data"]
# # #     print(res)
# # #     with open("./test.json", "w", encoding="utf-8") as f:
# # #         json.dump(illust_json, f)
# # #         f.close()

# # import requests
# # import random
# # import os

# # tag_list = ["111"]
# # tag = "贫乳"

# # if f"{tag} 10000users入り.json" not in tag_list:
# #     headers = {
# #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
# #         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
# #         "Accept-Encoding": "gzip, deflate, br",
# #         "Host": "www.pixiv.net"
# #     }
# #     res = requests.get(
# #         url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
# #         headers=headers,
# #         proxies={
# #             "http": "http://127.0.0.1:7890",
# #             "https": "http://127.0.0.1:7890"
# #         },
# #         timeout=5
# #     )
# #     # illust_total = int(res["body"]["illustManga"]["total"])
# #     # page_total = int(illust_total/60) + 1
# #     # random_page = random.randint(1, page_total)
# #     # resp = requests.get(
# #     #     url="https://www.pixiv.net/ajax/search/artworks/"+tag+"%2010000users%E5%85%A5%E3%82%8A?word="+tag+f"%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p="+str(random_page)+"&s_mode=s_tag&type=all&lang=zh",
# #     #     headers=headers,
# #     #     proxies={
# #     #         "http": "http://127.0.0.1:7890",
# #     #         "https": "http://127.0.0.1:7890"
# #     #     }
# #     # )
# #     print(res.url)
# #     resp = res.json()
# # # illust_list = resp["body"]["illustManga"]["data"]
# # # while True:
# # #     illust = illust_list[random.randint(0, len(illust_list)-1)]
# # #     illust_id: str = illust["id"]
# # #     illust_title: str = illust["title"]
# # #     illust_userName: str = illust["userName"]
# # #     flag, illust_pageCount = True, 1
# # #     if flag:
# # #         break
# # # illust_info = {"illust_id": illust_id, "illust_title": illust_title, "illust_userName": illust_userName}
# # # if illust_pageCount == 1:
# # #     print([illust_id+".png"])
# # # else:
# # #     print([illust_id+"-"+str(x+1)+".png" for x in range(illust_pageCount)])
# # # print(len(illust_list))
# # print(resp)

# import json
# import requests
# import os


# login_url = "https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh&source=pc&view_type=page"
# session = requests.session()
# res = session.post(
    
# )

# import requests

# tag = "贫乳"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#     "Accept-Encoding": "gzip, deflate, br",
#     # "Host": "www.pixiv.net",
#     # "Connection": "keep-alive",
#     # "Sec-Fetch-Dest": "document",
#     # "Sec-Fetch-Mode": "navigate",
#     # "Sec-Fetch-Site": "cross-site",
#     # "Sec-Fetch-User": "?1",
#     # "TE": "trailers",
#     # "Cache-Control": "no-cache",
#     "Cookie": "p_ab_d_id=1795725297; b_type=1; a_type=0; p_ab_id_2=9; p_ab_id=7; privacy_policy_notification=0; first_visit_datetime_pc=2022-07-23+01:59:44; yuid_b=EXZydVA; _im_uid.3929=h.68c0afe0720d021f; __utmz=235335808.1665973486.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _fbp=fb.1.1665973486510.1151231928; device_token=4039c25f78f2290a87dbc977eb73f326; _im_vid=01GFHW4EK6917QGHMXAQDVDQ65; login_ever=yes; _gcl_au=1.1.709795294.1666019582; adr_id=1lbq0BEfhZ04Izw8gSGNx9ux7i71nxY6cwGFXFXqvTHCZA87; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; privacy_policy_agreement=5; c_type=20; __utmv=235335808.|2=login ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=87378304=1^9=p_ab_id=7=1^10=p_ab_id_2=9=1^11=lang=zh=1; PHPSESSID=87378304_niYNYJhDtgOjhfECl9LP93uWw7yTPxur; _ga_MZ1NL4PHH0=GS1.1.1666598368.4.1.1666598620.0.0.0; cto_bundle=61UyKF80cGdwNjQ0SmdQNlpIT2VaMlVLSHNaUkFOenJOR0FDMVNya1dSb2QlMkJDbngybXBvTHdCSDlPU0xOVDdraXQxcmhSd09vMW9IRnAwY1BPVmNVQkg3eSUyQmdXeGE1ckpPJTJCSVB3QTkxajNtbXVtOHM5YjUlMkZOa2l5Q3BYSGYxSHVDRGRhRmYzVk1abyUyRmM3Y3ZValclMkJCZkNVQnclM0QlM0Q; __utma=235335808.173216847.1665973486.1666746730.1666845155.17; __utmc=235335808; __cf_bm=b4fd6oohjgJGTxyoMkavr9F3t_8y5PK82qx7BYA9d8Q-1666845158-0-AbPZ6yLFMOPDAYqiVie7frECh9vdcyPIEbg0BdE6sJjVPG7qvkG4rMQwWNR7xg93BaHwRSIKzRfDR1licz25hmTZ7ns9sh4bn8Bzm2bBP8PKs68QQiwkUP9jDhh/QU3XZ/DhtFG2gw1PZwdI0GoajdNwiZDqqKAzATshHB7vj3IhPche69rNLQNElOu9b6aF9g==; _gid=GA1.2.2060686082.1666845171; __utmb=235335808.2.10.1666845155; tag_view_ranking=RTJMXD26Ak~jH0uD88V6F~0xsDLqCEW6~RybylJRnhJ~Bd2L9ZBE8q~Lt-oEicbBr~py0hn8jqar~EZQqoW9r8g~27Pk8Qa19c~-98s6o2-Rp~wKl4cqK7Gl~jHx40ftsLV~kjfJ5uXq4m~KN7uxuR89w~MsYOGWeMbK~Kw3rxm81BS~hIbSsZ4_QS~1n-RsNEFpK~2R7RYffVfj~uW5495Nhg-~0M0zAeslDb~xha5FQn_XC~Ie2c51_4Sp~GNcgbuT3T-~pnCQRVigpy~jk9IzfjZ6n~_hSAdpN9rx~oJAJo4VO5E~kXfMq859P2~0rsCr94LAC~q303ip6Ui5~XDEWeW9f9i~EUwzYuPRbU~3W4zqr4Xlx~qtVr8SCFs5~w8ffkPoJ_S~t-2cmV0Swf~iszjNkquhZ~YCJduqB2Ci~ecMhD_UNXf~4qFCYZaetA~EGefOqA6KB~Hjx7wJwsUT~aKhT3n4RHZ~K8esoIs2eW~B9VsvJr9Z4~PTyxATIsK0~QaiOjmwQnI~RokSaRBUGr~Xyw8zvsyR4~_GuOetFMMO~_EOd7bsGyl~ziiAzr_h04~Nbvc4l7O_x~zyKU3Q5L4C~pYlUxeIoeg~tgP8r-gOe_~dcBA_MI-0N~8buMDtT-ku~eVxus64GZU~yvN_bfBdr-~nQRrj5c6w_~VN7cgWyMmg~1WiF9FWDcG~RIm1W1ofw1~iFcW6hPGPU~RAIgWz-BIv~pD0wVYlrjV~HY55MqmzzQ~CrFcrMFJzz~c8y2glRxy1~z8HrAjAXzi~hznVYuC5dv~f4V1aCLsyM~DpO7Lofslr~d2oWv_4U1L~i4Q_o7CyIB~SqVgDNdq49~gpglyfLkWs~LJo91uBPz4~j3leh4reoN~t6fkfIQnjP~dkvvzKpAOm~VMq-Vxsw8k~fg8EOt4owo~RcahSSzeRf~5oPIfUbtd6~323M2YxDZa~ahqc2_Z8SY~dJgU3VsQmO~GmCzj7c06U~4gzX-RNalt~ykNnpw2uh5~azESOjmQSV~FrSumU5wXT~mFosrNEiIG~kGYw4gQ11Z~BtXd1-LPRH~kqu7T68WD3~QliAD3l3jr; _ga_75BBYNYN9J=GS1.1.1666845156.21.1.1666845282.0.0.0; _gat=1; _ga_34B604LFFQ=GS1.1.1666845171.13.1.1666846313.60.0.0; _ga=GA1.1.173216847.1665973486"
# }
# res = requests.get(
#     url=f"https://www.pixiv.net/ajax/search/artworks/{tag}%2010000users%E5%85%A5%E3%82%8A?word={tag}%2010000users%E5%85%A5%E3%82%8A&order=date_d&mode=all&p=1&s_mode=s_tag&type=all&lang=zh",
#     headers=headers,
#     proxies={
#         "http": "http://127.0.0.1:7890",
#         "https": "http://127.0.0.1:7890"
#     }
# ).json()
# print(res)

# import os


# for tag in os.listdir("E:\Trash\QQBot\Alin\src\plugins\pixiv\\temp"):
#     print("setu add "+tag.replace(" 10000users入り.json", "")+"\n")


# import requests
# illust_name = "82803871.png"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52",
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate, br",
#     "Host": "i.pximg.net",
#     "Referer": "https://www.pixiv.net/"
# }
# result = False
# with open("./1.png", "wb") as f:
#     res = requests.get(
#             url=f"https://i.pximg.net/img-master/img/2022/10/25/01/03/05/102210339_p0_master1200.jpg",
#             headers=headers
#         )
#     f.write(res.content)
#     f.write(bytes("send by Alin(Bot)", encoding="utf-8"))
#     result = True
#     f.close()
# illust_p0_url = "https://i.pximg.net/img-master/img/2022/10/25/01/03/05/102210339_p0_master1200.jpg"
# illust_pageCount = 5
# t = [illust_p0_url.replace("p0", f"p{str(x)}") for x in range(illust_pageCount)]
# for illust_url in t:
    # print(illust_url.split("/")[-1])

t = ["1", "2", "3"]
print(t[1:])