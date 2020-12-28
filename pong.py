import pygame, random

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
        self.ball_x = 800/2
        self.ball_y = 600/2
        self.ball_pos = (self.ball_x, self.ball_y)
        self.speed_x = 2
        self.speed_y = 2
        self.reset()

    def move_ball(self):
        self.ball_y += self.random_y_speed
        self.ball_x += self.random_x_speed
        self.ball_pos = (self.ball_x, self.ball_y)
    
    def reset(self):
        self.random_x_speed = random.choice([-self.speed_x, self.speed_x])
        self.random_y_speed = random.choice([-self.speed_y, self.speed_y, 0])

class MAIN(object):
    def __init__(self):
        self.player = PLAYER()
        self.opponent = OPPONENT()
        self.ball = BALL()

    def draw_objects(self):
        screen.fill((0, 0, 0))
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
logo_surface = pygame.image.load("assets/ponglogo.jpg").convert()
pygame.display.set_icon(logo_surface)
clock = pygame.time.Clock()

#Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    game_main.ball.move_ball()
    game_main.draw_objects()

    pygame.display.update()
    clock.tick(120)
pygame.quit()