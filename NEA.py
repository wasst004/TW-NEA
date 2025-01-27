#importing
import sys
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
import time
#linking files
from classes import *
import functions
from level import level
from menu import menu

#setup
pygame.init()
screen = pygame.display.set_mode((1280, 680))
clock = pygame.time.Clock()
framerate = 60
#setting variables
shotCount = 0
pars = [2, 4]
currentLevel = 1
scoreMessages = ["Par", "Bogey", "Double Bogey", "Triple Bogey", "Eagle", "Birdie"]
finished = True
currentLevel = 0
time = 0
totalScore = 0
scores = []
shots = []


#initialising instances of ball and wall classes
ball = Ball(screen, 630, 550)
walls = [
    Wall(screen, (530,90), (540,90), (540,590), (530,590), "west"),
    Wall(screen, (710,90), (720,90), (720,590), (710,590), "east"),
    Wall(screen, (530,80), (720,80), (720,90), (530,90), "north"),
    Wall(screen, (530,590), (720,590), (720,600), (530,600), "south")
        ]
#walls for level two
walls2 = [
    Wall(screen, (440,100), (840,100), (840,110), (440,110), "north"),
    Wall(screen, (440,110), (450,110), (450,250), (440,250), "west"),
    Wall(screen, (450,240), (700,240), (700,250), (450,250), "south"),
    Wall(screen, (690,250), (700,250), (700,580), (690,580), "west"),
    Wall(screen, (690,570), (840,570), (840,580), (690,580), "south"),
    Wall(screen, (830,110), (840,110), (840,570), (830,570), "east")
  ]

hole = Hole(screen, 625, 130)
buttons = [
    Button(screen, 282.5, 535, "#40A15D", 140, 100, "circle"),
    Button(screen, 922.5, 480, "#40A15D", 120, 100, "square"),
    Button(screen, 560, 475, "#40A15D", 160, 120, "square")
    ]
settings = Button(screen, 25, 25, "#40A15D", 100, 100, "square")

#main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
    #drawing screen
    screen.fill('#55CE79')
            
    #manual controls
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        ball.set_pos(0,-10)
    elif keys[K_DOWN]:
        ball.set_pos(0,10)
    elif keys[K_LEFT]:
        ball.set_pos(-10,0)
    elif keys[K_RIGHT]:
        ball.set_pos(10,0)
                

    if currentLevel == 0:
        done = menu(screen, buttons)
        if done:
            currentLevel += 1
      
    elif currentLevel == 1:
      
        if finished:
            #running code for level 1
            finished, shotCount = level(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages, (605,530,50,40), settings, scores, shots)            
              
        else:
            #ending screen
            functions.display_text(screen, "YOU WON LEVEL 1", 600, 400, 80)
            score, shotDisplay = functions.calculate_Score(shotCount, scoreMessages, pars, currentLevel)
            functions.display_text(screen, shotDisplay, 600, 450, 70)
            time += 1
            #waits 3 seconds
            if time == 180:
                #sets all values to ones for level 2
                scores.append(score)
                shots.append(shotCount)
                currentLevel += 1
                totalScore += score
                finished = True
                shotCount = 0
                ball.set_pos(765, 530)
                hole.set_pos(470,175)
                ball.reset_speed()
            
      
    elif currentLevel == 2:
        
        if finished:
            #running code for level 2
            finished, shotCount = level(screen, ball, walls2, hole, shotCount, currentLevel, pars, scoreMessages, (740,510,50,40), settings, scores, shots)            
                
        else:
            #ending screen
            functions.display_text(screen, "YOU WON LEVEL 2", 600, 400, 80)
            score, shotDisplay = functions.calculate_Score(shotCount, scoreMessages, pars, currentLevel)
            functions.display_text(screen, shotDisplay, 600, 450, 70)
            #currentLevel += 1
            #finished = True
        
    
    pygame.display.flip()
    clock.tick(framerate)