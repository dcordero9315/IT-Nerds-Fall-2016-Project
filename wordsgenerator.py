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
found = False



print (word)
print(len(word))
while not finished:
        if len(word) < 5 or len(word) > 10:
                word = rw.random_word()
                print(word)
        else:
                finished=True

print(len(word))

space = len(word)
underscore = ("_ " * space)
print(underscore)

guessed = dict.fromkeys(word, 0)
wrong_guessed = dict.fromkeys(word, 0)

correct = 0


for i in range(1, 9):
    index = 0
    var = raw_input("What's your guess? ")

    if var == word:
        print("correct")
        break
    else:

        while index < len(word):
  #  for num in range (0,10):
            index = word.find(var, index)

            if index == -1:
                if found == False:
                    print (index)
                    print ('Incorrect!')
                    print (var +  '  - does not exist in this word. ')
                    letters_used =  letters_used + ' ' + var
                    print ('letter used: [' + letters_used + ']')
                break
            else:
                found = True
                print(var + ' found at', index)
                index += 1
                guessed[var] = 1
                correct += 1
                print(" ".join([ch if guessed[ch] else "_" for ch in word]))
        found = False
else:
    print("You lose!\nThe word was {}".format(word))
#underscore = ("_ " * space)
# print(underscore)


