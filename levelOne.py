import pygame
import functions


def level_1(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages):
    level1 = True

    #displays elements of level
    functions.draw_elements(screen, ball, walls, hole)
    functions.draw_board(screen, currentLevel, shotCount, pars)
            
    #calling ball methods in main code
    shotCount = ball.shoot(shotCount)
    ball.aim()
    ball.move()
    ball.collision(walls)
    level1 = hole.collision(ball.get_pos(), level1)

    #returning useful values to main file
    return level1, shotCount