#==================================================================================================
#Filename : PAZ_Bato-Bato Pick using python.py
#Author : Al Francis B. Paz
#Email : afpaz@gbox.adnu.edu.ph
#Assignment Number(Python) : 2
'''
Description : Bato-Bato Pick using python. Python 3 program so instead of using purely randomized choices, it
will have a semblance of intelligence and adaptability. One approach is to keep track of
how often a user chooses a weapon and use this playing history to determine the best
weapon of choice.
'''
#Last modified: November 20, 2022
#==================================================================================================


import random

random.seed()

keep_playing = 'Y'
rock_played = 0
paper_played = 0
scissors_played = 0
weapon_valid = False
tie_score = 0
computer_score = 0
player_score = 0


while keep_playing != 'Q':

    # Weapon choice
    while weapon_valid == False:
        print("           ")
        print("Bato-Bato Pick!!!")
        print("Please choose your weapon!!!")
        print("\t Type(R or r) to choose Rock")
        print("\t Type(P or p) to choose Paper")
        print("\t Type(S or s) to choose Scissor")
        player_weapon = input("Type here your chosen weapon: ").upper()

        # Weapon validation
        if (player_weapon != ('R')) and (player_weapon != ('P')) and (player_weapon != ('S')):
            print('You have choosen an invalid weapon, please type again')
        else:
            weapon_valid = True

    # Reset weapon validation flag
    weapon_valid = False

    # Player weapon choice
    if (player_weapon == 'R'):
        rock_played += 1
        print('Your chosen weapon is Rock')
    elif (player_weapon == 'P'):
        print('Your chosen weapon is Paper')
        paper_played += 1
    else:
        scissors_played += 1
        print('Your chosen weapon is Scissors')

    # Computer weapon choice
    if (rock_played > paper_played) and (rock_played > scissors_played):
        computer_weapon = 'P'
    elif (paper_played > rock_played) and (paper_played > scissors_played):
        computer_weapon = 'S'
    elif (scissors_played > rock_played) and (scissors_played > paper_played):
        computer_weapon = 'R'
    elif (rock_played == paper_played) and (rock_played > scissors_played):
        computer_weapon = random.choice(['P', 'S'])
    elif (scissors_played == rock_played) and (scissors_played > paper_played):
        computer_weapon = random.choice(['R', 'P'])
    elif (scissors_played == paper_played) and (scissors_played > rock_played):
        computer_weapon = random.choice(['R', 'S'])
    else:
        computer_weapon = random.choice(['R', 'P', 'S'])

    if (computer_weapon == 'R'):
        print('The chosen weapon of the computer is Rock')
    elif (computer_weapon == 'P'):
        print('The chosen weapon of the computer is Paper')
    else:
        print('The chosen weapon of the computer is Scissors')


    # Show the result
    if (player_weapon == computer_weapon):
        print('This round is a tie!')
        tie_score += 1
    elif ((player_weapon == 'R') and (computer_weapon == 'S')) or (
            (player_weapon == 'P') and (computer_weapon == 'R')) or(
            (player_weapon == 'S') and (computer_weapon == 'P')):
        print('You win this round!')
        player_score += 1
    else:
        print('The computer wins this round!')
        computer_score += 1
    print('Here is your current score:')
    print('\t Tie: ', tie_score)
    print('\t Won: ', player_score)
    print('\t Lost: ', computer_score)
    # Keep playing?
    keep_playing = input("Type(Q or q) if you want to Quit the game: ").upper()

print('Here is the final score:')
print('\t Tie: ',tie_score)
print('\t Won: ',player_score)
print('\t Lost: ',computer_score)
print('\t Rocks played: ',rock_played)
print('\t Papers played: ',paper_played)
print('\t Scissors played: ',scissors_played)
print('Thank you for playing!')