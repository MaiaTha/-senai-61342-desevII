from random import randint


class Monster:
    def __init__(self, nome, type, power_at, power_def,
                 life, evolution, nivel):
        self.nome = nome
        self.type = type
        self.power_at = power_at
        self.power_def = power_def
        self.life = life
        self.evolution = evolution
        self.nivel = nivel

    def ataque(self):
        return self.power_at * self.evolution * self.nivel * randint(1, 5)

    def defesa(self):
        return self.power_def * self.evolution * self.nivel * randint(1, 3)

    def receba_ataque(self, monster: 'Monster'):
        damage = monster.ataque() - self.defesa()
        if damage < 0:
            damage = 1
        self.life -= damage

        print("%s ataca %s" % (monster.nome, self.nome))
        print("%s causa %s de dano!" % (monster.nome, damage))
        if self.life > 0:
            print("%s ainda tem %s de vida!" % (self.nome, self.life))
        else:
            self.life = 0
            print("%s morreu no duelo!" % self.nome)
