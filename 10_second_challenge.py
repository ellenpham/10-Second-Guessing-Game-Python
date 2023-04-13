import time
import os

name = input("To start the game, please enter your name: ")
print("\n")

while True: #infinite loop
    os.system('clear') # to clear the screen
    print("Hello " + name + "! Welcome to the 10 second guessing game!")
    print("\n")
    print("Instruction\n")
    print("Please hit Enter key when you are ready.")
    print("When you think 10 seconds have passed, hit the Enter key again.")
    print("Are you ready? Press Enter to start...")

    input()
    start = time.time()
    input("Please wait for 10 seconds, then hit Enter...")
    print("\n")
    end = time.time()
    elapsed = end - start

    difference = abs(round(10 - elapsed, 2))

    print("You were " + str(difference) + " seconds out")

    if 0 < difference < 0.5:
        print("Well done! Your guessing were very close!")
        break

    elif 0.5 < difference < 1:
        print("Not bad! But you can do better!")

    else:
        print("Too bad!!! Would you like to try again?")
    
    print("\n")
    input("Having fun? Press Enter to play again!")