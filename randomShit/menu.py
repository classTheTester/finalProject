import pygame

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
WIDTH = 800
HEIGHT = 600
screen_size = (WIDTH, HEIGHT)
darkBlue = (15,91,243)
WHITE = (255,255,255)
PEACH = (243,144,15)
font = pygame.font.SysFont('Arial Black',27)

# Create the screen surface
screen = pygame.display.set_mode(screen_size)

# Game loop
gameLoop = True
while gameLoop:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((48, 221, 255)) #fill 2/3 screen
    topHalf = pygame.draw.rect(screen,PEACH,(0,0,2500,350)) 
    timeButton = pygame.draw.rect(screen,darkBlue,(WIDTH//2+10,HEIGHT//2-30,150,35)) 
    ballButton = pygame.draw.rect(screen,darkBlue,(205,HEIGHT//2-31,150,35))
    gameMessage = font.render('Welcome to RapidType! Please select from an option below!',18,WHITE)
    gameMessageTwo = font.render('RapidType is the best way to improve your typing!',18,WHITE)
    ballMessage = font.render('Balloon Pop',10,WHITE)
    personMessage = font.render('Made by Zach, Edward, Yifan and Braden',18,WHITE)
    timeMessage = font.render('Timed',12,WHITE)
    screen.blit(gameMessage,(100,75))
    screen.blit(gameMessageTwo,(155,185))
    screen.blit(ballMessage,(WIDTH//2-190,HEIGHT//2-24))
    screen.blit(timeMessage,(WIDTH//2+40,HEIGHT//2-23)) 
    screen.blit(personMessage,(200,425))

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
