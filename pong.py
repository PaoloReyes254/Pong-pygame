import pygame

#Classes
class PLAYER(object):
    def __init__(self):
        self.width = 6
        self.height = 80
        self.pos = 300 - (self.height/2)
        self.rect = pygame.Rect(10, self.pos, self.width, self.height)

class OPPONENT(PLAYER):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(800-10-self.width, self.pos, self.width, self.height)

class BALL(object):
    def __init__(self):
        self.radius = 8
        self.ball_pos = (800/2, 600/2)

class MAIN(object):
    def __init__(self):
        self.player = PLAYER()
        self.opponent = OPPONENT()
        self.ball = BALL()

    def draw_objects(self):
        pygame.draw.rect(screen, (254, 254, 254), self.player.rect)
        pygame.draw.rect(screen, (254, 254, 254), self.opponent.rect)
        pygame.draw.circle(screen, (254, 254, 254), self.ball.ball_pos, self.ball.radius, 0)

#Objects
game_main = MAIN()

#Pygame init
pygame.init()

#Initial settings
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")
logo_surface = pygame.image.load("assets/ponglogo.jpg").convert_alpha()
pygame.display.set_icon(logo_surface)
clock = pygame.time.Clock()

#Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game_main.draw_objects()

    pygame.display.update()
    clock.tick(120)
pygame.quit()