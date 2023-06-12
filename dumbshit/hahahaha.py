import time


class Words(word):
    def __init__(self, time, accuracy):
        self.time = 0
        self.accuracy = 0
        self.wordLen = len(str(word))
        self.letterList = [i for i in str(word)]


    def determineTime():
        timing1 = time.time()
        