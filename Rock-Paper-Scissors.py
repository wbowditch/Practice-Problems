#Will Bowditch
#Lab 2: Rock-Paper-Scissors
import random

player = ""
while player != "quit":
    player = str(raw_input("Welcome to Rock-Paper Scissors. Choose Rock, Paper, or Scissors. Type 'quit' to quit: "))

    computer = random.choice(["Rock","Paper","Scissors"])
    if player == "Rock" and computer == "Paper":
        print "Computer wins with Paper!"
    if player == "Paper" and computer == "Rock":
        print "Player wins against Rock!"
    if player == "Scissors" and computer == "Rock":
        print "Computer wins with Rock!"
    if player == "Rock" and computer == "Scissors":
        print "Player wins against Scissors!"
    if player == "Paper" and computer  == "Scissors":
        print "Computer wins with Scissors!"
    if player == "Scissors" and computer == "Paper":
        print "Player wins against Scissors!"
    if computer == player:
        print "It was a draw, the computer played ",computer

