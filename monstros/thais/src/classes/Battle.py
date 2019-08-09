from src.classes.Monster import Monster

class Battle:
    @staticmethod
    def battle (monster1: 'Monster', monster2: 'Monster'):
        round = 0

        while True:
            round += 1
            if monster1.life > 0:
                monster1.receba_ataque(monster2)

            if monster2.life > 0:
                monster2.receba_ataque(monster1)

            if monster1.life <= 0:
                winner = monster2
                break
            if monster2.life <= 0:
                winner = monster1
                break
        print("O vencedor foi %s do tipo %s , e durou %s rodadas!" % (winner.nome, winner.type, round))
        return winner