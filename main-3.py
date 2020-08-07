import random
import time


class Character():
    def __init__(self, name, health, punch_power, kick_power, special_power, special_name,defense):
        self.name = name
        self.health = health
        self.punch_power = punch_power
        self.kick_power = kick_power 
        self.special_power = special_power
        self.special_name = special_name
        self.defense = defense

    def __str__(self):
        return '''
        Name: %s
        Health: %s
        Punch Power: %s
        Kick Power: %s
        Special Power: %s (%d)
        Defense: %s
        ''' % (self.name, self.health, self.punch_power, self.kick_power, self.special_name, self.special_power, self.defense)

    def kick(self, opponent):
        if self.kick_power == "low":
            kick = random.randint(1,3)
        if self.kick_power == "medium":
            kick = random.randint(4,6)
        if self.kick_power == "high":
            kick = random.randint(7,9)
        defense = opponent.add_defense()
        if defense > kick:
            defense = kick
        opponent.health -= (kick - defense)
        print("%s kicked for %d damage to %s." %(self.name, kick, opponent.name))
        print("%s blocked with %d defense and has %d health left." % (opponent.name, defense, opponent.health))

    def punch(self, opponent):
        if self.punch_power == "low":
            punch = random.randint(1,3)
        if self.punch_power == "medium":
            punch = random.randint(4,6)
        if self.punch_power == "high":
            punch = random.randint(7,9)
        defense = opponent.add_defense()
        if defense > punch:
            defense = punch
        opponent.health -= (punch - defense)
        print("%s punched for %d damage to %s." %(self.name, punch, opponent.name))
        print("%s blocked with %d defense and has %d health left." % (opponent.name, defense, opponent.health))

    def special(self, opponent):
        defense = opponent.add_defense()
        if defense > self.special_power:
            defense = self.special_power
        opponent.health -= (self.special_power - defense)
        print("%s used %s for %d damage to %s." %(self.name, self.special_name, self.special_power, opponent.name))
        print("%s blocked with %d defense and has %d health left." % (opponent.name, defense, opponent.health))

    # def rand_attack(self, opponent):
    #     random_selection = random.randint(1,3)
    #     if random_selection == 1:
    #         self.punch(opponent)
    #     if random_selection == 2:
    #         self.kick(opponent)
    #     if random_selection == 3:
    #         self.special(opponent)
        
    def is_alive(self):
        return self.health > 0

    def add_defense(self):
        if self.defense == "low":
            return random.randint(1,3)
        if self.defense == "medium":
            return random.randint(4,6)
        if self.defense == "high":
            return random.randint(7,9)

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
character1 = Character("K. Relly", 50, "high", "high", 30, "Acid Drool", "low")
character2 = Character("Charg'n Ryno", 50, "medium", "low", 30, "Taekwon Leap", "medium")
character3 = Character("Cave Dolòn", 50, "high", "low", 30, "Nutcracker Choke", "high")
character4 = Character("Snake Jodgel", 50, "high", "medium", 30, "Eye Gouge", "low")
character5 = Character("Ron Sheid", 50, "low", "low", 30, "Bitch Slap", "high")
character6 = Character("Justin", 50, "high", "low", 30, "Words Of Fury", "medium")
character7 = Character("NeckBreakin Brit", 50, "low", "high", 30, "Roundhouse Kick To The Face", "high")
character8 = Character("Crazyeyes Chris", 50, "high", "medium", 30, "Stare Of Death", "medium")
character9 = Character("Yelrac Zil", 50, "high", "high", 30, "Teleport & Attack From Behind", "low")


print("""
@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@@@@   @@@  @@@  @@@   @@@@@@   @@@       
@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@  @@@@ @@@  @@@@@@@@  @@@       
  @@!    @@!       @@!  @@@  @@! @@! @@!  @@!  @@!@!@@@  @@!  @@@  @@!       
  !@!    !@!       !@!  @!@  !@! !@! !@!  !@!  !@!!@!@!  !@!  @!@  !@!       
  @!!    @!!!:!    @!@!!@!   @!! !!@ @!@  !!@  @!@ !!@!  @!@!@!@!  @!!       
  !!!    !!!!!:    !!@!@!    !@!   ! !@!  !!!  !@!  !!!  !!!@!!!!  !!!       
  !!:    !!:       !!: :!!   !!:     !!:  !!:  !!:  !!!  !!:  !!!  !!:       
  :!:    :!:       :!:  !:!  :!:     :!:  :!:  :!:  !:!  :!:  !:!   :!:      
   ::     :: ::::  ::   :::  :::     ::    ::   ::   ::  ::   :::   :: ::::  
   :     : :: ::    :   : :   :      :    :    ::    :    :   : :  : :: : :  
                                                                             
                                                                             
@@@  @@@   @@@@@@   @@@@@@@@@@   @@@@@@@    @@@@@@   @@@@@@@                 
@@@  @@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@                 
@@!  !@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@    @@!                   
!@!  @!!  !@!  @!@  !@! !@! !@!  !@   @!@  !@!  @!@    !@!                   
@!@@!@!   @!@  !@!  @!! !!@ @!@  @!@!@!@   @!@!@!@!    @!!                   
!!@!!!    !@!  !!!  !@!   ! !@!  !!!@!!!!  !!!@!!!!    !!!                   
!!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!    !!:                   
:!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!    :!:                   
 ::  :::  ::::: ::  :::     ::    :: ::::  ::   :::     ::                   
 :   :::   : :  :    :      :    :: : ::    :   : :     :                    
                                                                                         
""")

time.sleep(2)
input("Press any key to continue\n \n \n")

def opponents_list():
    #Make a character list and opponent list
    character_list = [character1, character2, character3, character4, character5, character6, character7, character8, character9]
    opponent_list = []
    #when user selects a character, it moves remaining characters to opponents list for battle
    for character in character_list:
        if player != character:
            opponents = opponent_list.append(character)
            return opponents

def start():
    #print list of characters and their attributes
    print(character1, character2, character3, character4, character5, character6, character7, character8, character9)

    #Looping user input to choose character
    while True:
        character_choice = input("Choose your player: (1 - 9) ")
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
            print("Typing is hard, yo!")

        opponent_list = opponents_list()
        

#Return to Game play
def keep_playing():
    while len(opponent_list) >= 1:
        keep_playing = input("Do you want to keep fighting? (y or n) ")
        if keep_playing == 'y':
            player.health = 50
            print("\nYou have absorbed power from your opponent!")
            print("You're back to Full Health: %d \n" % (player.health))
            print("Your next opponent is: %s" % (opponent_list[0]))
            print("""
                                             
@@@@@@@@  @@@   @@@@@@@@  @@@  @@@  @@@@@@@  
@@@@@@@@  @@@  @@@@@@@@@  @@@  @@@  @@@@@@@  
@@!       @@!  !@@        @@!  @@@    @@!    
!@!       !@!  !@!        !@!  @!@    !@!    
@!!!:!    !!@  !@! @!@!@  @!@!@!@!    @!!    
!!!!!:    !!!  !!! !!@!!  !!!@!!!!    !!!    
!!:       !!:  :!!   !!:  !!:  !!!    !!:    
:!:       :!:  :!:   !::  :!:  !:!    :!:    
 ::        ::   ::: ::::  ::   :::     ::    
 :        :     :: :: :    :   : :     :
 """)
            fight()
        elif keep_playing == 'n':
            print("Quitters never win!")
            print("")
            print("")
            print("""
                                                                                       
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :                                                                                                    
            """)
            break
        else:
            print("Typing is hard, yo!")

# Game Fight function            
def fight():



    player = start()
    # #Make a character list and opponent list
    # character_list = [character1, character2, character3, character4, character5, character6, character7, character8, character9]
    # opponent_list = []
    # #when user selects a character, it moves remaining characters to opponents list for battle
    # for character in character_list:
    #     if player != character:
    #         opponent_list.append(character)




    print("You have choosen %s" %(player))
    print()
    print(story)

    ready = input("Are you ready to fight? (y or n) ")
    if ready == "y":
        print("Good Luck!\n")
    else:
        print("Too bad! Time to fight!\n")
        
    print("Your first opponent is: %s" %(opponent_list[0]))
    print(""" 
    
    @@@@@@@@  @@@   @@@@@@@@  @@@  @@@  @@@@@@@  
    @@@@@@@@  @@@  @@@@@@@@@  @@@  @@@  @@@@@@@  
    @@!       @@!  !@@        @@!  @@@    @@!    
    !@!       !@!  !@!        !@!  @!@    !@!    
    @!!!:!    !!@  !@! @!@!@  @!@!@!@!    @!!    
    !!!!!:    !!!  !!! !!@!!  !!!@!!!!    !!!    
    !!:       !!:  :!!   !!:  !!:  !!!    !!:    
    :!:       :!:  :!:   !::  :!:  !:!    :!:    
    ::        ::   ::: ::::  ::   :::     ::    
    :        :     :: :: :    :   : :     :
    """)
    while opponent_list[0].health > 0 and player.health > 0:
        
        print()
        print("What do you want to do?")
        print("1. Kick")
        print("2. Punch")
        print("3. %s" % (player.special_name))
        print("4. Flee")
        print(">>> ",)
        user_input = input()
#Kick
        if user_input == "1":
            # Player attacks opponent
            player.kick(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                print("""
                                                               
@@@  @@@  @@@   @@@@@@@  @@@@@@@   @@@@@@   @@@@@@@   @@@ @@@  
@@@  @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  
@@!  @@@  @@!  !@@         @@!    @@!  @@@  @@!  @@@  @@! !@@  
!@!  @!@  !@!  !@!         !@!    !@!  @!@  !@!  @!@  !@! @!!  
@!@  !@!  !!@  !@!         @!!    @!@  !@!  @!@!!@!    !@!@!   
!@!  !!!  !!!  !!!         !!!    !@!  !!!  !!@!@!      @!!!   
:!:  !!:  !!:  :!!         !!:    !!:  !!!  !!: :!!     !!:    
 ::!!:!   :!:  :!:         :!:    :!:  !:!  :!:  !:!    :!:    
  ::::     ::   ::: :::     ::    ::::: ::  ::   :::     ::    
   :      :     :: :: :     :      : :  :    :   : :     :

                """)
                opponent_list.pop(0)
                # Day 2 refactor.  Added new fuction to fix while loop "slap in the face".
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else: 
                    print(ending_story)
                    break
#Punch
        elif user_input == "2":
            # Player attacks opponent
            player.punch(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                print("""
                                                               
@@@  @@@  @@@   @@@@@@@  @@@@@@@   @@@@@@   @@@@@@@   @@@ @@@  
@@@  @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  
@@!  @@@  @@!  !@@         @@!    @@!  @@@  @@!  @@@  @@! !@@  
!@!  @!@  !@!  !@!         !@!    !@!  @!@  !@!  @!@  !@! @!!  
@!@  !@!  !!@  !@!         @!!    @!@  !@!  @!@!!@!    !@!@!   
!@!  !!!  !!!  !!!         !!!    !@!  !!!  !!@!@!      @!!!   
:!:  !!:  !!:  :!!         !!:    !!:  !!!  !!: :!!     !!:    
 ::!!:!   :!:  :!:         :!:    :!:  !:!  :!:  !:!    :!:    
  ::::     ::   ::: :::     ::    ::::: ::  ::   :::     ::    
   :      :     :: :: :     :      : :  :    :   : :     :

""")
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else: 
                    print(ending_story)
                    break
        
#Special                
        elif user_input == "3":
            # Player attacks opponent
            player.special(opponent_list[0])
            if opponent_list[0].is_alive() == False:
                print("%s is dead.\n" % (opponent_list[0].name))
                print("")
                print("""
                                                               
@@@  @@@  @@@   @@@@@@@  @@@@@@@   @@@@@@   @@@@@@@   @@@ @@@  
@@@  @@@  @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@  @@@ @@@  
@@!  @@@  @@!  !@@         @@!    @@!  @@@  @@!  @@@  @@! !@@  
!@!  @!@  !@!  !@!         !@!    !@!  @!@  !@!  @!@  !@! @!!  
@!@  !@!  !!@  !@!         @!!    @!@  !@!  @!@!!@!    !@!@!   
!@!  !!!  !!!  !!!         !!!    !@!  !!!  !!@!@!      @!!!   
:!:  !!:  !!:  :!!         !!:    !!:  !!!  !!: :!!     !!:    
 ::!!:!   :!:  :!:         :!:    :!:  !:!  :!:  !:!    :!:    
  ::::     ::   ::: :::     ::    ::::: ::  ::   :::     ::    
   :      :     :: :: :     :      : :  :    :   : :     :

""")
                opponent_list.pop(0)
                if len(opponent_list) >= 1:
                    keep_playing()
                    break
                else: 
                    print(ending_story)
                    break
#RUN AWAY!!!!
        elif user_input == "4":
            print("Quitters never Win!")
            break
        else:
            print("Your keyboard skills need some work! You missed your attack chance!")
#Computer ATTACKS!
        if player.health > 0:
            # Opponent attacks player
            # opponent_list[0].rand_attack(player)
            #Day2 Added random computer attacks
            random_selection = random.randint(1,3)
            if random_selection == 1:
                opponent_list[0].punch(player)
            if random_selection == 2:
                opponent_list[0].kick(player)
            if random_selection == 3:
                opponent_list[0].special(player)
            if player.is_alive() == False:
                print("%s is dead." %(player.name))
                print("")
                print("")
                print("""                  
@@@ @@@   @@@@@@   @@@  @@@  @@@  @@@@@@@   @@@@@@@@  
@@@ @@@  @@@@@@@@  @@@  @@@   @@  @@@@@@@@  @@@@@@@@  
@@! !@@  @@!  @@@  @@!  @@@  @!   @@!  @@@  @@!       
!@! @!!  !@!  @!@  !@!  @!@       !@!  @!@  !@!       
 !@!@!   @!@  !@!  @!@  !@!       @!@!!@!   @!!!:!    
  @!!!   !@!  !!!  !@!  !!!       !!@!@!    !!!!!:    
  !!:    !!:  !!!  !!:  !!!       !!: :!!   !!:       
  :!:    :!:  !:!  :!:  !:!       :!:  !:!  :!:       
   ::    ::::: ::  ::::: ::       ::   :::   :: ::::  
   :      : :  :    : :  :         :   : :  : :: ::   
                                                      
                                                      
@@@@@@@   @@@@@@@@   @@@@@@   @@@@@@@                 
@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@                
@@!  @@@  @@!       @@!  @@@  @@!  @@@                
!@!  @!@  !@!       !@!  @!@  !@!  @!@                
@!@  !@!  @!!!:!    @!@!@!@!  @!@  !@!                
!@!  !!!  !!!!!:    !!!@!!!!  !@!  !!!                
!!:  !!!  !!:       !!:  !!!  !!:  !!!                
:!:  !:!  :!:       :!:  !:!  :!:  !:!                
 :::: ::   :: ::::  ::   :::   :::: ::                
:: :  :   : :: ::    :   : :  :: :  :             
                """)
                #End Day 2:  Need to fix
                while True:
                    punk = input("You feeling lucky ..... punk?! (y or n) ")
                    if punk == 'y':
                        player.health = 50
                        
                        print("")
                        print("")
                        print("Ok. It's your funeral.")
                        print("")
                        print("""
$$\                                $$\ $$\                                 
$$ |                               $$ |\__|                                
$$ |      $$$$$$\   $$$$$$\   $$$$$$$ |$$\ $$$$$$$\   $$$$$$\              
$$ |     $$  __$$\  \____$$\ $$  __$$ |$$ |$$  __$$\ $$  __$$\             
$$ |     $$ /  $$ | $$$$$$$ |$$ /  $$ |$$ |$$ |  $$ |$$ /  $$ |            
$$ |     $$ |  $$ |$$  __$$ |$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |            
$$$$$$$$\\$$$$$$  |\$$$$$$$ |\$$$$$$$ |$$ |$$ |  $$ |\$$$$$$$ |$$\ $$\ $$\ 
\________|\______/  \_______| \_______|\__|\__|  \__| \____$$ |\__|\__|\__|
                                                     $$\   $$ |            
                                                     \$$$$$$  |            
                                                      \______/
                                                                                                    
                                                                                    """)
                        time.sleep (2)
                        input("Press any key to play")
                        start()
                        fight()
                        break
                    elif punk == 'n':
                        print("")
                        print("")
                        print("Quitters never win!")
                        print("")
                        print("")
                        print("""
                                                                                       
 @@@@@@@@   @@@@@@   @@@@@@@@@@   @@@@@@@@      @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@     @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@        @@!  @@@  @@! @@! @@!  @@!          @@!  @@@  @@!  @@@  @@!       @@!  @@@  
!@!        !@!  @!@  !@! !@! !@!  !@!          !@!  @!@  !@!  @!@  !@!       !@!  @!@  
!@! @!@!@  @!@!@!@!  @!! !!@ @!@  @!!!:!       @!@  !@!  @!@  !@!  @!!!:!    @!@!!@!   
!!! !!@!!  !!!@!!!!  !@!   ! !@!  !!!!!:       !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
:!!   !!:  !!:  !!!  !!:     !!:  !!:          !!:  !!!  :!:  !!:  !!:       !!: :!!   
:!:   !::  :!:  !:!  :!:     :!:  :!:          :!:  !:!   ::!!:!   :!:       :!:  !:!  
 ::: ::::  ::   :::  :::     ::    :: ::::     ::::: ::    ::::     :: ::::  ::   :::  
 :: :: :    :   : :   :      :    : :: ::       : :  :      :      : :: ::    :   : :                                                                                                    
                                                                                    """)
                        break
                    else:
                        print("Typing is hard, yo!")

fight()
    




#add play again statment
# if __name__ == '__main__':
#     while True:
#         fight()
#         again = input('Would you like to play again? (y or n')
#         if again in ('y'):
#             break


