# Imports
from random_word import RandomWords

# Restart game or not
def exitGame():
    restart = str(input("Do you want to play again (y/n)? "))
    print()
    if restart[0] == 'y':
        return False
    if restart[0] == 'n':
        return True
    else:
        print("Please use 'y' or 'n'")
        return exitGame()

# Main loop
while True:
    # Variables
    gameContinue = True
    lettersFound = 0
    health = 10

    # Choose word and make result list with same length
    wordStr = RandomWords().get_random_word(hasDictionaryDef="true")
    wordLst  = list(wordStr)
    resultLst = []
    usedLetter = []
    for x in range(len(wordLst)):
        resultLst.append("-")

    # Intro
    print("Welcom to Python Hangman")
    print("You start with " + str(health) + " health, good luck!")
    print("-----------------------------------\n")

    # The game
    while gameContinue:
        letterInput = str(input("Guess a letter: "))

        # Checks if letter is in the word or has already been used
        if letterInput in usedLetter:
            print("You already tried that letter")
        elif letterInput in wordLst:
            letterIndex = wordLst.index(letterInput)
            resultLst[letterIndex] = letterInput
            usedLetter.append(letterInput)
            lettersFound += 1
            print("Yes, the word contains the letter '" + letterInput + "' on place " + str(letterIndex+1))
        else:
            health -= 1
            usedLetter.append(letterInput)
            print("No, the word does not contain the letter '" + letterInput + "'")
            print("Health left: " + str(health))

        # Check if game has ended
        if lettersFound == len(wordLst):
            print("\nCongrats, you won!")
            print("The word was: " + wordStr)
            gameContinue = False
        elif health == 0:
            print("\nYou lost!")
            print("The word was: " + wordStr)
            gameContinue = False
        else:
            print("The word: " + ''.join(resultLst) + "\n")

    # Asks if player wants to play again
    if exitGame(): break

# Quit the game
input("Press any key to quit...")