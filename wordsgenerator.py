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


for i in range(1, 9):
    index = 0
    var = input("\nWhat's your guess? ")

    if var.isspace():
       print("\n\n Please enter your guess!")

    if not var.isalpha():
       print("\n\n Please enter a letter or word!")

    if var in letters_used:
       print("\n\n You have already guessed this letter!")

   
    if var == word:
        print("correct")
        break
    else:


        while index < len(word):
  #  for num in range (0,10):
            index = word.find(var, index)

            if index == -1:
                if found == False:
                    print ('\nIncorrect!')
                    print ("\n" + var +  '  - does not exist in this word. ')
                    if len(var) > 1:
                        words_used =  words_used + ' ' + var
                        #print ('\nwords used: [' + words_used + ']')
                   # else:
                    if len(var) == 1:
                        letters_used =  letters_used + ' ' + var
                    if len(words_used) > 1:
                        print ('\nwords used: [' + words_used + ']')
                    print ('\nletter used: [' + letters_used + ']')
                    print ("\n")
                    print(" ".join([ch if guessed[ch] else "_" for ch in word]))
                break
            else:
                found = True
                #print("\n" + var + ' found at', index)
                index += 1
                guessed[var] = 1
                correct += 1
                print ("\n")
                print(" ".join([ch if guessed[ch] else "_" for ch in word]))
        found = False
else:
    print("\nYou lose!\n\nThe word was: {}".format(word))
#underscore = ("_ " * space)
# print(underscore)


