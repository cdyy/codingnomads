# Instruction:
# Write your guess-the-number game again from scratch to revisit the concepts you learned.
# Change the game's functionality so a user has only a limited number of tries to guess the right number. Which loop will you use for this implementation?
# Write a guess-the-word program. Provide some hints to make it easier. Try to improve on any previous implementations you've created.

import random
answer = random.randint(1, 10)
counter = 3
guess = input("Guess a number that is between 1 and 10. You have 3 tries. Enter your guess: ")

while counter >= 1:
    if guess != str(answer):
        guess = input(f"Wrong! Remaining tries: {counter}. Please try again: ")
        counter -= 1
        continue
    else: 
        print("Correct! Bye!")
        break

if counter < 1:
    print(f"Remaining tries: {counter}. Sorry, you lost. Bye!")