import pygame
from math import sqrt  
from random import randint 

from random import randrange

pygame.init()

HEIGHT = 600
WIDTH = 800
surface = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)

font = pygame.font.SysFont('Ariel Black', 40)

ufo_image = pygame.image.load('result.png')

background_image = pygame.image.load('space.jpg')

ufo_image = ufo_image.subsurface(ufo_image.get_bounding_rect())  
ufo_image = pygame.transform.scale(ufo_image, (ufo_image.get_width() // 8, ufo_image.get_height() // 8)) 
surface.blit(background_image, (0, 0))

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))  
surface.blit(background_image, (0, 0))
pygame.mixer.music.load( 'music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(loops=-1)

sound = pygame.mixer.Sound('sound.wav')
sound.set_volume(0.5)
class Balloon():
    def __init__(self, speed, number):
        self.balloonX = randrange(60, WIDTH-60,50)
        self.balloonY = randrange(number*HEIGHT / 5, HEIGHT * 2 / 5,50)
        self.balloonR  = randint(30, 40)
        self.balloonSPEED = speed
        #self.balloonCLR = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.balloonVisible = True
        self.value = randint(0, 25)
        self.letter = chr(self.value + 65)
    
  
    
    def draw(self):
        if self.balloonVisible:
            surface.blit( ufo_image, (self.balloonX, self.balloonY))
            #pygame.draw.circle(surface, self.balloonCLR, (self.balloonX, self.balloonY), self.balloonR, 0)
            text = font.render(self.letter, True, WHITE)
            #text_rect = text.get_rect(center=(self.balloonX, self.balloonY))
            text_rect = text.get_rect(center=(self.balloonX + ufo_image.get_width() / 2, self.balloonY + ufo_image.get_height() / 2))

            surface.blit(text, text_rect)

   
    def moveDown(self):
        if self.balloonVisible:
            self.balloonY += self.balloonSPEED
            if self.balloonY > HEIGHT + 100 :
                self.balloonVisible = False
                return True
        return False

    
   # def __eq__(self,other):
        #  if self.letter==other.letter and self.balloonCLR !=other.balloonCLR:
           # return True
          #return False
       
    def pop(self, key, score ):
          if self.balloonVisible and key == self.letter and self.balloonY>0:
              self.balloonVisible = False
              #self.balloonY = -6*600
              return score + 1
          return score
  

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def endScreen():
    surface.fill(WHITE)
    text = font.render('Game Over! Your score is '+str(score) ,1, (0,0,0))
    surface.blit(text,(300, HEIGHT//2 ))

    pygame.display.update()


def showScore():
    text1 = font.render('Popped:' + str(score), 1, (0,0,0),WHITE)
    surface.blit(text1, (0,0))
    text2 = font.render('Flown away:' + str(fly), 1, (0,0,0),WHITE)
    surface.blit(text2, (WIDTH-200, 0))



          
                

def redraw(balloonList):
    surface.blit(background_image, (0, 0))
    showScore()
    
    for i in balloonList: 
        i.draw()
    
    pygame.draw.line(surface, (0,0,0), (0, HEIGHT * 1 / 4), (WIDTH, HEIGHT * 1 / 4), 2)
    pygame.display.update()


def selectDifficulty():
    surface.fill(WHITE)
    text = font.render('Select Difficulty:', 1, (0,0,0))
    surface.blit(text,(300, HEIGHT//2 - 50 ))
    text1 = font.render('1. Easy', 1, (0,0,0))
    surface.blit(text1,(350, HEIGHT//2 ))
    text2 = font.render('2. Medium', 1, (0,0,0))
    surface.blit(text2,(350, HEIGHT//2 + 50 ))
    text3 = font.render('3. Hard', 1, (0,0,0))
    surface.blit(text3,(350, HEIGHT//2 + 100 ))
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == '1':
                  
                    return 1
                elif event.unicode == '2':
                    return 2
                elif event.unicode == '3':
                    return 3


difficulty = selectDifficulty()
if difficulty == 1:
    speed = 1
    number = -20
elif difficulty == 2:
    speed = 2
    number = -6
else:
    speed = 3
    number = -6
numberOfBalloons = randint(50,70)
balloonList=[]
for i in range(numberOfBalloons):
    balloon=Balloon(speed,number)
    balloonList.append(balloon)


score, fly = 0, 0
exitFlag = False


while not exitFlag:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exitFlag = True  
        elif event.type == pygame.KEYDOWN:
            
            key = pygame.key.name(event.key).upper()

            balloons_to_pop = []
            for balloon in balloonList:
                if balloon.letter == key and balloon.balloonVisible:
                    balloons_to_pop.append(balloon)
            
            if balloons_to_pop:
                sound.play()
                balloon_to_pop = balloons_to_pop[0]
                for balloon in balloons_to_pop:
                    if balloon.balloonY > balloon_to_pop.balloonY:
                        balloon_to_pop = balloon
            
                score = balloon_to_pop.pop(key, score)

           
                    
                
                    
    
    for i in balloonList:
        fly += i.moveDown()
        
        
    
    if fly + score == numberOfBalloons:
        exitFlag = True

    redraw(balloonList)
    pygame.time.delay(60)
endScreen()
pygame.time.delay(2000)
   


pygame.quit()
