import pygame
import functions


def level(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages, rect, settings, scores, shots):
    finished = True

    #displays elements of level
    functions.draw_elements(screen, ball, walls, hole, rect)
    pause = functions.draw_board(screen, currentLevel, shotCount, pars, settings)
    
    if pause:
        screen.fill('#55CE79')
        while pause:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   sys.exit()
           pause = functions.display_settings(screen, scores, shots, pars, settings)
           pygame.display.flip()


    #calling ball methods in main code
    shotCount = ball.shoot(shotCount)
    ball.aim()
    ball.move()
    ball.collision(walls)
    finished = hole.collision(ball.get_pos())

    #returning useful values to main file
    return finished, shotCount