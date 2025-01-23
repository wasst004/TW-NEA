import pygame

class Ball:

    #constructor
    def __init__(self,screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.radius = 10
        self.colour = "white"
        self.dx = 0
        self.dy = 0
        self.dragging = False
        self.pos1 = (0,0)


    #displays the ball object on sceen
    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.radius)

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
            pygame.draw.line(self.screen, 'white', self.pos1, mousePos, 2)

    #calculates an initial x and y speed based on mouse movement
    def shoot(self, shotCount):
        mousePos = pygame.mouse.get_pos()
        ballArea = pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.radius)
        if ballArea.collidepoint(mousePos) and pygame.mouse.get_pressed()[0]:
            self.dragging = True
            self.pos1 = mousePos
        elif self.dragging and not pygame.mouse.get_pressed()[0]:
            self.dragging = False
            shotCount += 1
            pos2 = mousePos
            self.dx = (self.pos1[0]- pos2[0]) / 9
            self.dy = (self.pos1[1]- pos2[1]) / 9
        return shotCount

    #makes ball slow down as it rolls
    def move(self): 
        self.dx = round(self.dx, 2) # rounds to 2dp to reduce lag
        self.dy = round(self.dy, 2)
        self.x = round((self.x+self.dx),2)
        self.y = round((self.y+self.dy),2)
        self.dx *= 0.95 #decreases speed slightly each frame
        self.dy *= 0.95
        if abs(self.dx) < 0.1 and abs(self.dy) < 0.1:
            self.dx = 0
            self.dy = 0

     #collision detection
    def collision(self,walls):
        ballRect = pygame.Rect((self.x-self.radius), (self.y-self.radius), self.radius*2, self.radius*2)
        for wall in walls: # iterates through each wall
            wallRect = pygame.Rect(wall.tl[0], wall.tl[1], wall.tr[0] - wall.tl[0], wall.bl[1] - wall.tl[1])
            if ballRect.colliderect(wallRect):
                if wall.direction == "west" and ballRect.left < wallRect.right and self.dx < 0:
                    self.dx = -self.dx #changes direction of ball if it hits left wall
                elif wall.direction == "east" and ballRect.right > wallRect.left and self.dx > 0:
                    self.dx = -self.dx #changes direction of ball if it hits right wall
                elif wall.direction == "north" and ballRect.top < wallRect.bottom and self.dy < 0:
                    self.dy = -self.dy #changes direction of ball if it hits top wall
                elif wall.direction == "south" and ballRect.bottom > wallRect.top and self.dy > 0:
                    self.dy = -self.dy #changes direction of ball if it hits bottom wall

        
class Wall:

    #sets values
    def __init__(self, screen, tl, tr, br, bl, direction):
        #tl, tr, br and bl refer to each corner of the shape e.g. top right
        self.screen = screen
        self.tl = tl
        self.tr = tr
        self.br = br
        self.bl = bl
        self.colour = "white"
        self.direction = direction

    #draws shape
    def draw(self):
        pygame.draw.polygon(self.screen, self.colour, [self.tl, self.tr, self.br, self.bl], 0)

class Hole:

    #constuctor
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = "black"
        self.radius = 15

    #draws the shape
    def draw(self):
        pygame.draw.circle(self.screen, self.colour, (self.x, self.y), self.radius)
    
    #checks for a collision with the hole
    def collision(self, ballPos, level1):
        holeArea = pygame.Rect(self.x -11, self.y -11, 22, 22)
        if holeArea.collidepoint(ballPos):
            return False
        else:
            return True


class Button:

    #constructor
    def __init__(self, screen, x, y, colour, width, height, shape):
        self.screen = screen
        self.x = x
        self.y = y
        self.colour = colour
        self.width = width
        self.height = height
        self.shape = shape

    #draws shape
    def draw(self):
        if self.shape == "square":
            pygame.draw.rect(self.screen, self.colour, (self.x, self.y, self.width, self.height))
        else:
            pygame.draw.circle(self.screen, self.colour, (self.x, self.y), (self.width/2))

    #detects a mouse click
    def clicked(self):
        mousePos = pygame.mouse.get_pos()
        buttonArea = pygame.Rect(self.x, self.y, self.width, self.height)
        if buttonArea.collidepoint(mousePos) and pygame.mouse.get_pressed()[0]:
          return 1
        else:
          return 0
