from nonebot import Bot, on_command
from nonebot.rule import to_me
from nonebot.matcher import Matcher
from nonebot.adapters import Message, Event
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.log import logger
import json
import os
import random

data_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data"

arknights_dir = data_dir + os.path.sep + "arknights" + os.path.sep
rarity_2: list = None
rarity_3: list = None
rarity_4: list = None
rarity_5: list = None
no_rarity_5_times = {} # {"user_id": {"up_id": {"no_rarity_5_times": 0, "total_times": 0, "total_rarity_5_times": 0}}}
up = {} # {"up_id": {"name": "", "rarity_3": [{}], "rarity_4": [], "rarity_5": []}}  {}里为干员信息，多一个"up_to"

def init():
    global rarity_2, rarity_3, rarity_4, rarity_5, no_rarity_5_times, up
    with open(arknights_dir + f"rarity_2.json", "r", encoding="utf-8") as f:
        rarity_2 = json.load(f)
        f.close()
    with open(arknights_dir + f"rarity_3.json", "r", encoding="utf-8") as f:
        rarity_3 = json.load(f)
        f.close()
    with open(arknights_dir + f"rarity_4.json", "r", encoding="utf-8") as f:
        rarity_4 = json.load(f)
        f.close()
    with open(arknights_dir + f"rarity_5.json", "r", encoding="utf-8") as f:
        rarity_5 = json.load(f)
        f.close()
    with open(arknights_dir + f"no_rarity_5_times.json", "r", encoding="utf-8") as f:
        no_rarity_5_times = json.load(f)
        f.close()
    with open(arknights_dir + f"up.json", "r", encoding="utf-8") as f:
        up = json.load(f)
        f.close()
    # random.shuffle(arknights_rate)
    logger.success("gacha_arknights加载完成")
    print(no_rarity_5_times)

async def get_arknights_gacha_res(user_id: str, up_id: str = "arknights_up_0") -> str:
    global rarity_2, rarity_3, rarity_4, rarity_5, no_rarity_5_times
    local_rarity_2 = rarity_2
    local_rarity_3 = rarity_3
    local_rarity_4 = rarity_4
    local_rarity_5 = rarity_5


    # up
    up_rarity_3_num = len(up[up_id]["rarity_3"])
    up_rarity_3_rate = 0
    up_rarity_4_num = len(up[up_id]["rarity_4"])
    up_rarity_4_rate = 0
    up_rarity_5_num = len(up[up_id]["rarity_5"])
    up_rarity_5_rate = 0
    up_rarity_5_id = [] # 给后面up个数用
    for c in up[up_id]["rarity_3"]:
        up_rarity_3_rate += c["up_to"] #up特有
    for c in up[up_id]["rarity_4"]:
        up_rarity_4_rate += c["up_to"]
    for c in up[up_id]["rarity_5"]:
        up_rarity_5_rate += c["up_to"]
        up_rarity_5_id.append(c["id"])
    rarity_3_sum = round((len(local_rarity_3)-up_rarity_3_num)/(1-up_rarity_3_rate))
    rarity_4_sum = round((len(local_rarity_4)-up_rarity_4_num)/(1-up_rarity_4_rate))
    rarity_5_sum = round((len(local_rarity_5)-up_rarity_5_num)/(1-up_rarity_5_rate))
    for c in up[up_id]["rarity_3"]:
        local_rarity_3 += [c]*round(rarity_3_sum*c["up_to"])
    for c in up[up_id]["rarity_4"]:
        local_rarity_4 += [c]*round(rarity_4_sum*c["up_to"])
    for c in up[up_id]["rarity_5"]:
        local_rarity_5 += [c]*round(rarity_5_sum*c["up_to"])


    try:
        no_rarity_5_times_in_up = no_rarity_5_times[user_id][up_id]["no_rarity_5_times"]
        total_times_in_up = no_rarity_5_times[user_id][up_id]["total_times"]
        total_rarity_5_times_in_up = no_rarity_5_times[user_id][up_id]["total_rarity_5_times"]
    except:
        no_rarity_5_times_in_up = 0
        total_times_in_up = 0
        total_rarity_5_times_in_up = 0
    rarity = [] # 抽卡稀有度结果
    arknights_rate = [2]*50 + [3]*40 + [4]*8 + [5]*2 # 抽卡概率

    for i in range(10): # 十连
        if no_rarity_5_times_in_up >= 50: # 99抽保底
            this_time_rate = no_rarity_5_times_in_up + 1
            rate_2 = round((100-(1+this_time_rate-50)*2)/98*50)
            rate_3 = round((100-(1+this_time_rate-50)*2)/98*40)
            rate_4 = round((100-(1+this_time_rate-50)*2)/98*8)
            rate_5 = (1+this_time_rate-50)*2
            if rate_2+rate_3+rate_4+rate_5 > 100:
                rate_2 = rate_2-(rate_2+rate_3+rate_4+rate_5-100)
            arknights_rate = [2]*rate_2 + [3]*rate_3 + [4]*rate_4 + [5]*rate_5

        r = arknights_rate[random.randint(0,99)]
        rarity.append(r)
        if r != 5:
            no_rarity_5_times_in_up = no_rarity_5_times_in_up + 1
        elif r == 5:
            total_rarity_5_times_in_up += 1
            no_rarity_5_times_in_up = 0
            arknights_rate = [2]*50 + [3]*40 + [4]*8 + [5]*2
    total_times_in_up += 10


    # 保存抽卡数据
    no_rarity_5_times[user_id][up_id] = {"no_rarity_5_times": no_rarity_5_times_in_up, "total_times": total_times_in_up, "total_rarity_5_times": total_rarity_5_times_in_up}
    with open(arknights_dir + f"no_rarity_5_times.json", "w", encoding="utf-8") as f:
        json.dump(no_rarity_5_times, f, ensure_ascii=False)
        f.close()


    # 十连保底
    res = []
    up_num = 0
    if rarity == [2]*10:
        rarity[9] = 3
    for r in rarity:
        if r == 2:
            res.append(local_rarity_2[random.randint(0, len(local_rarity_2)-1)]["name"]+" ★3")
        if r == 3:
            res.append(local_rarity_3[random.randint(0, len(local_rarity_3)-1)]["name"]+" ★4")
        if r == 4:
            res.append(local_rarity_4[random.randint(0, len(local_rarity_4)-1)]["name"]+" ★5")
        if r == 5:
            character = local_rarity_5[random.randint(0, len(local_rarity_5)-1)]
            res.append(character["name"]+" ★6")
            if up_id != "arknights_up_0":
                if character["id"] in up_rarity_5_id:
                    up_num += 1


    # 回复文字
    rarity_5_num = str(rarity).count("5")
    if up_id == "arknights_up_0":
        s = f"本次十连寻访共出现{rarity_5_num}个六星干员，寻访结果为：" + "，".join(res)
    else:
        s = f"本次十连寻访共出现{rarity_5_num}个六星干员，{up_num}个UP六星干员，已{no_rarity_5_times_in_up}抽没有出六星干员，寻访结果为：" + "，".join(res)
    return s


if __name__ == "__main__":
    init()
    print(get_arknights_gacha_res())