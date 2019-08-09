from random import randint


class Monster:
    def __init__(self, nome, type, power_at, power_def,
                 life, evolution, nivel):

        if type == "lutador":
            self.power_def = power_def * nivel
        else:
            self.power_def = power_def
        if type == "ancião":
            self.nivel = nivel * 3
        else:
            self.nivel = nivel
        if type == "range":
            self.power_at = power_at * nivel
        else:
            self.power_at = power_at
        if type == "humanoide":
            self.evolution = evolution * 3
        else:
            self.evolution = evolution
        if type == "dragão":
            self.life = life + life
        else:
            self.life = life

        self.nome = nome
        self.type = type

    def ataque(self):
        return self.power_at * self.evolution * self.nivel * randint(1, 5)

    def defesa(self):
        return self.power_def * self.evolution * self.nivel * randint(1, 3)

    def receba_ataque(self, monster: 'Monster'):
        damage = monster.ataque() - self.defesa()
        if damage < 0:
            damage = 1
        self.life -= damage
