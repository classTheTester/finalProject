#########################################
# Programmer: Edward Weisberg
# Date: 9/11/2021
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################

import time
import pygame
pygame.init()
import time
from math import sqrt                   # only sqrt function is needed from the math module
from random import randint, choice              # only randint function is needed from the random module
asteroid = pygame.image.load("images/asteroidPic.png")
asteroid = pygame.transform.scale(asteroid, (100, 100))
spaceShip = pygame.image.load("images/spaceShip.png")
spaceShip = pygame.transform.scale(spaceShip, (50,50))
laser = pygame.image.load("images/laser.png")
nitro = pygame.image.load("images/nitro.png")
nitro = pygame.transform.scale(nitro, (50,50))
nitroPos = [0, 300]
getNitro = False
laser = pygame.transform.scale(laser, (50,50))
laserPos = [0, 150]
shipSpeed = 5
nitroValue = 255
shipList = [350, 550]
level = 1
getLaser = False
gameTime = 50
asteroidDist = []
asteroidClass = []
shipRect = spaceShip.get_rect()
shipW = shipRect.width
shipH = shipRect.height
shipX = shipList[0]
shipY = shipList[1]
print(shipW)
laserEnergy = 10
HEIGHT = 600
WIDTH  = 800
surface=pygame.display.set_mode((WIDTH,HEIGHT))
background = pygame.image.load("images/space.jpg")
background = background.convert_alpha()
background = pygame.transform.scale(background,(WIDTH,HEIGHT))

###################Sound#########################
nitroSound = pygame.mixer.Sound("sound/nitro.wav")
nitroSound.set_volume(0.5)

explosionSound = pygame.mixer.Sound("sound/explosion.wav")
explosionSound.set_volume(0.5)

themeMusic = pygame.mixer.music.load("sound/ramjam.mp3") #Change to techno.mp3
pygame.mixer.music.play(-1)


font = pygame.font.SysFont("Ariel Black",60) # create a variable font
font2 = pygame.font.SysFont("Ariel Black",110) # create a variable font

WHITE = (  0,  0,  0)                   # used colours
BLACK= (255, 255, 255)
outline = 0                               # thickness of the shapes' outlin
counter = 0                              #pop counter                              #miis counter
timer = 0

start = True

#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#


def startScreen():
    surface.blit(background, (0,0))
    startText = font2.render("Space Racers!", 0, BLACK)
    startText2 = font.render("Press Space to start!", 0 , BLACK)
    surface.blit(startText, (150, 250))
    surface.blit(startText2, (190, 350))
    surface.blit(spaceShip, shipList)
    pygame.display.update()


while start:
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exitFlag = False
            start = False
    # act upon mouse events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
         exitFlag = True
         start = False
    startScreen()
        
    
def redraw():
    surface.blit(background, (0,0))
    nitroIcon = pygame.transform.scale(nitro, (30,30))
    laserIcon = pygame.transform.scale(laser, (30,30))
    text1 = font.render("Level: ", 1, BLACK)
    text2 = font.render(str(level), 1, BLACK)
    text3 = font.render("Timer:", 1, BLACK)
    text4 = font.render(str(timer//20), 1, BLACK)
    surface.blit(spaceShip, (350, 550))
    surface.blit(text1,(0,0))
    surface.blit(text2,(125,0))
    surface.blit(text3,(600,0))
    surface.blit(text4,(735,0))
    for i in range(len(balloonVisible)):
        if balloonVisible[i] == True:
            #pygame.draw.rect(surface, BLACK, (asteroidClass[i].asteroidX,asteroidClass[i].asteroidY,asteroidClass[i].asteroidW,asteroidClass[i].asteroidH),1)
            surface.blit(balloonImg[i], (balloonX[i], balloonY[i]))
                # display must be updated, in order
                                        # to show the drawings
    if not getNitro:
        surface.blit(nitro, nitroPos)
    if getNitro:
        pygame.draw.rect(surface, BLACK, pygame.Rect(70, 50, nitroValue, 10),  0)
        surface.blit(nitroIcon,(35, 38))
    if not getLaser:
        surface.blit(laser, laserPos)
    if getLaser:
        laserText = font.render("Energy: " + str(laserEnergy), 0, BLACK)
        surface.blit(laserText, (575, 50))
        surface.blit(laser, (laserX - 12.5, laserY - 25))
    pygame.display.update()


    #endGame
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exitFlag = False                       #
balloonR = []                      # create lists of 20 items each
balloonX = []                      # for balloons' properties
balloonY = []                       #
balloonSPEED = []                   #
balloonImg = []
balloonVisible = []
lose = False

def makeAsteroids(amount):
    for i in range(amount):
        balloonX.append(randint(0, WIDTH))     # initialize the coordinates and the size of the balloons
        balloonY.append(randint(0, 200))
        balloonR.append(randint(50, 65))
        balloonSPEED.append(randint(1,5))
        balloonVisible.append(True)
        picture = asteroid
        picture = pygame.transform.scale(picture,(balloonR[i], balloonR[i] + balloonR[i]))
        balloonImg.append(picture)
        asteroidRect = asteroid.get_rect()
        asteroidW = balloonR[i]
        asteroidH = balloonR[i]
        asteroidX = balloonX[i] - 12.5
        asteroidY = balloonY[i] + 37.5
        asteroidClass.append(asteroidRect)


makeAsteroids(20)
def loseLoop():
    global balloonVisible, timer, level, gameTime, getLaser, getNitro, laserEnergy, nitroValue
    while True:
        explosion = pygame.image.load("images/explosion.png")
        explosion = pygame.transform.scale(explosion, (150,150))
        text = font2.render("GAME OVER", 1, BLACK)
        finalText2 = font.render("Press enter to play again", 1, BLACK)
        surface.blit(explosion, (shipList[0] - 40, shipList[1] - 37.5))
        surface.blit(finalText2,(125,350))
        surface.blit(text, (150, 250))
        pygame.display.update()
        for event in pygame.event.get():    # check for any events
            if event.type == pygame.QUIT:   # If user clicked close
                exitFlag = True
                break
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            level = 1
            gameTime = 50
            balloonVisible = [False] * len(balloonVisible)
            makeAsteroids(20)
            timer = 0
            getNitro = False
            getLaser = False
            laserEnergy = 10
            nitroValue = 255
            break
    
    
while not exitFlag:
    shipX = shipList[0]
    shipY = shipList[1]
    if balloonVisible.count(False) == len(balloonVisible):
        makeAsteroids(5)
    (cursorX,cursorY)=pygame.mouse.get_pos()
    laserX,laserY = cursorX, cursorY
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exitFlag = True            # Flag that we are done so we exit this loop
# act upon mouse events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        shipList[1] -= shipSpeed
    if keys[pygame.K_DOWN]:
        shipList[1] += shipSpeed
    if keys[pygame.K_LEFT]:
        shipList[0] -= shipSpeed
    if keys[pygame.K_RIGHT]:
        shipList[0] += shipSpeed
    if keys[pygame.K_SPACE] and getNitro:
        nitroSound.play()
        nitroValue -= 8
        shipSpeed = 45
        if nitroValue <= 0:
            nitroValue = 255
            getNitro = False
    else:
        shipSpeed = 5
    if len(balloonVisible) == balloonVisible.count(False):
        progression = font2.render("Level: " + str(level), 1, BLACK)
        surface.blit(progression, (300, 250))
        pygame.display.update()
        time.sleep(1)
        shipList = [350, 550]
        balloonVisible = [False] * len(balloonVisible)        #makeAsteroids(20)
        gameTime -= 15
    if shipList[1] >= 550:
        shipList[1] = 550
    if shipList[0] >= 750:
        shipList[0] = 750
    if shipList[0] <= 0:
        shipList[0] = 0
 
    for i in range(len(balloonVisible)):
        if balloonVisible[i] == True:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if distance(cursorX, cursorY, balloonX[i]+balloonR[i]//2, balloonY[i]+balloonR[i]//2)< balloonR[i]//2 and getLaser:
                    if laserEnergy == 0:
                        laserEnergy = 10
                        getLaser = False
                    else:
                        print("mouse click")
                        balloonVisible[i] = False
                        laserEnergy -= 1
            if distance(shipList[0], shipList[1], balloonX[i], balloonY[i]) < (balloonR[i]/1.25):
                explosionSound.play()
                lose = True
                loseLoop()
                
    if distance(shipList[0], shipList[1], nitroPos[0], nitroPos[1]) < (50/1.25):
        getNitro = True
        nitroSound.play()
    if distance(shipList[0], shipList[1], laserPos[0], laserPos[1]) < (50/1.25):
        getLaser = True

        
        
  
# move the balloons
    for i in range(len(balloonVisible)):
        balloonY[i] += balloonSPEED[i]
        if balloonVisible[i] == True:
            if balloonX[i]+balloonR[i] < 0:
                balloonVisible[i]=False
                
        
# update the screen
    pygame.time.delay(gameTime)
    timer += 1
    redraw()
pygame.quit()                           # always quit pygame when done!


