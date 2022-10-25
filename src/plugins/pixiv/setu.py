from loguru import logger
from nonebot import Bot, on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
import os

from ...util import send_group_msg, send_private_msg, send_group_img, send_private_img, get_image_cq
from .pixiv import get_setu, download_setu, download_tag_json, get_tag_setu

pixiv_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = pixiv_dir + os.path.sep + "data"
images_dir = pixiv_dir + os.path.sep + "images"
setu = on_command(cmd="setu", rule=to_me(), aliases={"来张涩图", "涩图", "色图", "来张色图"})


@setu.handle()
async def handle_func(e: Event, bot: Bot, matcher: Matcher, args: Message = CommandArg()):
    matcher.set_arg("cmd&arg", args)


@setu.got(key="cmd&arg")
async def got_func(e: Event, bot: Bot, ca: str = ArgPlainText("cmd&arg")):
    private = False
    group = False
    user_id = str(e.__getattribute__("user_id"))
    user_name = e.__getattribute__("sender").__getattribute__("nickname")
    if e.__getattribute__("message_type") == "group":
        group = True
        group_id = str(e.__getattribute__("group_id"))
    elif e.__getattribute__("message_type") == "private":
        private = True
        group_id = "253016320"
    ca = ca.strip()
    if ca == "":
        illust_list, illust_info = await get_setu()

        await send_images_from_list(illust_list, bot, user_id)

        info = f"PID{illust_info['illust_id']}， 画师{illust_info['illust_userName']}， 标题{illust_info['illust_title']}"
        return await setu.finish(f"{user_name}要的涩图，"+info)
    
    cmd = ca.split(" ")[0]
    if not " " in ca:
        return await setu.finish("参数错误")
    else:  
        arg = ca.split(" ")[1]

    if cmd == "add" or cmd == "添加":
        if os.path.exists(data_dir+os.path.sep+f"{arg} 10000users入り.json"):
            return await setu.finish(f"Tag {arg} 已存在")
        await setu.send(f"开始下载 {arg} 10000users入り.json")
        flag = await download_tag_json(arg)
        if flag:
            return await setu.finish(f"Tag {arg} 添加成功")
        else:
            return await setu.finish(f"Tag {arg} 添加失败")
    elif cmd == "tag" or cmd == "标签":
        illust_list, illust_info = await get_tag_setu(arg)
        if illust_list == []:
            return await setu.finish(f"没有{user_name}要的{arg}涩图，私密马赛desu")
        await send_images_from_list(illust_list, bot, user_id)
        info = f"PID{illust_info['illust_id']}， 画师{illust_info['illust_userName']}， 标题{illust_info['illust_title']}"
        return await setu.finish(f"{user_name}要的{arg}涩图，"+info)
    else:
        await setu.finish("目前暂未支持")
    
    
    # if e.__getattribute__("message_type") == "group":
    #     await send_group_msg(bot, str(e.__getattribute__("group_id")), get_image_cq())
    # elif e.__getattribute__("message_type") == "private":
    #     await send_private_msg(bot, str(e.__getattribute__("user_id")), get_image_cq(images_dir+os.path.sep+"62258773_p0.png"))
    # await setu.finish()


async def send_images_from_list(illust_list: list, bot: Bot, user_id: str):
    await setu.send("别急，在下载图")
    for illust_name in illust_list:
        image_path = images_dir+os.path.sep+illust_name
        result = False
        if not os.path.exists(image_path):
            result = await download_setu(illust_name)
            await setu.send("下好了，在发了")
        else:
            logger.info("使用本地缓存图片")
            result = True
        if result:
            # try:
                # if group:
                #     await send_group_img(bot, "641133014", image_path)
                # elif private:
                # await send_private_img(bot, user_id, image_path)
            # except:
            #     await setu.finish("Bot发送图片错误私密马赛desu，敲A1in让他解决")

            await bot.call_api("upload_group_file", **{
                "group_id": "253016320",
                "file": image_path,
                "name": illust_name,
                "folder": "/ff270fff-b39b-4721-a6a2-195ba77714eb"
            })
        else:
            await setu.send("Alin下载图片错误私密马赛desu，敲A1in让他解决")



#setu 从本地标签库里随机抽取一张
#setu pid/编号 id 发指定pid的图片
#setu rank/排行 日/月/年 只支持插画illust模式 发前十张
#setu tag/标签 tag_name 10000users入 只支持全年龄模式 从中随机抽取一张（要检查
#setu user/画师 id 随机发一张该画师的图
#setu add/添加 tag_name 添加本地标签库