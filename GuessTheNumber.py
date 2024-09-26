"""
Create a simple number guessing game. 
The program should generate a random number between 1 and 30, and the user should guess the number.
The program should continue to prompt the user until they guess the correct number.
"""
import random

answer = random.randrange(0,30)
guess = int(input("enter a number between 0 and 30:"))
while guess != answer:
    print("try again!")
    guess = int(input("enter a number between 0 and 30:"))
else: print("You got it right! The answer is " + str(answer))