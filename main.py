import random
import time
from text import story, title, fight_text, game_over, fatality, loading, ending_story, choose
from classes import Character
from functions import player_selection, ending, character_list, sound, player_defeated, opponent_dead_action
import sys

# Music
from pygame import mixer
mixer.init()
mixer.music.load("audio/TK_Intro_2.wav")
mixer.music.play(-1)


def keep_playing():
    while len(opponent_list) >= 1:
        keep_playing = input("Do you want to keep fighting? (y or n) ")
        if keep_playing == 'y':
            player.health = 50
            print("\nYou have absorbed power from your opponent!")
            print("You're back to Full Health: %d \n" % (player.health))
            print("Your next opponent is: %s" % (opponent_list[0]))
            play_list.pop(0)

            for num in play_list:
                if num == play_list[0]:
                    sound("round" + num + ".wav")

            time.sleep(2)
            fight_text()
            sound("fight.wav")
            fight()
        elif keep_playing == 'n':
            print("Quitters never win!\n\n")
            sound("laugh.wav")
            game_over()
            sys.exit(0)
        else:
            sound("gong.wav")
            print("Typing is hard, yo!\n")


def attack(type, opponent_list):
    # Player attacks opponent
    type(opponent_list[0])
    # mixer.Sound.play(special_se)
    time.sleep(1.5)
    if opponent_list[0].is_alive() == False:
        opponent_dead_action(opponent_list)
        if len(opponent_list) >= 1:
            keep_playing()
            play_list.pop(0)
        else:
            ending()


# Game Fight function
def fight():

    while opponent_list[0].health > 0 and player.health > 0:
        if opponent_list[0].health < 15:
            if opponent_list[0].sex == "F":
                sound("finish_her.wav")
            else:
                sound("finish_him.wav")
        print("\nWhat do you want to do?")
        print("1. Kick")
        print("2. Punch")
        print("3. %s" % (player.special_name))
        print("4. Flee")
        print(">>> ",)
        user_input = input()
# Kick
        if user_input == "1":
            attack(player.kick, opponent_list)
# Punch
        elif user_input == "2":
            attack(player.punch, opponent_list)
# Special
        elif user_input == "3":
            attack(player.special, opponent_list)

# RUN AWAY!!!!
        elif user_input == "4":
            print("QUITTERS NEVER WIN!")
            sound("laugh.wav")
            time.sleep(3)
            sys.exit(0)
        else:
            sound("gong.wav")
            print(
                "Your keyboard skills need some work! You missed your chance to attack!\n")
            time.sleep(1.5)
# Computer ATTACKS!
        if player.health > 0:
            # Opponent attacks player
            opponent_list[0].rand_attack(player)
            if player.is_alive() == False:
                player_defeated(player)


                # print title screen
title()


time.sleep(2)
sound("gong.wav")
input("Press enter to continue\n \n \n")

choose()
player = player_selection()
character_list = character_list()
opponent_list = []
for character in character_list:
    if player != character:
        opponent_list.append(character)


play_list = ['1', '2', '3', '4', '5', '6', '7', '8']

# when user selects a character, it moves remaining characters to opponents list for battle


print("You have choosen %s" % (player))


sound("excellent.wav")
print()
time.sleep(1)
story()
time.sleep(3)
sound("test_your_luck.wav")
ready = input("\nAre you ready to fight? (y or n) ")
if ready == "y":
    print("\nGET READY!\n")
    sound("round1.wav")
else:
    print("\nToo bad! Time to fight!\n")
    sound("laugh.wav")

print("\nYour first opponent is: %s" % (opponent_list[0]))
time.sleep(2)
fight_text()
sound("fight.wav")
fight()
