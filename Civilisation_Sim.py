# Cool Civilisation Simulaiton Text-Based Game.
import random
import time
import sys
import math

# program variables
program_run = True
menu_option = 0
menu_sub_op = 0

# people class variables
citizen_names = ["John", "Mary", "Cindy", "Clyde", "Bob", "George", "Sully", "Diego", "Karen", "Matilda", "Jeremy", "Josh", "Amelia", "Omar"] # names database will grow, these are placeholders
citizen_traits = ["confident", "wit", "frustration", "impatience", "depression", "big brain", "kindness", "lustful", "greedy", "DETERMINATION", "sincere", "trustworthiness", "happy", "lazy"] # traits the citizens can have
citizens = []
current_citizen = ""
human_task = ""
map_rows = ["[][][][][]", "[][][][][]", "[][]{}[][]", "[][][][][]", "[][][][][]"] # the [] mean empty spaces, the {} means the village center

class people:
    def __init__(self, citizen_names, citizen_traits, citizens, current_citizen, human_task):
        self.citizen_names = citizen_names
        self.citizen_traits = citizen_traits
        self.citizens = citizens
        self.current_citizen = current_citizen
        self.human_task = human_task
    
    def human_create(self):
        self.current_citizen = f"Name: {random.choice(citizen_names)} | Trait: {random.choice(citizen_traits)} | Age: {random.randint(0, 72)}"
        self.citizens.append(self.current_citizen)
        print(f"You have created a human;\n{self.citizens[-1]}")
    
    def check_humans(self):
        print("Humans in Town:")
        for i in self.citizens:
            print(i)
    
    def human_status(self):
        if menu_sub_op == 1:
            self.human_task = "war"
        elif menu_sub_op == 2:
            self.human_task = "scavange"
        elif menu_sub_op == 3:
            self.human_task = "build"

class menus:
    def __init__(self, menu_option, menu_sub_op, program_run):
        self.menu_option = menu_option
        self.menu_sub_op = menu_sub_op
        self.program_run = program_run
    
    def game_start(self):
        print("-- Welcome to CivSim -- \n 1. Start Game \n 2. Options \n 3. About Project \n 4. More Games \n 5. Quit Game")
        self.menu_option = int(input("Menu Option; 1/2/3/4/5: "))

        if self.menu_option == 1:
            pass
        elif self.menu_option == 2:
            print("\nThere are no options, bro this is a text based simulator...\n")
        elif self.menu_option == 3:
            print("\nThis game is being made as a tiny side project for my internship!\n")
        elif self.menu_option == 4:
            print("\nFor more games please check out my;\n 1. itch.io: https://rouzyoqi.itch.io \n 2. website: https://sites.google.com/imas.edu.my/thedevdungeon/home \n 3. GitHub: https://github.com/Rouzyoqi/Rouzyoqi/tree/main")
        elif self.menu_option == 5:
            print("Shutting project down...")
            self.program_run = False



humans = people(citizen_names=citizen_names, citizen_traits=citizen_traits, citizens=citizens, current_citizen=current_citizen, human_task=human_task)

while program_run:
    humans.human_create()

while not program_run:
    sys.exit("program quitted")
