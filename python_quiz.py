import random
import time

def get_tof_statements():

    statements = []
    statements.append(["Is the UK part of the EU", "F"])
    statements.append(["Alliumphobia is a fear of garlic", "T"])
    statements.append(["Electrons move faster than the speed of light", "F"])
    statements.append(["Light travels in a straight line", "T"])

    return statements

def play_tof_quiz():

    #Get true or false statments

    tof_statements = get_tof_statements()

    #Randomise tof statements
    random.shuffle(tof_statements)

    #Set player score to 0
    score = 0

    #Show tof statements using a loop
    for s in  tof_statements:
        #present statment
        print("True or False: " + s[0])
        #user enter guess
        guess = input("Enter T or F: ")
        #check if guess is correct
        if guess == s[1]:
            print("Correct!")
           
            #update score
            score = score + 1
        else:
            print("Incorrect:)")
    #show final score
    print("Your final score is: " + str(score))
    time.sleep(10)

def main_menu():

    print("+--------------------------------+")
    print("| Welcome to Python Quiz 6000!   |")
    print("+--------------------------------+")
    print("| Please select an option:       |")
    print("|                                |")
    print("| 1. Play True or False quiz     |")
    print("| 0 . Quit                       |")
    print("+--------------------------------+")
    choice = input("Enter 1 or 0: ")
    if choice == "1":
        play_tof_quiz()
    elif choice == 0:
        print("Thanks for playing")
        quit()

main_menu()