from nonebot import Bot, on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText

from .arknights import get_arknights_gacha_res
from ...util import check_user_cd, set_user_cd

gacha = on_command(cmd="gacha", rule=to_me() & check_user_cd, aliases={"抽卡"}, priority=5)

game_list = ["明日方舟"]

@gacha.handle()
async def handle_func(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("game&up", args)

@gacha.got(key="game&up", prompt="请输入需要抽卡的游戏及卡池编号，不填卡池编号默认为常驻卡池，目前支持的游戏："+'，'.join(game_list))
async def got_func(e: Event, gu: str = ArgPlainText("game&up")):
    from .arknights import up
    gu = gu.strip()
    user_id = e.get_user_id()
    if " " in gu:
        game_name = gu.split(" ")[0]
        up_id = "arknights_up_" + gu.split(" ")[1]
    else:
        game_name = gu
        up_id = "arknights_up_0"

    # await gacha.send(game_name)
    # await gacha.send(up_id)

    if game_name not in game_list:
        await set_user_cd(user_id)
        await gacha.finish(f"游戏 {game_name} 暂不支持，请重新输入游戏名字")

    if game_name == "明日方舟" and up_id == "arknights_up_卡池":
        s = []
        for index, u in enumerate(up):
            s.append(f"{index} {up[u]['name']}")
        await set_user_cd(user_id)
        await gacha.finish("现在支持的明日方舟卡池及编号:\n"+"\n".join(s))
    
    if game_name == "明日方舟" and up_id in up:
        gacha_res = await get_arknights_gacha_res(str(e.__getattribute__("user_id")), up_id)
        await set_user_cd(user_id)
        await gacha.finish(e.__getattribute__("sender").__getattribute__("nickname")+gacha_res)
    
    await set_user_cd(user_id)
    await gacha.finish("不支持的明日方舟参数")