import string

# Prompt user to start the game
# Declare empty array for the word

# Random word generated
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()
index = 0
finished = False
guesses = 0
letters_used = " "
words_used = " "
found = False
incorrect = 0
foundinword = 0

print('Lets play Hangman!!')
print ('')
#print (word)
#print(len(word))
while not finished:
        if len(word) < 5 or len(word) > 10:
                word = rw.random_word()
                #print(word)
        else:
                finished=True

#print(len(word))

space = len(word)
underscore = ("_ " * space)
print(underscore)

guessed = dict.fromkeys(word, 0)
wrong_guessed = dict.fromkeys(word, 0)

correct = 0
def drawHangman(incorrect):
    if incorrect == 1:
        print("________ ")
        print("|      | ")
        print("|        ")
        print("|        ")
        print("|        ")
        print("|        ")
    elif incorrect == 2:
        print("________")
        print("|      |")
        print("|      0")
        print("|       ")
        print("|       ")
    elif incorrect == 3:
        print("________")
        print("|      |")
        print("|      0")
        print("|     / ")
        print("|       ")
        print("|       ")
    elif incorrect == 4:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|")
        print("|       ")
        print("|        ")
    elif incorrect == 5:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|         ")
        print("|         ")
    elif incorrect == 6:
        print("________ ")
        print("|      | ")
        print("|      0 ")
        print("|     /|\ ")
        print("|     /   ")
        print("|         ")
    elif incorrect == 7:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     / \ ")
        print("|         ")

    elif incorrect == 8:
        print("________")
        print("|      |")
        print("|      0")
        print("|     /|\ ")
        print("|     / \ ")
        print("|         ")

    elif incorrect == 9:
        print("________")
        print("|      |")
        print("|      0")
        print("|    \/|\ ")
        print("|     / \ ")
        print("|         ")

    else:
        print("________")
        print("|      |")
        print("|      0")
        print("|    \/|\/ ")
        print("|     / \ ")
        print("|         ")



while incorrect<10:
    index = 0
    foundinword=0
    var = input("\nWhat's your guess? ")

    if var.isspace():
       print("\n\n Please enter your guess!")
    if not var.isalpha():
       print("\n\n Please enter a letter!")
    


    if var == word:
        print("Correct!! You Win!!")
        break
    else:

        while index < len(word):
            index = word.find(var, index)
            if correct == len(word):
                print("Correct!! You Win!!")
                break
            if index == -1:

                if found == False:
                    incorrect +=1
                    print ('\nIncorrect!')
                    print ("\n" + var +  '  - does not exist in this word. ')
                    if len(var) > 1:
                        words_used =  words_used + ' ' + var
                    if len(words_used) > 1:
                        print ('\nwords used: [' + words_used + ']')
                    if len(var) == 1:
                        letters_used =  letters_used + ' ' + var
                    if len(letters_used) > 1:
                        print ('\nletter used: [' + letters_used + ']')
                    print ("\n")
                    print(" ".join([ch if guessed[ch] else "_" for ch in word]))
                    drawHangman(incorrect)
                break
            else:
                found = True
                foundinword += 1
                index += 1
                guessed[var] = 1
                correct += 1
                print ("\n")
                if foundinword == 1:
                    print(" ".join([ch if guessed[ch] else "_" for ch in word]))
        found = False
else:
    print("\nYou lose!\n\nThe word was: {}".format(word))



