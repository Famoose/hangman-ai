import random

from gameController import GameController

correct = 0
wrong = 0
wordGuessed = 0
notGuessed = 0
for i in range(10000):
    gc = GameController()
    while not (gc.wordGuessed or gc.gameover):
        usableKeys = gc.getUsableKeys()
        wordBefore = gc.showWord()
        i = random.randint(0, len(usableKeys) - 1)
        success = gc.guesKey(usableKeys[i])
        if success:
            correct += 1
        else:
            wrong += 1
            #print('wrong')
    if(gc.wordGuessed):
        wordGuessed += 1
        #print('word guessed')
    else:
        notGuessed += 1
        #print('not guessed')

print(wordGuessed)
print(notGuessed)