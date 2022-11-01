import json
import os

data_dir = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + "data"
arknights_dir = data_dir + os.path.sep + "arknights" + os.path.sep

rarity_2 = []
rarity_3 = []
rarity_4 = []
rarity_5 = []

with open(arknights_dir+os.path.sep+"character_table.json", "r", encoding="utf-8") as f:
    characters = json.load(f)
    f.close()

for c in characters:
    if characters[c]["itemObtainApproach"] == "招募寻访":
        t = {
            "id": characters[c]["potentialItemId"],
            "name": characters[c]["name"],
            "rarity": characters[c]["rarity"],
            "isSpChar": characters[c]["isSpChar"],
            "limited_operator": False,
            "only_open_recruitment": False,
            "sp_up_id": None
        }
        if characters[c]["rarity"] == 2:
            rarity_2.append(t)
        if characters[c]["rarity"] == 3:
            rarity_3.append(t)
        if characters[c]["rarity"] == 4:
            rarity_4.append(t)
        if characters[c]["rarity"] == 5:
            rarity_5.append(t)
    
with open(arknights_dir+os.path.sep+"rarity_2.json", "w", encoding="utf-8") as f:
    json.dump(rarity_2, f, ensure_ascii=False)
    f.close()

with open(arknights_dir+os.path.sep+"rarity_3.json", "w", encoding="utf-8") as f:
    json.dump(rarity_3, f, ensure_ascii=False)
    f.close()

with open(arknights_dir+os.path.sep+"rarity_4.json", "w", encoding="utf-8") as f:
    json.dump(rarity_4, f, ensure_ascii=False)
    f.close()

with open(arknights_dir+os.path.sep+"rarity_5.json", "w", encoding="utf-8") as f:
    json.dump(rarity_5, f, ensure_ascii=False)
    f.close()