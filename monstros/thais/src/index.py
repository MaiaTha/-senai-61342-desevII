from src.classes.Monster import Monster

new_monster2 = Monster("Robozão", "aço", 1, 10, 1000, 4, 6)
new_monster3 = Monster("Predeira Parafuso", "pedra", 5, 8, 900, 1, 1)
new_monster4 = Monster("android", "samsung", 8, 2, 20, 2, 1)
new_monster5 = Monster("Geladeira", "brastemp", 6, 8, 1800, 2, 6)
new_monster6 = Monster("Porquinha", "youtuber", 8, 5, 1400, 2, 6)

monsters = [new_monster2,new_monster3]

print("#############----- Battle Royal CETIND -----############")

turn = 1
while monsters[0].life > 0 and monsters[1].life > 0:
    print("###----------------Round %s---------------------###" % turn)
    turn += 1

    if monsters[0].life > 0:
        monsters[0].receba_ataque(monsters[1])

    if monsters[1].life > 0:
        monsters[1].receba_ataque(monsters[0])
