from src.classes.Monster import Monster
from src.classes.Battle import Battle

new_monster2 = Monster("Robozão", "aço", 1, 10, 1000, 4, 6)
new_monster3 = Monster("Predeira Parafuso", "pedra", 5, 8, 900, 1, 1)
new_monster4 = Monster("android", "samsung", 8, 2, 20, 2, 1)
new_monster5 = Monster("Geladeira", "brastemp", 6, 8, 1800, 2, 6)
new_monster6 = Monster("Porquinha", "youtuber", 8, 5, 1400, 2, 6)
new_monster7 = Monster("toquinho", "eletricista", 4, 5, 100, 2, 6)
new_monster8 = Monster("Frizza", "Sayajin", 8, 5, 400, 2, 10)
new_monster9 = Monster("reyals", "apresentadora", 8, 5, 900, 2, 4)

battle = Battle()
oitavas = []
semi = []
final = []

oitavas.append(new_monster2)

print("#############----- Battle Royal CETIND -----############")

print("Oitavas")
semi.append(battle.battle(oitavas[0], oitavas[1])
            )