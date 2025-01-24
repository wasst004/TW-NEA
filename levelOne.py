import pygame
import functions


def level(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages, rect):
    finished = True

    #displays elements of level
    functions.draw_elements(screen, ball, walls, hole, rect)
    functions.draw_board(screen, currentLevel, shotCount, pars)
            
    #calling ball methods in main code
    shotCount = ball.shoot(shotCount)
    ball.aim()
    ball.move()
    ball.collision(walls)
    finished = hole.collision(ball.get_pos())

    #returning useful values to main file
    return finished, shotCount
