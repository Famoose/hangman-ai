from loadData import getWord, keys


class GameController:

    def __init__(self, tries=6):
        self.usedKeys = []
        self.word = getWord()
        self.wordGuessed = False
        self.gameover = False
        self.tries = tries

    def wordIsGuessed(self):
        return set(self.word).issubset(set(self.usedKeys))

    def showWord(self):
        hint = []
        for letter in list(self.word):
            if len(self.usedKeys) == 0:
                hint.append('_')
            elif letter in self.usedKeys:
                hint.append(letter)
            else:
                hint.append('_')
        return hint

    def getUsableKeys(self):
        return list(set(keys).difference(set(self.usedKeys)))

    def guesKey(self, k):
        if k in self.usedKeys:
            print(k + 'is already used')
            return
        if k not in keys:
            print(k + 'is not in keys')
            return

        self.usedKeys.append(k)
        if k in self.word:
            if self.wordIsGuessed():
                self.wordGuessed = True
                return True
            return True
        else:
            self.tries -= 1
            if self.tries == 0:
                self.gameover = True
            return False
