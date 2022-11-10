from nonebot import Bot, on_command, on_notice
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
import os

from ..util import send_group_msg, send_private_msg, get_image_cq, html_entity

pixiv_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = pixiv_dir + os.path.sep + "images"

# test = on_command(cmd="test", rule=to_me(), aliases={"测试"})
test = on_notice(rule=to_me())

@test.handle()
async def handle_func(e: Event, bot: Bot):
    # await send_group_msg(bot, "641133014", "test")
    # await send_private_msg(bot, "2973907330", "[CQ:image,file=file:///E:\Trash\QQBot\Alin\src\plugins\pixiv\images\97668606.png,type=show,id=40000]")
    # await send_group_msg(bot, "641133014", "[CQ:image,file=file:///E:\Trash\QQBot\Alin\src\plugins\pixiv\images\97668606.png,type=show,id=40000]")
    
    # f = await bot.call_api("can_send_image")
    # await send_private_msg(bot, "2973907330", str(f))
    # h = '<msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>'
    # print(111)
    # await send_private_msg(bot, "2973907330", f"111")
    # await send_private_msg(bot, "2973907330", '[CQ:json,data=[CQ:json,data={"app":"com.tencent.miniapp"&#44;"desc":""&#44;"view":"notification"&#44;"ver":"0.0.0.1"&#44;"prompt":"&#91;应用&#93;"&#44;"appID":""&#44;"sourceName":""&#44;"actionData":""&#44;"actionData_A":""&#44;"sourceUrl":""&#44;"meta":{"notification":{"appInfo":{"appName":"全国疫情数据统计"&#44;"appType":4&#44;"appid":1109659848&#44;"iconUrl":"http:\/\/gchat.qpic.cn\/gchatpic_new\/719328335\/-2010394141-6383A777BEB79B70B31CE250142D740F\/0"}&#44;"data":&#91;{"title":"确诊"&#44;"value":"80932"}&#44;{"title":"今日确诊"&#44;"value":"28"}&#44;{"title":"疑似"&#44;"value":"72"}&#44;{"title":"今日疑似"&#44;"value":"5"}&#44;{"title":"治愈"&#44;"value":"60197"}&#44;{"title":"今日治愈"&#44;"value":"1513"}&#44;{"title":"死亡"&#44;"value":"3140"}&#44;{"title":"今**亡"&#44;"value":"17"}&#93;&#44;"title":"中国加油，武汉加油"&#44;"button":&#91;{"name":"病毒：SARS-CoV-2，其导致疾病命名 COVID-19"&#44;"action":""}&#44;{"name":"传染源：新冠肺炎的患者。无症状感染者也可能成为传染源。"&#44;"action":""}&#93;&#44;"emphasis_keyword":""}}&#44;"text":""&#44;"sourceAd":""}]]')
    # await send_private_msg(bot, "2973907330", "[CQ:share,url=bilibili://space/1954091502,title=测试]")
    
    if e.__getattribute__("group_id") != None:
        group_id = str(e.__getattribute__("group_id"))
        await send_group_msg(bot, group_id, "[CQ:music,type=163,id=1956534872]")
    else:
        await send_private_msg(bot, "2973907330", "[CQ:music,type=163,id=1956534872]")
    
