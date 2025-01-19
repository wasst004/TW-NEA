import pygame

#funtion to show text on screen
def display_text(screen, text, x, y, size):
    font = pygame.font.Font(None, size) 
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))

#function to draw the parts of level one
def draw_elements(screen, ball, walls, hole):
    pygame.draw.rect(screen, "#3D872C", (605,530,50,40))
    ball.draw()
    for wall in walls:
        wall.draw()
    hole.draw()

#function to show current info on screen
def draw_board(screen, level, shotCount, pars):
    pygame.draw.rect(screen, "#CE514F", (970,40,270,190))
    par = "Par: " + str(pars[level-1])
    level = "Level " + str(level)
    shots = "Shots: " + str(shotCount)
    display_text(screen, level, 980, 45, 65)
    display_text(screen, par, 980, 110, 65)
    display_text(screen, shots, 980, 175, 65)

def calculate_Score(shotCount, scoreMessages, pars, level):
    score = shotCount - pars[level-1]
    if shotCount == 1:
        return "Hole in One!"
    elif score > -3 and score < 4:
        return scoreMessages[score]
    else:
        return ("+" + str(score))