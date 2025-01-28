import pygame

#funtion to show text on screen
def display_text(screen, text, x, y, size):
    font = pygame.font.Font(None, size) 
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))

#function to draw the parts of level one
def draw_elements(screen, ball, walls, hole, rect):
    pygame.draw.rect(screen, "#24542F", rect)
    ball.draw()
    for wall in walls:
        wall.draw()
    hole.draw()

#function to show current info on screen
def draw_board(screen, level, shotCount, pars, settings):
    #topright box showing current level, par and shots
    pygame.draw.rect(screen, "#CE514F", (970,40,270,190))
    par = "Par: " + str(pars[level-1]) #converting values to strings
    level = "Level " + str(level)
    shots = "Shots: " + str(shotCount)
    display_text(screen, level, 980, 45, 65) #displaying then on screen
    display_text(screen, par, 980, 110, 65)
    display_text(screen, shots, 980, 175, 65)
    #settings button in top left
    settings.draw()
    pause = settings.clicked()
    return pause


def calculate_Score(shotCount, scoreMessages, pars, level):
    score = shotCount - pars[level-1]
    if shotCount == 1:
        return score, "Hole in One!"
    elif score > -3 and score < 4:
        return score, scoreMessages[score]
    else:
        return score, ("+" + str(score))


def display_settings(screen, scores, shots, pars, settings):
    #text headings
    display_text(screen, "Level", 150, 100, 100)
    display_text(screen, "Par", 350, 100, 100)
    display_text(screen, "Shots", 490, 100, 100)
    display_text(screen, "Score", 700, 100, 100)
    #level numbers
    for i in range(1,5):
        text = str(i)
        display_text(screen, text, 150, 90 + (i)*80, 80)
    #stored aray values
    for i in range (len(scores)):
        text1 = str(pars[i])
        text2 = str(shots[i])
        text3 = str(scores[i])
        display_text(screen, text1, 350, 170 + (i)*80, 80)
        display_text(screen, text2, 490, 170 + (i)*80, 80)
        display_text(screen, text3, 700, 170 + (i)*80, 80)

    settings.draw()
    pause = settings.clicked()
    return pause