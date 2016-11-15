import string
import time
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

print("Hello! Let's Play Hangman!");
diffLevel = input("Please select your difficulty level: \n (1) Easy \n (2) Medium \n (3) Hard \n");

if diffLevel == 1:
    while not finished:
        if len(word) < 5 or len(word) > 6:
            word = rw.random_word()
            # print(word)
        else:
            finished = True
    print("You have selected Easy mode")
    print("Your word is ",len(word), "characters long.")

elif diffLevel == 2:
    while not finished:
        if len(word) < 5 or len(word) > 6:
            word = rw.random_word()
            # print(word)
        else:
            finished = True
    print("You have selected Medium mode")
    print("Your word is ",len(word), "characters long.")

elif diffLevel == 3:
    while not finished:
        if len(word) < 5 or len(word) > 6:
            word = rw.random_word()
            # print(word)
        else:
            finished = True
    print("You have selected Hard mode")
    print("Your word is ",len(word), "characters long.")




def countdown(p,q):
    i=p
    j=q
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):
            print(str(k)+str(i)+":"+str(j), end="\r")
        else:
            print(str(k)+str(i)+":"+str(k)+str(j), end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        print("Goodbye!", end="\r")
        time.sleep(1)
countdown(1,5) #countdown(min,sec)
