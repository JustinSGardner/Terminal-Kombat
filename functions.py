import time
import sys
from pygame import mixer
from classes import Character
from text import victory, ending_story, fatality


mixer.init()


# Character Functions and Definitions

character1 = Character("K. Relly", 50, "high", "high",
                       30, "Acid Drool", "low", "M")
character2 = Character("Charg'n Ryno", 50, "medium", "low",
                       30, "Gor'n Horn Of Pain", "medium", "M")
character3 = Character("NeckBreakin Brit", 50, "low",
                       "high", 30, "Roundhouse Kick To The Face", "high", "F")
character4 = Character("Snake Jodgel", 50, "high",
                       "medium", 30, "Eye Gouge", "low", "M")
character5 = Character("Ron Sheid", 50, "low", "low",
                       30, "Bitch Slap", "high", "M")
character6 = Character("Justin", 50, "high", "low", 30,
                       "Words Of Fury", "medium", "M")
character7 = Character("Cave Dolòn", 50, "high", "low",
                       30, "Nutcracker Choke", "high", "M")
character8 = Character("Crazyeyes Chris", 50, "high",
                       "medium", 30, "Stare Of Death", "medium", "M")
character9 = Character("Yelrac Zil", 50, "high", "high",
                       30, "Teleport & Attack From Behind", "high", "F")


def character_list():
    return [character1, character2, character3, character4, character5, character6, character7, character8, character9]


def print_character_menu(pos1, char1, pos2, char2, pos3, char3):
    print("-" * 110)
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Name:", (pos1 + char1.name), (pos2 + char2.name), (pos3 + char3.name)))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Health:", char1.health, char2.health, char3.health))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Punch:", char1.punch_power.title(), char2.punch_power.title(), char3.punch_power.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Kick:", char1.kick_power.title(), char2.kick_power.title(), char3.kick_power.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Defense:", char1.defense.title(), char2.defense.title(), char3.defense.title()))
    print("{:<10}|| {:<30}|| {:<30}|| {:<30}|".format(
        "Special:", char1.special_name, char2.special_name, char3.special_name))
    print("-" * 110)


def player_selection():
    print_character_menu("1. ", character1, "2. ",
                         character2, "3. ", character3)
    print_character_menu("4. ", character4, "5. ",
                         character5, "6. ", character6)
    print_character_menu("7. ", character7, "8. ",
                         character8, "9. ", character9)

# Looping user input to choose character
    while True:
        character_choice = input("Who will it be? (1-9) ")
        if character_choice == "1":
            player = character1
            return player
        elif character_choice == "2":
            player = character2
            return player
        elif character_choice == "3":
            player = character3
            return player
        elif character_choice == "4":
            player = character4
            return player
        elif character_choice == "5":
            player = character5
            return player
        elif character_choice == "6":
            player = character6
            return player
        elif character_choice == "7":
            player = character7
            return player
        elif character_choice == "8":
            player = character8
            return player
        elif character_choice == "9":
            player = character9
            return player
        else:
            sound("gong.wav")
            print("Typing is hard, yo!")


# Gameplay Functions

def sound(file):
    sound = mixer.Sound("audio/%s" % file)
    return mixer.Sound.play(sound)


def opponent_dead_action(opponent_list):
    print("%s is dead.\n" % (opponent_list[0].name))
    print("")
    victory()
    sound("impressive.wav")
    opponent_list.pop(0)


def player_defeated(player):
    print("%s is dead.\n\n" % (player.name))
    fatality()
    sound("fatality.wav")
    time.sleep(1.5)
    print("Better luck next time, chump.")
    sound("laugh.wav")
    time.sleep(5)
    sys.exit(0)


def ending():
    time.sleep(1.5)
    ending_story()
    sound("flawless_victory.wav")
    time.sleep(5)
    sys.exit(0)
