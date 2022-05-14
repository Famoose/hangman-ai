# Python program to read
# json file


import json

# Opening JSON file
import random
keys = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

f = open('./data/words.json')

# returns JSON object as
# a dictionary
words = list(json.load(f))


def filterForUsableWords(word):
    word = word.lower()
    isUsable = True
    for letter in word:
        if letter not in keys:
            isUsable = False
    return isUsable


usableWords = list(filter(filterForUsableWords, words))[:30000]
testWords = list(filter(filterForUsableWords, words))[30000:]
print(len(usableWords))
print(len(testWords))

# Closing file
f.close()

def getWord():
    wordPosition = random.randint(0, len(testWords) - 1)
    return testWords[wordPosition].lower()
