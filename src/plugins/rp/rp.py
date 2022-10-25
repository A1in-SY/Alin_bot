import nonebot
from nonebot import on_command, on_message, on_startswith
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText, Received
import random
import time
import pickle
import os

from ...util import send_group_msg, send_private_msg

rp = on_command(cmd="rp", rule=to_me(), aliases={"人品", "今日人品"})

rp_dict = {}
rp_path = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data" + os.path.sep + "rp.pkl"
if os.path.exists(rp_path):
    rp_dict = pickle.load(open(rp_path, "rb"))


@rp.handle()
async def handle_func(e: Event):
    bot = nonebot.get_bot("2675421868")
    user_id = str(e.__getattribute__("user_id"))
    user_name = e.__getattribute__("sender").__getattribute__("nickname")
    rp_time = e.__getattribute__("time")
    private = False
    group = False
    group_id = ""
    msg = ""

    if e.__getattribute__("message_type") == "group":
        group = True
        group_id = e.__getattribute__("group_id")
    elif e.__getattribute__("message_type") == "private":
        private = True
        

    if user_id not in rp_dict:
        rp = roll_rp()
        save(user_id, rp_time, rp)
        msg = f"今日{user_name}运势Roll点：{rp}"
    elif user_id in rp_dict:
        time_array = time.localtime(rp_time)
        rp_date = time.strftime("%b-%d-%Y", time_array)
        last_time_array = time.localtime(rp_dict[user_id]["last_rp_timestamp"])
        last_rp_timestamp = time.strftime("%b-%d-%Y", last_time_array)
        if rp_date == last_rp_timestamp:
            msg = f"今天{user_name}你已经Roll过了的说，改不了的说"
        else:
            rp = roll_rp()
            save(user_id, rp_time, rp)
            msg = f"今日{user_name}运势Roll点：{rp}"

    if group:
        return await send_group_msg(bot, group_id, msg)
    elif private:
        return await send_private_msg(bot, user_id, msg)

def roll_rp():
    rp = random.randint(1, 10)
    return rp

def save(user_id: str, time: int, rp: int):
    rp_dict[user_id] = {"last_rp_timestamp": time, "rp": rp}
    pickle.dump(rp_dict, open(rp_path, "wb"))
    return