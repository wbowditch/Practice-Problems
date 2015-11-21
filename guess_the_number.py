#Will Bowditch
#Lab 2: Guess the Number

import random

goal = random.randint(0,1000)

guess = 1001

while guess != goal:
    guess = int(raw_input("Guess the number between 0 and 1000: "))
    if guess > goal:
        print "Too high! Guess again."
    if guess < goal:
        print "Too low! Guess again."

        
print "You guessed the right number!"
