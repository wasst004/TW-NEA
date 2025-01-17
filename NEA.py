#importing
import sys
import pygame
from pygame.locals import K_UP, K_DOWN, K_LEFT, K_RIGHT

#setup
pygame.init()
screen = pygame.display.set_mode((1280, 680))
playing = True
clock = pygame.time.Clock()
framerate = 30


class Ball:

    #constructor
    def __init__(self,screen, x, y):
        self.x = x
        self.y = y
        self.radius = 10
        self.colour = "white"
        self.dx = 0
        self.dy = 0
        self.dragging = False

    #displays the ball object on sceen
    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

    #allows the main code to change the position of the ball
    def set_pos(self, x, y):
        self.x += x
        self.y += y

    #returns the position of the ball to the main code
    def get_pos(self):
        return (self.x , self.y)

    #displays aiming line as you are dragging back
    def aim(self):
        if self.dragging:
            mousePos = pygame.mouse.get_pos()
            pygame.draw.line(screen, 'white', self.pos1, (mousePos), 2)

    #calculates an initial x and y speed based on mouse movement
    def shoot(self):
        mousePos = pygame.mouse.get_pos()
        ballArea = pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
        if ballArea.collidepoint(mousePos) and pygame.mouse.get_pressed()[0] == True:
            self.dragging = True
            self.pos1 = mousePos
        elif self.dragging and pygame.mouse.get_pressed()[0] == False:
            self.dragging = False
            pos2 = mousePos
            self.dx = (self.pos1[0]- pos2[0]) / 10
            self.dy = (self.pos1[1]- pos2[1]) / 10

    #makes ball slow down as it rolls
    def move(self): 
        self.x += self.dx
        self.y += self.dy
        self.dx *= 0.95
        self.dy *= 0.95
        if abs(self.dx) < 0.1 and abs(self.dy) < 0.1:
            self.dx = 0
            self.dy = 0

     #collision detection
    def collision(self,walls):
        ballRect = pygame.Rect((self.x-self.radius), (self.y-self.radius), self.radius*2, self.radius*2)
        for wall in walls:
            wallRect = pygame.Rect(wall.tl[0], wall.tl[1], wall.tr[0] - wall.tl[0], wall.bl[1] - wall.tl[1])
            if ballRect.colliderect(wallRect):
                if abs(ballRect.left - wallRect.right) < abs(self.dx) or abs(ballRect.right - wallRect.left) < abs(self.dx):
                    self.dx = -self.dx # Reflect X velocity if ball hits lest o right edge
                if abs(ballRect.top - wallRect.bottom) < abs(self.dy) or abs(ballRect.bottom - wallRect.top) < abs(self.dy):
                    self.dy = -self.dy # Reflect Y velocity if ball hits top or bottom

        
class Wall:

    #sets values
    def __init__(self, screen, tl, tr, br, bl):
        self.tr = tr
        self.tl = tl
        self.br = br
        self.bl = bl
        self.colour = "white"

    #draws shape
    def draw(self):
        pygame.draw.polygon(screen, self.colour, [self.tl, self.tr, self.br, self.bl], 0)

class Hole:

    #constuctor
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.colour = "black"
        self.radius = 15

    def draw(self):
        pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)
    
    def collision(self, ballPos, level1):
        holeArea = pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius-6)
        if holeArea.collidepoint(ballPos):
            return False
        else:
            return True


def display_text(text, x, y):
    font = pygame.font.Font(None, 74) 
    text = font.render(text, True, (255, 255, 255))
    screen.blit(text, (x, y))


#initialising instances of ball and wall classes
ball = Ball(screen, 630, 550)
walls = [
    Wall(screen, (530,90), (540,90), (540,590), (530,590)),
    Wall(screen, (710,90), (720,90), (720,590), (710,590)),
    Wall(screen, (530,80), (720,80), (720,90), (530,90)),
    Wall(screen, (530,590), (720,590), (720,600), (530,600))
        ]
hole = Hole(screen, 630, 130)

level1 = True
font = pygame.font.Font('freesansbold.ttf', 32)


#main game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        #drawing screen and ball location every game loop
        screen.fill('#55CE79')

        
            pygame.draw.rect(screen, "#3D872C", (605, 530,50,40))
            ball.draw()
            for wall in walls:
                wall.draw()
            hole.draw()
            
            #mainual controls
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                ball.set_pos(0,-10)
            elif keys[K_DOWN]:
                ball.set_pos(0,10)
            elif keys[K_LEFT]:
                ball.set_pos(-10,0)
            elif keys[K_RIGHT]:
                ball.set_pos(10,0)
                
        if level1:  
            #calling ball methods in main code
            ball.shoot()
            ball.aim()
            ball.move()
            ball.collision(walls)

            ballPos = ball.get_pos()
            level1 = hole.collision(ballPos, level1)
        else:
            display_text("YOU WON LEVEL 1", 600, 400)


    pygame.display.flip()
    clock.tick(framerate)
