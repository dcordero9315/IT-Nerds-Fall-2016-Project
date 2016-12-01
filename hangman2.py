
import sys
import string
import getpass
import time
import datetime



# Prompt user to start the game
# Declare empty array for the word

# Random word generated
from random_words import RandomWords
rw = RandomWords()
index = 0
finished = False
guesses = 0
letters_used = " "
words_used = " "
letter_guessed = []


found = False
incorrect = 0
foundinword = 0
game_again = "y"
valid_entry = True
No_of_left_guesses=10;
points = 90;
diffTime =0;
arrDiff = [[1, "Easy, 5-6 characters long"],[2,"Medium, 7-8 characters long"],[3,"Hard, 9-10 characters long"]]
valid_entry = False

while game_again.lower() == "y":

    print('\nLets play Hangman!! \n')
    while not valid_entry:
        numplayers = input("\nEnter the number of players (1 or 2): ")

        if numplayers == '2':
            valid_entry = True
            diffLevel = input("Please select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");
            if diffLevel == '1':
                word =  getpass.getpass("\nWord must be 5 - 6 letters long: Enter your word: ")
            elif diffLevel == '2':
                word =  getpass.getpass("\nWord must be 7 - 8 letters long: Enter your word: ")
            elif diffLevel == '3':
                word =  getpass.getpass("\nWord must be 9 - 10 letters long: Enter your word: ")
            while not finished:
                if diffLevel == '1':
                    if len(word) < 5 or len(word) > 6:
                     word = getpass.getpass("\nWord must be 5 - 6 letters long: Enter your word: ")
                    else:
                        finished=True
                elif diffLevel == '2':
                    if len(word) < 7 or len(word) > 8:
                     word =  getpass.getpass("\nWord must be 7 - 8 letters long: Enter your word: ")
                    else:
                        finished=True
                elif diffLevel == '3':
                    if len(word) < 9 or len(word) > 10:
                     word =  getpass.getpass("\nWord must be 9 - 10 letters long: Enter your word: ")
                    else:
                        finished=True
                else:
                    diffLevel = input("\nPlease select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");

        elif numplayers == '1':
            valid_entry = True
            word = rw.random_word()
            diffLevel = input("\nPlease select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");
            while not finished:
                if diffLevel == '1':
                    if len(word) < 5 or len(word) > 6:
                        word = rw.random_word()
                    else:
                        finished=True
                elif diffLevel == '2':
                    if len(word) < 7 or len(word) > 8:
                        word = rw.random_word()
                    else:
                        finished=True
                elif diffLevel == '3':
                    if len(word) < 9 or len(word) > 10:
                        word = rw.random_word()
                    else:
                        finished=True
                else:
                    diffLevel = input("\nPlease select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");


        else:
            print("Invalid input")
            valid_entry = False

    print("\n*****************************************************************")
    print("* You selected difficulty level of ", arrDiff[int(diffLevel)-1])
    print("* You have 10 incorrect guesses")
    print("* You have 90 points")

    if diffLevel == '1':
        diffTime = 240
    elif diffLevel == '2':
        diffTime = 180
    elif diffLevel == '3':
        diffTime = 120

    print("* You have ", int(diffTime/60) , " minutes to guess the word." )
    print("*****************************************************************\n")

    space = len(word)
    underscore = ("_ " * space)
    print(underscore)

    guessed = dict.fromkeys(word, 0)
    wrong_guessed = dict.fromkeys(word, 0)


    def drawHangman(incorrect):
        if incorrect == 1:
            print("________")
            print("|      |")
            print("|      0")
            print("|       ")
            print("|       ")
        elif incorrect == 2:
            print("________")
            print("|      |")
            print("|      0")
            print("|      |")
            print("|       ")
            print("|       ")
        elif incorrect == 3:
            print("________")
            print("|      |")
            print("|      0")
            print("|     /|")
            print("|       ")
            print("|        ")
        elif incorrect == 4:
            print("________")
            print("|      |")
            print("|      0")
            print("|     /|\ ")
            print("|         ")
            print("|         ")
        elif incorrect == 5:
            print("________ ")
            print("|      | ")
            print("|      0 ")
            print("|     /|\ ")
            print("|     /   ")
            print("|         ")
        elif incorrect == 6:
            print("________")
            print("|      |")
            print("|      0")
            print("|     /|\ ")
            print("|     / \ ")
            print("|         ")

        elif incorrect == 7:
            print("________")
            print("|      |")
            print("|      0")
            print("|    \/|\ ")
            print("|     / \ ")
            print("|         ")

        elif incorrect == 8:
            print("________")
            print("|      |")
            print("|      0")
            print("|    \/|\/ ")
            print("|     / \ ")
            print("|         ")

        elif incorrect == 9:
            print("________")
            print("|      |")
            print("|      0")
            print("|    \/|\/ ")
            print("|   __/ \ ")
            print("|         ")

        elif incorrect == 10:
            print("________")
            print("|      |")
            print("|      0")
            print("|    \/|\/ ")
            print("|   __/ \__ ")
            print("|         ")


    correct = 0
    timer = time.time()

    while time.time() - timer < diffTime and incorrect != 10:
        index = 0
        foundinword=0
        var = input("\nGuess a word or letter? ")

        if var.isspace():
            print("\n\n Invalid entry! Please enter a word or a letter!")
            valid_entry = False
        elif not var.isalpha():
            print("\n\n Invalid entry! Please enter a word or a letter!")
            valid_entry = False
        elif var in letter_guessed:
            index = -2
            incorrect += 1
        else:
            valid_entry = True
        if time.time() - timer > diffTime:
            print("\n****Time is up!****")
       #    print(time.time() - timer)
        else:
            #print("index " , index)
            if var == word:
                print("Correct!! You Win!!")
                break
            elif valid_entry is True and index <= 0:
                while index < len(word):
                    if index != -2 :
                        index = word.find(var, index)
                    else:
                        found = False
                    if correct == len(word):
                        break
                    if index == -1 or index == -2:
                        if found == False:
                            incorrect +=1
                            No_of_left_guesses-=1
                            points-=9
                            print("\n*******************************")
                            print ('* Incorrect!')
                            print ("* " + var +  '  - does not exist in this word. ')
                            print("* Number of guesses left:",No_of_left_guesses)
                            print("* Points: ", points)
                            print("*******************************")
                            if len(var) > 1:
                                words_used =  words_used + ' ' + var
                            if len(words_used) > 1:
                                print ('\nwords used: [' + words_used + ']')
                            if len(var) == 1:
                                letters_used =  letters_used + ' ' + var
                            if len(letters_used) > 1:
                                print ('\nletter used: [' + letters_used + ']')
                            if len(letter_guessed) > 0:
                                print ('\nletter guessed:')
                                print (letter_guessed)
                            print ("\n")
                            print(" ".join([ch if guessed[ch] else "_" for ch in word]))
                            drawHangman(incorrect)
                        break
                    else:
                        if var in letter_guessed:
                            correct += 1
                            #correct = correct
                            #print(correct)
                        else:
                            if len(var) > 1:
                                words_used =  words_used + ' ' + var
                                incorrect += 1
                            else:
                                correct += 1
                                letter_guessed.append(var)
                                print ('\nletter guessed:')
                                print (letter_guessed)
                            if len(words_used) > 1:
                                print ('\nwords used: [' + words_used + ']')
                            if len(letters_used) > 1:
                                print ('\nletter used: [' + letters_used + ']')

                        found = True
                        foundinword += 1
                        index += 1
                        guessed[var] = 1
                        print ("\n")

                        if foundinword == 1:
                            drawHangman(incorrect)
                            print("\n")
                            print(" ".join([ch if guessed[ch] else "_" for ch in word]))

                found = False
            if correct == len(word):
                print("\nCorrect!! You Win!!\n")
                print("*******************************")
                print("* Number of guesses left:",No_of_left_guesses,"  *")
                print("* Points: ", points,"                *")
                print("*******************************\n")
                break
    else:
        print("\nYou lose!\n\nThe word was: {}".format(word))
        print("\n**** Game Over *****")
        print("\n*******************************")
        print("* Number of guesses left:",No_of_left_guesses)
        print("* Points: ", points)
        print("*******************************\n")
   # if time.time() - timer > diffTime:
    #    print("Time is up!")
       # print(time.time() - timer)
    game_again = input("\nWould you like to play again? y/n")
    if game_again.lower() == "n":
        print("\nThank you for playing Hangman!")
        break
    else:
        correct = 0
        incorrect = 0
        del letter_guessed[:]
        letters_used = ""
        words_used = ""
        finished = False
        points = 90
        No_of_left_guesses=10
        valid_entry = False



