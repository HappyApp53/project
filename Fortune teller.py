# The following program generates a fortune-teller game.
import random

def random_number():
    boolean = False

    while not boolean:
        fortune = random.randint(0,10)

        rollDice = input(
            "Greetings good sir! I James Burlingame the second will predict your future. Roll your dice. Figure out the"
            "the future. Will you be a murder or a adventurous and courageous person? It can be anything"
            "So go ahead and roll the dice" )
        if rollDice == "roll" or rollDice == "Roll":
            print("\n" + "Fortune Selected: " + str(fortune))
            if 0 <= fortune <= 3:
                print("Oh no! You selected a low fortune!" + "\n")
            elif 3 < fortune <= 7:
                print("You selected an average fortune." + "\n")
            else:
                print("Congratulations! You selected great fortune." + "\n")

        elif rollDice == "exit" or rollDice == "Exit":
            print("Bye, see you again!")
            boolean = True
        else:
            print("Try again!")

random_number()