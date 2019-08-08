from src.classes.Monster import Monster

class Battle:
    def battle (monster1: Monster, monster2: Monster):

        while monster1.life > 0 and monster2.life > 0:

            if monster1.life > 0:
                monster1.receba_ataque(monster2)

            if monster2.life > 0:
                monster2.receba_ataque(monster1)

        if monster1.life >= 0:
            return monster1
        else:
            return monster2