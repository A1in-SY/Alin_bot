#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter
from loguru import logger

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)


# Please DO NOT modify this file unless you know what you are doing!
# As an alternative, you should use command `nb` or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...

# @driver.on_bot_connect
# async def do_something():
#     bot = nonebot.get_bot("2675421868")
#     await bot.call_api("upload_group_file", **{
#         "group_id": "253016320",
#         "file": "E:\\Trash\\QQBot\\Alin\\src\\plugins\\pixiv\\images\\75743642.png",
#         "name": "test.png",
#         "folder": "/ff270fff-b39b-4721-a6a2-195ba77714eb"
#     })
    # f = await bot.call_api("get_group_root_files", **{
    #     "group_id": "253016320",
    # })
    # await bot.call_api("send_private_msg", **{
    #     "user_id": "2973907330",
    #     "message": str(f)
    # })

# from nonebot.message import event_postprocessor
# from nonebot.adapters import Event
# @event_postprocessor
# async def do_something(e: Event):
#     print(e)
#     pass


if __name__ == "__main__":
    nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
