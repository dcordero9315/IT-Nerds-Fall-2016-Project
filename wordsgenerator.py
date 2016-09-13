import string

# Prompt user to start the game
# Declare empty array for the word

# Random word generated
from random_words import RandomWords
rw = RandomWords()
word = rw.random_word()

finished = False

print (word)
print(len(word))
while not finished:
        if len(word) < 5 or len(word) > 10:
                word = rw.random_word()
                print(word)
        else:
                finished=True

print( len(word))


