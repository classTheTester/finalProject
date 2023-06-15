import time
#testing
import pygame
pygame.init()
green = (0, 255, 0)
red = (149, 53, 83)
yellow = (255,255,0)
black = (0, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)


class Words():
    def __init__(self, word, prevWordLen, wordPos):
        self.time = 0
        self.accuracy = 0
        self.word = word
        self.wordLen = len(str(word))
        self.letterList = list(word)
        self.counter = -1
        self.listColour = [black] * self.wordLen
        self.prevWordLen = prevWordLen
        self.wordPos = wordPos
    def backSpace(self):
        self.listColour[self.counter] = black
        if self.counter < 0:
            return True
        else:
            self.counter -= 1

    def checkCorrect(self, letterPressed):
        self.counter += 1
        if self.letterList[self.counter] == letterPressed:
            self.listColour[self.counter] = green
        elif self.letterList[self.counter] != letterPressed:
            self.listColour[self.counter] = red
        if self.counter == self.wordLen-1:
            return True
    def drawWord(self, surface, pointer):
        for i in range(len(self.word)):
            if i == self.counter + 1 and pointer:
                text = font.render(self.letterList[i], True, self.listColour[i], yellow)
            else:
                text = font.render(self.letterList[i], True, self.listColour[i])
            surface.blit(text, (10 +30*i,50*self.wordPos))

#or just use return and append it to the list in the main
    def inputData(self, accList, timeList):
        accList.append(self.accuracy); timeList.append(self.timeList)        
