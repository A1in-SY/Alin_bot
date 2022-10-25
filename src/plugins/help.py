import nonebot
from nonebot import on_command, on_message, on_startswith
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText, Received

from ..util import send_group_msg, send_private_msg

matcher = on_command(cmd="help", rule=to_me(), aliases={"你能干嘛"})

@matcher.handle()
async def handle_func(e: Event):
    bot = nonebot.get_bot("2675421868")
    return await send_private_msg(bot=bot, user_id="2973907330", message="help")