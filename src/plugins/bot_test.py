from nonebot import Bot, on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
import os

from ..util import send_group_msg, send_private_msg, get_image_cq, html_entity

pixiv_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = pixiv_dir + os.path.sep + "images"

test = on_command(cmd="test", rule=to_me(), aliases={"测试"})

# @test.handle()
# async def handle_func(e: Event, bot: Bot, matcher: Matcher, args: Message = CommandArg()):
    # await send_group_msg(bot, "641133014", "test")
    # await send_private_msg(bot, "2973907330", "[CQ:image,file=file:///E:\Trash\QQBot\Alin\src\plugins\pixiv\images\97668606.png,type=show,id=40000]")
    # await send_group_msg(bot, "641133014", "[CQ:image,file=file:///E:\Trash\QQBot\Alin\src\plugins\pixiv\images\97668606.png,type=show,id=40000]")
    
    # f = await bot.call_api("can_send_image")
    # await send_private_msg(bot, "2973907330", str(f))
    # h = '<msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'
    # await send_private_msg(bot, "2973907330", f"[CQ:xml,data={html_entity(h)}")