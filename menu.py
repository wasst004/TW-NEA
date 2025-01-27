import pygame
import functions

def menu(screen, buttons):
    for button in buttons:
        button.draw()
        complete = button.clicked()
    functions.display_text(screen, "PUTTZONE", 390, 50, 150)

    pygame.draw.polygon(screen, "#273963", [(610, 485), (690,535), (610, 585)], 0)
    pygame.draw.polygon(screen, "#86A8F4", [(610, 485), (690, 535), (610, 585)], 1)

    functions.display_text(screen, "- Shoot by clicking and dragging", 200, 200, 40)
    functions.display_text(screen, "- Hold down settings to see previous scores", 200, 250, 40)
    
    return complete