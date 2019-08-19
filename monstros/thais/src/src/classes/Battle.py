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

        print("Batalha entre %s vs %s" % (monster1.nome, monster2.nome))
        print("O vencedor foi %s do tipo %s, e durou %s rodadas!" % (winner.nome, winner.type, round))
        print()
        winner.life = winner.new_life

        if winner.type == "lutador":
            winner.nivel + 1 and winner.power_def + 6
        if winner.type == "ancião":
            winner.nivel + 7
        if winner.type == "range":
            winner.nivel + 1 and winner.power_at + 6
        if winner.type == "humanoide":
            winner.nivel + 1 and winner.evolution + 1
        if winner.type == "dragão":
            winner.nivel + 1 and winner.life + 100000
        return winner
