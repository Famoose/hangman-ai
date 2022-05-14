from __future__ import absolute_import, division, print_function

import json
import random

from gameController import GameController


logTable = []
trues = 0
for i in range(0, 1000000):
    if i%10 == 0:
        print(i)
    gc = GameController()
    while not gc.wordGuessed:
        usableKeys = gc.getUsableKeys()
        nextKey = random.randint(0, len(usableKeys) - 1)
        wordBefore = gc.showWord()
        success = gc.guesKey(usableKeys[nextKey])
        if success:
            trues += 1
            logTable.append([usableKeys[nextKey], wordBefore, usableKeys])

f = open("./data/playData.json", "w")
f.write(json.dumps(logTable))
f.close()