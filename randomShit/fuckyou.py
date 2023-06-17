# import pygame module in this program
from testingClassesFuck import *
white = (255, 255, 255)
black = (0,0,0)
blue = (0, 0, 255)
totalLetters = 0
mistakes = 0
wrongLetterList = []
accList = []
timeList = []
font = pygame.font.Font('freesansbold.ttf', 32)
import pygame
import json
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .
 
# assigning values to X and Y variable
X = 800
Y = 600
keyboardImg = pygame.image.load("keyboard.png")
#keyboardImg = pygame.transform.scale(keyboardImg, (200, 150))
timeList = []
accuracyList = []
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font

 
# create a text surface object,
# on which text is drawn on it.

words = [ 'yes', 'no','fool', 'please', 'testing', 'foolish', 'pain', 'suffering', 'howwhy', 'foolish', 'damning', 'damningfool']
listClass = []
wordsCounter = 0
endList = False
gameLoop = True
scoreLoop = False
def createClasses(words):
    xSpace = 0
    ySpace = 50
    for i in range(len(words)):
        wordUsed = Words(words[i],xSpace, ySpace)
        listClass.append(wordUsed)
        if xSpace + 30*len(words[i])+40 < 600:
            xSpace += 30*len(words[i]) + 50
        else:
            ySpace += 50
            xSpace = 0
        print(xSpace, ySpace)
        
createClasses(words)
# create a rectangular object for the
# text surface object
 
# set the center of the rectangular object.
 
# infinite loop
userList = []
nameSaved = False
def scoreDraw():
    display_surface.fill(white)
    text = font.render("Please enter a username (max 15 letters)", True, black)
    display_surface.blit(text, (50, 140))
    if len(userList) > 0:
        text = font.render(''.join(userList), True, black)
        display_surface.blit(text, (50,185))
        if nameSaved:
            text = font.render("Username is saved!", True, blue)
            display_surface.blit(text, (50, 230))
        
def redraw():
    yVal = 20
    display_surface.fill(white)
    display_surface.blit(keyboardImg, (0, 300))
    if len(listClass) - 1 > 0:
        listClass[wordsCounter].indicateKeyboard(display_surface)
    #text = font.render(str(sum(timeList)), True, black)
    #display_surface.blit(text, (30, 20)) 
    for i in range(len(listClass)):
        if i == wordsCounter:
            listClass[i].drawWord(display_surface, True)
        else:
            listClass[i].drawWord(display_surface, False)

while scoreLoop:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and len(userList) > 0:
                nameSaved = True
                readInfo = open("scores.txt", "r")
                readDict = json.load(readInfo)
                readDict[''.join(userList)] = (0,0)
                readInfo.close()
                writingInfo = open("scores.txt", "w")
                dumpingInfo = json.dumps(readDict)
                writingInfo.write(dumpingInfo)
                writingInfo.close()
            elif keys[pygame.K_BACKSPACE]:
                if len(userList) > 0: 
                    userList.pop()
            else:
                if len(userList) <= 15:
                    userList.append(pygame.key.name(event.key))
    scoreDraw()

listClass[0].initiateTime()
while gameLoop:
    redraw()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if endList:
                    endList = False
                    listClass[wordsCounter].inputData(timeList, accuracyList, wrongLetterList)
                    print("accc", accuracyList, "timmm", timeList, "wrong", wrongLetterList)
                    wordsCounter += 1
                    if wordsCounter == len(words):
                        totalTime = sum(timeList)
                        #if the user presses space, the timer doesn't start so the score would always be zero")
                        print("your words per minute is", round((60/totalTime)*len(words)))
                        print("you accuracy is", sum(accuracyList)//len(words), "%")
                        words = [a for a in wrongLetterList if a != ""]
                        if len(words) == 0:
                            print("timeList", timeList, "accuracyList", accuracyList, "wrongLetters", wrongLetterList)
                            print(totalTime)
                            gameLoop = False
                        else:
                            wordsCounter = 0
                            wrongLetterList.clear()
                            listClass.clear()
                            createClasses(words)
                    else:
                         print('scmool')
                         listClass[wordsCounter].initiateTime()
            elif keys[pygame.K_BACKSPACE]:
                if listClass[wordsCounter].backSpace() and wordsCounter > 0:
                    wordsCounter -= 1


            elif listClass[wordsCounter].checkCorrect(pygame.key.name(event.key)):
                if wordsCounter < len(words)-1:
                    listClass[wordsCounter+1].initiateTime()
                print("dope fucking shit")
                endList = True
                #     totalTime = sum(timeList)
                #     #if the user presses space, the timer doesn't start so the score would always be zero")
                #     print("your words per minute is", round((60/totalTime)*len(words)))
                #     print("you accuracy is", sum(accuracyList)//len(words), "%")
                #     words = [a for a in wrongLetterList if a != ""]
                #     if len(words) == 0:
                #         print("timeList", timeList, "accuracyList", accuracyList, "wrongLetters", wrongLetterList)
                #         print(totalTime)
                #         gameLoop = False
                #     else:
                #         wordsCounter = 0
                #         wrongLetterList.clear()
                #         listClass.clear()
                #         createClasses(words)

                    


