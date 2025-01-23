#importing
import sys
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT
import time
#linking files
from classes import *
import functions
from levelOne import level_1
from menu import menu

#setup
pygame.init()
screen = pygame.display.set_mode((1280, 680))
clock = pygame.time.Clock()
framerate = 60
#setting variables
shotCount = 0
pars = [2]
currentLevel = 1
scoreMessages = ["Par", "Bogey", "Double Bogey", "Triple Bogey", "Eagle", "Birdie"]
finished = True
currentLevel = 0


#initialising instances of ball and wall classes
ball = Ball(screen, 630, 550)
walls = [
    Wall(screen, (530,90), (540,90), (540,590), (530,590), "west"),
    Wall(screen, (710,90), (720,90), (720,590), (710,590), "east"),
    Wall(screen, (530,80), (720,80), (720,90), (530,90), "north"),
    Wall(screen, (530,590), (720,590), (720,600), (530,600), "south")
        ]
hole = Hole(screen, 630, 130)

buttons = [
    Button(screen, 282.5, 535, "#40A15D", 140, 100, "circle"),
    Button(screen, 922.5, 480, "#40A15D", 120, 100, "square"),
    Button(screen, 560, 475, "#40A15D", 160, 120, "square")
    ]

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
      currentLevel += menu(screen, buttons)
      
    elif currentLevel == 1:
      
      if finished:
          #running code for level 1
          finished, shotCount = level_1(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages)            
              
      else:
          #ending screen
          functions.display_text(screen, "YOU WON LEVEL 1", 600, 400, 80)
          shotDisplay = functions.calculate_Score(shotCount, scoreMessages, pars, currentLevel)
          functions.display_text(screen, shotDisplay, 600, 450, 70)
          #time.sleep(3)
          #currentLevel += 1

    pygame.display.flip()
    clock.tick(framerate)
