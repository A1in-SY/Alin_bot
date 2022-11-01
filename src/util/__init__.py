import nonebot
from nonebot import Bot
from nonebot.adapters import Event
from nonebot.log import logger
import time
import html

def get_date() -> str:
    time_array = time.localtime(time.time())
    return time.strftime("%b-%d-%Y", time_array)

async def send_group_msg(bot: Bot, group_id: str, message: str, auto_escape: bool = False):
    return await bot.call_api("send_group_msg", **{
        "group_id": group_id,
        "message": message,
        "auto_escape": auto_escape
    })

async def send_private_msg(bot: Bot, user_id: str, message: str, auto_escape: bool = False):
    return await bot.call_api("send_private_msg", **{
        "user_id": user_id,
        "message": message,
        "auto_escape": auto_escape
    })

async def send_group_img(bot: Bot, group_id: str, img_path: str, auto_escape: bool = False):
    return await bot.call_api("send_group_msg", **{
        "group_id": group_id,
        "message": get_image_cq(img_path),
        "auto_escape": auto_escape
    })

async def send_private_img(bot: Bot, user_id: str, img_path: str, auto_escape: bool = False):
    return await bot.call_api("send_private_msg", **{
        "user_id": user_id,
        "message": get_image_cq(img_path),
        "auto_escape": auto_escape
    })

def get_image_cq(file_path: str):
    return f"[CQ:image,file=file:///{file_path},type=show,id=40000]"

def html_entity(content: str):
    content = content.replace("&", "&amp;")
    content = html.escape(content)
    return content

user_cd = {}
async def check_user_cd(e: Event) -> bool:
    user_id = e.get_user_id()
    if user_id not in user_cd:
        return True
    else:
        now_timestamp = time.time()
        last_commad_timestamp = user_cd[user_id]
        if int(now_timestamp-last_commad_timestamp) > 1:
            return True
        else:
            logger.warning(f"{user_id}还在cd中")
            return False

async def set_user_cd(user_id: str) -> None:
    now_timestamp = time.time()
    user_cd[user_id] = now_timestamp
    return