# Instruction:
# Write your guess-the-number game again from scratch to revisit the concepts you learned.
# Change the game's functionality so a user has only a limited number of tries to guess the right number. Which loop will you use for this implementation?
# Write a guess-the-word program. Provide some hints to make it easier. Try to improve on any previous implementations you've created.

import random
answer = random.randint(1, 10)
guess = input("Guess a number that is between 1 and 10. Enter your guess: ")

while guess != str(answer):
    guess = input("Wrong! Please try again: ")

print("Correct! Bye!")