import pygame
import functions

def menu(screen, buttons):
    for button in buttons:
        button.draw()
        complete = button.clicked()
    functions.display_text(screen, "PUTTZONE", 390, 50, 150)

    pygame.draw.polygon(screen, "#273963", [(610, 485), (690,535), (610, 585)], 0)
    pygame.draw.polygon(screen, "#86A8F4", [(610, 485), (690, 535), (610, 585)], 1)
    
    return complete
    
