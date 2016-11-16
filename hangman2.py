
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


#now = datetime.datetime.now()
#dt = datetime.timedelta (seconds=5)
#then = now + dt
#while datetime.datetime.now() != datetime.datetime.now() + datetime.timedelta (seconds=5):
 #   print (datetime.datetime.now())
   # print (then)

while game_again.lower() == "y":

    print('Lets play Hangman!! \n')

    numplayers = input("\nEnter the number of players (1 or 2): ")


    diffLevel = input("Please select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");

    print("\n*******************************")
    print("* You have 10 incorrect guesses")
    print("* You have 90 points")
    print("* You selected difficulty level of ", arrDiff[int(diffLevel)-1])
    print("*******************************\n")



    if numplayers == '2':
        word =  getpass.getpass("\nEnter your word: ")

        while not finished:
            if diffLevel == '1':
                if len(word) < 5 or len(word) > 6:
                 word =  input("\nWord must be 5 - 6 letters long: Enter your word: ")
                #print(word)
                else:
                    finished=True
            elif diffLevel == '2':
                if len(word) < 7 or len(word) > 8:
                 word =  input("\nWord must be 7 - 8 letters long: Enter your word: ")
                #print(word)
                else:
                    finished=True
            elif diffLevel == '3':
                if len(word) < 9 or len(word) > 10:
                 word =  input("\nWord must be 9 - 10 letters long: Enter your word: ")
                #print(word)
                else:
                    finished=True
            else:
                diffLevel = input("\nPlease select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");

    else:
        word = rw.random_word()
        print ('')
        #print (word)
        #print(len(word))
        while not finished:
            if diffLevel == '1':
                if len(word) < 5 or len(word) > 6:
                    word = rw.random_word()
                #print(word)
                else:
                    finished=True
            elif diffLevel == '2':
                if len(word) < 7 or len(word) > 8:
                    word = rw.random_word()
                #print(word)
                else:
                    finished=True
            elif diffLevel == '3':
                if len(word) < 9 or len(word) > 10:
                    word = rw.random_word()
                #print(word)
                else:
                    finished=True
            else:
                diffLevel = input("\nPlease select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");


#print(len(word))
#    now = datetime.datetime.now()
    #delay = float (input ("enter delay (s): "))

#time based on diffLevel
    if diffLevel == '1':
        diffTime = 3
        #time.sleep(30)
 #       print("Time is up")
    elif diffLevel == '2':
        diffTime = 2
    elif diffLevel == '3':
        diffTime = 1

    #timeout = time.time() + 60*diffTime   # 5 minutes from now
  #  while True:
   #     #test = 0
    #    if time.time() > timeout:
     #       break
      #  #test = test - 1
    #print (timeout)

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
    while incorrect != 10:
        index = 0
        foundinword=0
        var = input("\nWhat's your guess? ")
        #start the timer


        if var.isspace():
            print("\n\n Invalid entry! Please enter a word or a letter!")
            valid_entry = False
        elif not var.isalpha():
            print("\n\n Invalid entry! Please enter a word or a letter!")
            valid_entry = False
        else:
            valid_entry = True

        if var == word:
            print("Correct!! You Win!!")
            break
        elif valid_entry is True:
            while index < len(word):
                index = word.find(var, index)
                if correct == len(word):
                    break
                if index == -1:
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
                        if len(letter_guessed) > 1:
                            print ('\nletter guessed:')
                            print (letter_guessed)
                        print ("\n")
                        print(" ".join([ch if guessed[ch] else "_" for ch in word]))
                        drawHangman(incorrect)
                    break
                else:
                    if var in letter_guessed:
                        correct += 1
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



