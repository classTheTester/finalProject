# import pygame module in this program
white = (255, 255, 255)
green = (0, 255, 0)
red = (149, 53, 83)
import pygame
letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letterDict = {}
listOfShit = [green] * 13
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
words = ['thewiseman', 'hahahahaha']
 
# create a rectangular object for the
# text surface object
 
# set the center of the rectangular object.
 
# infinite loop

k = 0
counter = 0
while True:
    yVal = 200
    display_surface.fill(white)
    for j in words:
        for i in range(len(j)):
            text = font.render(j[i], True, listOfShit[i])
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

 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            keyMapping = list(keys)
            letters = list(words[counter])
            letter = letters[k]
            print("hahahahaha", letter)
            if keys[pygame.K_SPACE]:
                print('aaha')
                counter += 1
            if 1 in keyMapping:
                print(letterDict.get(str(keyMapping.index(1)+1)))
                if letterDict.get(str(keyMapping.index(1)+1)) == letter:
                    print('fuck yeah')
                else:
                    listOfShit[k] = red
                k += 1
        # Draws the surface object to the screen.
        pygame.display.update()
