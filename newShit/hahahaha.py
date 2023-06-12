# import pygame module in this program
white = (255, 255, 255)
green = (0, 255, 0)
red = (149, 53, 83)
yellow = (255,255,0)
totalLetters = 0
mistakes = 0
import pygame
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letterDict = {}
for i in range(len(letterList)):
    letterDict[str(i + 5)] =letterList[i]


print(letterDict)
# activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# define the RGB value for white,
#  green, blue colour .

 
# assigning values to X and Y variable
X = 400
Y = 400
 
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))
 
# set the pygame window name
pygame.display.set_caption('Show Text')
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
<<<<<<< HEAD
words = ['thewiseman', 'hahahahaha', 'bitchassss', 'fuckoff', 'bitch', 'what', 'fjfjfjfjfjfjfj']
=======
words = ['thewiseman', 'hahahahaha', 'bitchass', 'fuckoff', 'bitch', 'what']
>>>>>>> parent of 39a6e4c (Update hahahaha.py)
 
# create a rectangular object for the
# text surface object
 
# set the center of the rectangular object.
 
# infinite loop
listOfShit = []
for i in words:
    listOfShit.append([green]* len(i))
k = 0
counter = 0
while True:
    yVal = 20
    display_surface.fill(white)
    for j in words:
        for i in range(len(j)):
            if i == k and counter == words.index(j):
                text = font.render(j[i], True, listOfShit[words.index(j)][i], yellow)
            else:
                text = font.render(j[i], True, listOfShit[words.index(j)][i])
            display_surface.blit(text, (10 +30*i,yVal))
        yVal += 50
 
    # completely fill the surface object
    # with white color

 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
            print((1-(mistakes/totalLetters))*100)

 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            letters = list(words[counter])
            letter = letters[k]
            if keys[pygame.K_SPACE]:
                counter += 1
                k = -1
<<<<<<< HEAD
#<<<<<<< Updated upstream
            if pygame.key.name(event.key) == letter:
                print('fuck yeah')
                listOfShit[counter][k] = green
                if k < len(letters)-1:
                    totalLetters += 1
                    k += 1
            elif pygame.key.name(event.key) != letter and pygame.key.name(event.key) != "backspace":
                listOfShit[counter][k] = red
                mistakes += 1

#=======        
            elif keys[pygame.K_BACKSPACE]:
                if k > 0:
                    listOfShit[counter][k] = black
                    k -= 2
                    print('yeah')
                elif k== 0 and counter == 0:
                    pass
=======
            elif 1 in keyMapping:
                print(letterDict.get(str(keyMapping.index(1)+1)))
                if letterDict.get(str(keyMapping.index(1)+1)) == letter:
                    print('fuck yeah')
>>>>>>> parent of 39a6e4c (Update hahahaha.py)
                else:
                    counter -= 1
                    k = len(words[counter])-2
                    print(words[counter])
                    listOfShit[counter][k] = black
                letter = letters[k]

#>>>>>>> Stashed changes
        # Draws the surface object to the screen.
        pygame.display.update()
