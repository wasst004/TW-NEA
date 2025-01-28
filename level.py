import pygame
import functions


def level(screen, ball, walls, hole, shotCount, currentLevel, pars, scoreMessages, rect, settings, scores, shots, roughGrass):
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

    slowDown = 0.95
    for rough in roughGrass:
        rough.draw()
    for rough in roughGrass:    
        slowDown = rough.rolling_over(ball)
        if slowDown < 0.95:
            break

    #calling ball methods in main code
    shotCount = ball.shoot(shotCount)
    ball.aim()
    ball.move(slowDown)
    ball.collision(walls)
    finished = hole.collision(ball.get_pos())

    #returning useful values to main file
    return finished, shotCount