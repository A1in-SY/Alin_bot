import nonebot
from nonebot import Bot
from nonebot import on_command, on_message, on_startswith
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText, Received
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