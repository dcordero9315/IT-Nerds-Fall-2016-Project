import random
import string


from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()

finished = False
print(word)

count = 0

while not finished:
        if len(word) < 5 or len(word) > 10:
                word = rw.random_word()
                print(word)
        else:
                finished=True


# Random word generated
# word = "random"
# Prompt user to start the game

# while count is less than or equal to 9
while count < 9 :

    wordList = []
    letterList = []

    # Show the number of letters
    print("\nThe word length = ", len(word)) # this is where len(word)
    print("\nWords guessed: ", wordList)
    print("Letters guessed: ", letterList)



    #Prompts the user for a word or letter to be guessed
    guessType = input("\nWould you like to guess a word or letter?:")
    # for item in letterList:
    #    if item in letterGuess or letterGuess :
    # if guessType == word OR Word OR W or w Then Word
    if guessType[0] in ['W', 'w']:
        wordGuess = input("Please guess a word: ")

        if wordGuess != word:
            print("\nSorry! Guess again!")
            wordList.append(wordGuess);
            count += 1
        else:
            print("That is correct! You Win!")
    elif guessType[0] in ['L', 'l']:
        letterGuess = input("Please guess a letter: ")
        for letter in letterList:
            if letterGuess == letterList[letter]:
                print("Sorry! Guess again!")
                count += 1
                letterList.append(letterGuess);
                print(letterList)
    else:
        print("Please retype your selection:")

print (count)

    # Declare empty array for the word

    #guess = input("What is your guess?:")

    #if (guess == word):
    #    print("This has already been guessed")
    #    count += 1

    #elif (guess != word):
     #   print("something else")

    #else:
     #   print("")

    # if letter guess

        # check if it's in word and not in word list
            # print to screen

        # if not display wrong message and part of body
            # add to counter

        # if letter has been used
            # print error
            # add to counter

    # if word guess

        # check if it matches the word
            # Show win screen

        # if does not match word OR has been used before
            # display message and show next body part
            # add to counter

# check counter





