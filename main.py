class Chararcter():
    def __init__(self, name, health, attackpower, defense):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.defense = defense

    def __str__(self):
        return '''
        Name: %s
        Health: %s
        Power: %d
        Defense: %d
        ''' % (self.name, self.health, self.attackpower, self.defense)

    def attack(self, opponent):
        opponent.health -= self.attackpower


character1 = Chararcter("Character1", 100, 5, 20)
character2 = Chararcter("Character2", 100, 5, 0)
character3 = Chararcter("Character3", 100, 5, 0)

print(chris)
print(enemy)

chris.attack(enemy)
print(enemy)
