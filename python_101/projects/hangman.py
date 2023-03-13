# game variables

import random
word_list = ["pancake", "lion", "dog"]
answer = random.choice(word_list)
blanks = ["_"] * len(answer)
playerGuess = ""
playerMistakesCount = 0

# game display messages

messageIntro = '''
==================================================================
>> Hangman!
    How to play:
    1/ I think of a word and you try to guess it.
    2/ You make your guess by suggesting letters one at a time.
    3/ You are allowed 8 mistakes.
    * To quit the game, enter "quit".
=================================================================='''

promptGuess  = ">> Your guess: "
messageGuessError = ">> Please enter only one character at a time!"
messageWon = ">> You won! Well done!"
messageLost = ">> You lost! Bye bye!"

# gameplay functions

def isPlayerGuessValid(playerGuess):
    return True if len(playerGuess) == 1 else False

def isPlayerGuessCorrect(playerGuess, answer):
    return True if playerGuess in answer else False

def isGameOver(playerMistakesCount, blanks):
    if playerMistakesCount < 8 and "_" in blanks:
        return False
    else:
        return True

def update_blanks(playerGuess, blanks, answer):
    for i in range(len(answer)):
        if playerGuess == answer[i]:
            blanks[i] = playerGuess

def display_scoreboard(playerMistakesCount, blanks):
    blanks = " ".join(blanks)
    print(f">> {blanks} / Mistakes: {playerMistakesCount}\n")

def display_result(playerMistakesCount, blanks):
    if playerMistakesCount < 8 and "_" not in blanks:
        print(messageWon)
    elif playerMistakesCount >= 8:
        print(messageLost)

# game start

print(messageIntro)
display_scoreboard(playerMistakesCount, blanks)

while isGameOver(playerMistakesCount, blanks) == False:
    playerGuess = input(promptGuess).lower()
    if playerGuess == "quit":
        break
    elif isPlayerGuessValid(playerGuess) == False:
        print(messageGuessError)
        continue   
    elif isPlayerGuessCorrect(playerGuess, answer):
        update_blanks(playerGuess, blanks, answer)
    else:
        playerMistakesCount += 1
    display_scoreboard(playerMistakesCount, blanks)

# game over

display_result(playerMistakesCount, blanks)