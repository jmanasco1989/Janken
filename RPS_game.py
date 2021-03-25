# Rock Paper Scissors (Simple)
# by: Wes Manasco

"""
This game took some inspiration from a few online resources that I cannot find again to credit.
If any of the code looks familiar please let me know.

This game is simply made for me to build and exercise my skills with Python with no intention for profit.
"""

import os
import random
import re
import sys

os.system('cls' if os.name=='nt' else 'clear')

# Display RPS declaration
print("*********************************")
print("*                               *")
print("* Rock, Paper, Scissors, SHOOT! *")
print("*                               *")
print("*********************************")

# Variables
choices = ['R', 'P', 'S']
user_score = 0
cpu_score = 0

# Main loop
while user_score <= 2 and cpu_score <= 2:

    user_choice = input("Choose your weapon: (Type R, P, or S): ").upper()
    if not re.match("^[r,R,p,P,s,S]*$", user_choice):
        print("Error! Only letters R, P, and S are allowed!")
        sys.exit()
    CPU_Choice = random.choice(choices).upper
    print("Player: " + str(user_choice) + " Computer: " + str(CPU_Choice))

    if user_choice == CPU_Choice:
        print("It's A Draw!!!")

    elif user_choice == str('R') and CPU_Choice == str('S'):
        print("Rock crushes scissors, Player wins!")
        user_score += 1
        print("Player: " + str(user_score) + " Computer: " + str(cpu_score))
        continue

    elif user_choice == str('S') and CPU_Choice == str('P'):
        print("Scissors cut paper, Player wins!")
        user_score += 1
        print("Player: " + str(user_score) + " Computer: " + str(cpu_score))
        continue

    elif user_choice == str('P') and CPU_Choice == str('R'):
        print("Paper covers rock, Player wins!")
        user_score += 1
        print("Player: " + str(user_score) + " Computer: " + str(cpu_score))
        continue

    else:
        print("Computer Wins!")
        cpu_score += 1
        print("Player: " + str(user_score) + " Computer: " + str(cpu_score))
        continue
# Janken
