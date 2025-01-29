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
pars = [2, 3, 4, 5]
currentLevel = 1
scoreMessages = ["Par", "Bogey", "Double Bogey", "Triple Bogey", "Eagle", "Birdie"]
finished = True
currentLevel = 0
time = 0
totalScore = 0
scores = []
shots = []
timer = 0


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
#walls for level three
walls3 = [
    Wall(screen, (430, 100), (850, 100), (850, 110), (430, 110), "north"),
    Wall(screen, (430, 110), (440, 110), (440,400), (430, 400), "west"),
    Wall(screen, (440, 390), (580, 390), (580, 400), (440, 400), "south"),
    Wall(screen, (570, 250), (580, 250), (580, 390), (570, 390), "east"),
    Wall(screen, (570, 240), (710, 240), (710, 250), (570, 250), "south"),
    Wall(screen, (700, 250), (710, 250), (710, 580), (700, 580), "west"),
    Wall(screen, (710, 570), (850, 570), (850, 580), (710, 580), "south"),
    Wall(screen, (840, 110), (850, 110), (850, 570), (840, 570), "east"),
  ]
freeWall = Directional(screen, (710, 300), (770, 300), (770, 310), (710, 310), "n/a")

walls4 = [
  Wall(screen, (320, 50), (960, 50), (960, 60), (320, 60), "north"),
  Wall(screen, (320, 60), (330, 60), (330, 620), (320, 620), "west"),
  Wall(screen, (320, 620), (960, 620), (960, 630), (320, 630), "south"),
  Wall(screen, (950, 60), (960, 60), (960, 620), (950, 620), "east"),
  Wall(screen, (450, 180), (575, 180), (575, 190), (450, 190), "south"),
  Wall(screen, (450, 190), (460, 190), (460, 500), (450, 500), "east"),
  Wall(screen, (460, 490), (830, 490), (830, 500), (460, 500), "north"),
  Wall(screen, (820, 180), (830, 180), (830, 490), (820, 490), "west"),
  Wall(screen, (705, 180), (820, 180), (820, 190), (705, 190), "south"),
  Wall(screen, (705, 190), (715, 190), (715, 220), (705, 220), "east"),
  Wall(screen, (715, 210), (800, 210), (800, 220), (715, 220), "north"),
  Wall(screen, (790, 220), (800, 220), (800, 470), (790, 470), "east"),
  Wall(screen, (480, 460), (790, 460), (790, 470), (480, 470), "south"),
  Wall(screen, (480, 210), (490, 210), (490, 460), (480, 460), "west"),
  Wall(screen, (490, 210), (575, 210), (575, 220), (490, 220), "north"),
  Wall(screen, (565, 190), (575, 190), (575, 210), (565, 210), "west"),
  ]
freeWalls = [
    Directional(screen, (563, 263), (715, 263), (715, 274), (563, 274), "n/a"),
    Directional(screen, (490,325), (590, 325), (590, 336), (490, 336), "n/a"),
    Directional(screen, (690, 325), (790, 325), (790, 336), (690, 336), "n/a"),
    Directional(screen, (565, 387), (715, 387), (715, 398), (565, 398), "n/a")
 ] 
timers = [0, 0, 0, 0]
roughGrass = [
    Terrain(screen, 710, 190, 60, 110, "rough"),
    Terrain(screen, 440, 250, 130, 60, "rough"),
    Terrain(screen, 570, 110, 140, 50, "rough"),
    Terrain(screen, 570, 190, 140, 50, "rough"),
]
terrains = [
    Terrain(screen, 330, 180, 40, 320, "rough"),
    Terrain(screen, 370, 180, 40, 320, "ice"),
    Terrain(screen, 410, 180, 40, 320, "rough"),
    Terrain(screen, 830, 180, 40, 320, "rough"),
    Terrain(screen, 870, 180, 40, 320, "ice"),
    Terrain(screen, 910, 180, 40, 320, "rough"),
    Terrain(screen, 490, 220, 300, 240, "ice")
]

#initialising instances of hole and button classes
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
            finished, shotCount = level(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages, (605,530,50,40), settings, scores, shots, [])            

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
                time = 0
                ball.set_pos(765, 530)
                hole.set_pos(470,175)
                ball.reset_speed()
            
      
    elif currentLevel == 2:
        
        if finished:
            #running code for level 2
            finished, shotCount = level(screen, ball, walls2, hole, shotCount, currentLevel, pars, scoreMessages, (740,510,50,40), settings, scores, shots, [])            
            
        else:
            #ending screen
            functions.display_text(screen, "YOU WON LEVEL 2", 600, 400, 80)
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
                time = 0
                ball.set_pos(775, 530)
                hole.set_pos(505,365)
                ball.reset_speed()
    
    elif currentLevel == 3:
      
        if finished:
            #running code for level 3
            finished, shotCount = level(screen, ball, walls3, hole, shotCount, currentLevel, pars, scoreMessages, (750,510,50,40), settings, scores, shots, roughGrass)            
            freeWall.draw()
            timer = freeWall.collision(ball, timer)
        else:
            #ending screen
            functions.display_text(screen, "YOU WON LEVEL 3", 600, 400, 80)
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
                time = 0
                ball.set_pos(640, 590)
                hole.set_pos(640,430)
                ball.reset_speed()



    elif currentLevel == 4:
      
        if finished:
            #running code for level 4
            finished, shotCount = level(screen, ball, walls4, hole, shotCount, currentLevel, pars, scoreMessages, (615,570,50,40), settings, scores, shots, terrains)            
            
            for wall in freeWalls:
                wall.draw()
                timers[freeWalls.index(wall)] = wall.collision(ball, timers[freeWalls.index(wall)])
        else:
            #ending screen
            functions.display_text(screen, "YOU WON LEVEL 4", 600, 400, 80)
            score, shotDisplay = functions.calculate_Score(shotCount, scoreMessages, pars, currentLevel)
            functions.display_text(screen, shotDisplay, 600, 450, 70)
      
        
    
    pygame.display.flip()
    clock.tick(framerate)