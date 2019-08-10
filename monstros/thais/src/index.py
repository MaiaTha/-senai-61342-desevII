from src.classes.Monster import Monster
from src.classes.Battle import Battle

new_monster0 = Monster("Grand", "lutador", 9, 9, 68600, 1, 3)
new_monster1 = Monster("Riskha", "ancião", 5, 5, 30200, 10, 3)
new_monster2 = Monster("Naleme", "range", 8, 5, 48800, 6, 4)
new_monster3 = Monster("Sa'dic", "humanoide", 3, 8, 20900, 7, 6)
new_monster4 = Monster("Nelius", "dragão", 9, 4, 16707, 8, 10)
new_monster5 = Monster("Bagion", "range", 5, 5, 17900, 3, 5)
new_monster6 = Monster("Drornne", "dragão", 9, 5, 44400, 9, 2)
new_monster7 = Monster("Reyals", "humanoide", 3, 7, 29600, 9, 5)

battle = Battle()
oitavas = [
    new_monster0,
    new_monster1,
    new_monster2,
    new_monster3,
    new_monster4,
    new_monster5,
    new_monster6,
    new_monster7
]
semi = []
final = []

print()
print("---------------------Arena Batlle Royal-------------------------")
print("-------------------------OITAVAS--------------------------------")
print()
print()
semi.append(battle.battle(oitavas[0], oitavas[1]))
semi.append(battle.battle(oitavas[2], oitavas[3]))
semi.append(battle.battle(oitavas[4], oitavas[5]))
semi.append(battle.battle(oitavas[6], oitavas[7]))
print("-------------------------SEMI - FINAL---------------------------")
print()
print()
final.append(battle.battle(semi[0], semi[1]))
final.append(battle.battle(semi[2], semi[3]))
print("----------------------------FINAL-------------------------------")
print()
print()
battle.battle(final[0], final[1])
print("----------------------------------------------------------------")

