from pathlib import Path

from DarkestDungeonClass.dd_game_type.buff.buff import buff_table

files = set(
    [
        i
        for i in Path(r"E:\SteamLibrary\steamapps\common\DarkestDungeon").rglob(
            r"buffs/*.json"
        )
        if "network" not in i.name and "mods" not in str(i)
    ]
)
files |= set(
    Path(r"D:\Program Files\MO2\Game\DarkestDunGeon\mods").rglob(r"buffs/*.json")
)
for i in files:
    print(i)
    try:
        buff_table.model_validate_json(open(i).read()).model_dump_json()
    except Exception as e:
        print(e)
