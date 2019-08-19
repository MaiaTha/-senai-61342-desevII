import json

from src.classes.Monster import Monster
from src.classes.Battle import Battle

arq = open('personagens.json','r')
arq = arq.read()

data = json.loads(arq)

oitavas = []
for personagem in data["personagens"]:

    oitavas.append(
        Monster(
            personagem["name"],
            personagem["type"],
            personagem["power_at"],
            personagem["powe_def"],
            personagem["life"],
            personagem["evolution"],
            personagem["nivel"]
        )
    )


battle = Battle()
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

