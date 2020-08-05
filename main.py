class Character():
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
        print("%s did %d damage to %s." %(self.name, self.attackpower, opponent.name))
        print("%s has %d health left." % (opponent.name, opponent.health))
        
    def is_alive(self):
        return self.health > 0

#Story Line and Instructions
story = """
WELCOME TO THE TOURNAMENT.
You have selected your fighter based on their special attributes and will now face your opponents in a fight to the DEATH.
Each turn you will have the opportunity to choose attack or use an item, and your opponent will be able to attack you.
After each round that you win, you will gain items that you can use to boost your health or give yourself extra attack power.
"""
story2 = """ """

ending_story = """Peace out girl scout"""

#characters
character1 = Character("Character1", 10, 5, 20)
character2 = Character("Character2", 100, 5, 0)
character3 = Character("Character3", 10, 5, 0)

#print list of characters and their attributes
print(character1, character2, character3)
#Looping user input to choose character
while True:
    character_choice = input("Choose your player: ")
    if character_choice == "Character1":
        player = character1
        break
    elif character_choice == "Character2":
        player = character2
        break
    elif character_choice == "Character3":
        player = character3
        break
    else:
        print("Spelling is hard, yo!")
    
#Make a character list and opponent list
character_list = [character1, character2, character3]
opponent_list = []
#when user selects a character, it moves remaining characters to opponents list for battle
for character in character_list:
    if player != character:
        opponent_list.append(character)

print("You have choosen %s." %(player))
print(story)

ready = input("Are you ready to fight? (y or n) ")
if ready == "y":
    print("Good Luck!\n")
else:
    print("Too bad! Time to fight!")
    
print("Your first opponent is: %s" %(opponent_list[0]))
def main():

    while opponent_list[0].health > 0 and player.health > 0:
        
        print()
        print("What do you want to do?")
        print("1. Kick")
        print("2. Punch")
        print("3. Flee")
        print("> ",)
        user_input = input()
#Kick
        if user_input == "1":
            # Player attacks opponent
            player.attack(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing = input("Do you want to keep fighting? (y or n) ")
                    if keep_playing == 'y':
                        player.health += 10
                        player.attackpower += 10
                        player.defense += 10
                        print("\nYou have absorbed power from your opponent!")
                        print("Health: %d \nPower: %d \nDefense: %d \n" % (player.health, player.attackpower, player.defense))
                        print("Your next opponent is: %s" % (opponent_list[0]))
                    else:
                        print("Quitters never win!")
                        break
                else: 
                    print(ending_story)
                    break
#Punch
        elif user_input == "2":
            # Player attacks opponent
            player.attack(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing = input("Do you want to keep fighting? (y or n) ")
                    if keep_playing == 'y':
                        player.health += 10
                        player.attackpower += 10
                        player.defense += 10
                        print("\nYou have absorbed power from your opponent!")
                        print("Health: %d \nPower: %d \nDefense: %d \n" % (player.health, player.attackpower, player.defense))
                        print("Your next opponent is: %s" % (opponent_list[0]))
                    else:
                        print("Quitters never win!")
                        break
                else: 
                    print(ending_story)
                    break
#RUN AWAY!!!!
        elif user_input == "3":
            print("Quitters never Win!")
            break
        else:
            print("Invalid input %r" % user_input)
#Computer ATTACKS!
        if player.health > 0:
            # Opponent attacks player
            opponent_list[0].attack(player)
            if player.is_alive() == False:
                print("%s is dead." %(player.name))


main()
#add play again statment