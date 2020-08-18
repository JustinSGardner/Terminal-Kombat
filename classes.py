import random
import time
from pygame import mixer

mixer.init()
punch_se = mixer.Sound("audio/Punch.wav")
kick_se = mixer.Sound("audio/Kick.wav")
special_se = mixer.Sound("audio/rage_of_blades.wav")


class Character():
    def __init__(self, name, health, punch_power, kick_power, special_power, special_name, defense, sex):
        self.name = name
        self.health = health
        self.punch_power = punch_power
        self.kick_power = kick_power
        self.special_power = special_power
        self.special_name = special_name
        self.defense = defense
        self.sex = sex

    def __str__(self):
        return """
        Name: %s
        Health: %s
        Punch Power: %s
        Kick Power: %s
        Special Power: %s (%d)
        Defense: %s
        """ % (self.name, self.health, self.punch_power, self.kick_power, self.special_name, self.special_power, self.defense)

    def kick(self, opponent):
        if self.kick_power == "low":
            kick = random.randint(1, 3)
        if self.kick_power == "medium":
            kick = random.randint(4, 6)
        if self.kick_power == "high":
            kick = random.randint(7, 9)
        defense = opponent.add_defense()
        if defense > kick:
            defense = kick
        opponent.health -= (kick - defense)
        mixer.Sound.play(kick_se)
        time.sleep(1)
        print("\n\n%s kicked for %d damage to %s." %
              (self.name, kick, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def punch(self, opponent):
        if self.punch_power == "low":
            punch = random.randint(1, 3)
        if self.punch_power == "medium":
            punch = random.randint(4, 6)
        if self.punch_power == "high":
            punch = random.randint(7, 9)
        defense = opponent.add_defense()
        if defense > punch:
            defense = punch
        opponent.health -= (punch - defense)
        mixer.Sound.play(punch_se)
        time.sleep(1)
        print("\n\n%s punched for %d damage to %s." %
              (self.name, punch, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def special(self, opponent):
        defense = opponent.add_defense()
        if defense > self.special_power:
            defense = self.special_power
        opponent.health -= (self.special_power - defense)
        mixer.Sound.play(special_se)
        time.sleep(4)
        print("\n\n%s used %s for %d damage to %s." %
              (self.name, self.special_name, self.special_power, opponent.name))
        print("%s blocked with %d defense and has %d health left." %
              (opponent.name, defense, opponent.health))

    def rand_attack(self, opponent):
        random_selection = random.randint(1, 3)
        if random_selection == 1:
            self.punch(opponent)
        if random_selection == 2:
            self.kick(opponent)
        if random_selection == 3:
            self.special(opponent)

    def is_alive(self):
        return self.health > 0

    def add_defense(self):
        if self.defense == "low":
            return random.randint(1, 3)
        if self.defense == "medium":
            return random.randint(4, 6)
        if self.defense == "high":
            return random.randint(7, 9)
