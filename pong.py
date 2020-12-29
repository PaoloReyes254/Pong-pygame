import pygame, random

#Classes
class PLAYER(object):
    def __init__(self):
        self.width = 6
        self.height = 90
        self.pos = 300 - (self.height/2)
        self.rect = pygame.Rect(10, self.pos, self.width, self.height)
    
    def move_up(self):
        if self.pos <= 0:
            self.pos = 0
        else:
            self.pos -= 5
            self.rect = pygame.Rect(10, self.pos, self.width, self.height)

    def move_down(self):
        if self.pos + self.height >= 600:
            self.pos = 600 - self.height
        else:
            self.pos += 5
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
        self.player_score = 0
        self.opponent_score = 0
        self.reset()

    def move_ball(self):
        self.ball_y += self.random_y_speed
        self.ball_x += self.random_x_speed
        self.ball_pos = (self.ball_x, self.ball_y)
        self.bounce()
        self.out_screen()
    
    def bounce(self):
        if self.ball_y <= 0 or self.ball_y >= 590:
            self.random_y_speed = -self.random_y_speed

    def out_screen(self):
        if self.ball_x <= -10:
            self.opponent_score += 1
            self.ball_x = 800/2
            self.ball_y = 600/2
            self.ball_pos = (self.ball_x, self.ball_y)
            self.reset()
        elif self.ball_x >= 810:
            self.player_score += 1
            self.ball_x = 800/2
            self.ball_y = 600/2
            self.ball_pos = (self.ball_x, self.ball_y)
            self.reset()

    def reset(self):
        self.random_x_speed = random.choice([-self.speed_x, self.speed_x])
        self.random_y_speed = random.choice([-self.speed_y, self.speed_y])

class MAIN(object):
    def __init__(self):
        self.player = PLAYER()
        self.opponent = OPPONENT()
        self.ball = BALL()

    def draw_objects(self):
        screen.fill((0, 0, 0))
        #Dvision line
        self.division_rect = pygame.Rect(388, 0, 4, 600)
        pygame.draw.rect(screen, (127, 127, 127), self.division_rect)

        #Text
        self.game_font = pygame.font.Font("assets/FreeSansBold.ttf", 100)
        self.player_score = self.game_font.render(str(self.ball.player_score), True, (180, 180, 180))
        self.opponent_score = self.game_font.render(str(self.ball.opponent_score), True, (180, 180, 180))
        self.player_rect = self.player_score.get_rect(center = (280, 50))
        self.opponent_rect = self.opponent_score.get_rect(center = (500, 50))
        screen.blit(self.player_score, self.player_rect)
        screen.blit(self.opponent_score, self.opponent_rect)

        #Objects
        pygame.draw.rect(screen, (254, 254, 254), self.player.rect)
        pygame.draw.rect(screen, (254, 254, 254), self.opponent.rect)
        pygame.draw.circle(screen, (254, 254, 254), self.ball.ball_pos, self.ball.radius, 0)

        #Methods
        self.check_collision()
        self.follow_ball()

    def check_collision(self):
        if self.ball.ball_x == 16 and self.ball.ball_y >= self.player.rect.top and self.ball.ball_y <= self.player.rect.bottom-60:
            self.ball.random_x_speed = -self.ball.random_x_speed
            self.ball.random_y_speed = random.choice([self.ball.speed_y, -self.ball.speed_y])
        elif self.ball.ball_x == 16 and self.ball.ball_y >= self.player.rect.bottom-60 and self.ball.ball_y <= self.player.rect.bottom-30:
            self.ball.random_x_speed = -self.ball.random_x_speed
        elif self.ball.ball_x == 16 and self.ball.ball_y >= self.player.rect.bottom-30 and self.ball.ball_y <= self.player.rect.bottom:
            self.ball.random_x_speed = -self.ball.random_x_speed
            self.ball.random_y_speed = random.choice([self.ball.speed_y, -self.ball.speed_y])
        elif self.ball.ball_x == 800-16 and self.ball.ball_y >= self.opponent.rect.top and self.ball.ball_y <= self.opponent.rect.bottom-60:
            self.ball.random_x_speed = -self.ball.random_x_speed
            self.ball.random_y_speed = random.choice([self.ball.speed_y, -self.ball.speed_y])
        elif self.ball.ball_x == 800-16 and self.ball.ball_y >= self.opponent.rect.bottom-60 and self.ball.ball_y <= self.opponent.rect.bottom-30:
            self.ball.random_x_speed = -self.ball.random_x_speed
        elif self.ball.ball_x == 800-16 and self.ball.ball_y >= self.opponent.rect.bottom-30 and self.ball.ball_y <= self.opponent.rect.bottom:
            self.ball.random_x_speed = -self.ball.random_x_speed
            self.ball.random_y_speed = random.choice([self.ball.speed_y, -self.ball.speed_y])

    def follow_ball(self):
        if self.ball.ball_y <= self.opponent.rect.top:
            if self.opponent.pos <= 0:
                self.opponent.pos = 0
            else:
                self.opponent.pos -= 4
                self.opponent.rect = pygame.Rect(800-16, self.opponent.pos, self.opponent.width, self.opponent.height)
        elif self.ball.ball_y >= self.opponent.rect.bottom:
            if self.opponent.pos + self.opponent.height >= 600:
                self.opponent.pos = 600
            else:
                self.opponent.pos += 4
                self.opponent.rect = pygame.Rect(800-16, self.opponent.pos, self.opponent.width, self.opponent.height)

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

#Game variables
movement_up = False
movement_down = False

#Game loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                movement_up = True
            elif event.key == pygame.K_DOWN:
                movement_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                movement_up = False
            elif event.key == pygame.K_DOWN:
                movement_down = False

    if movement_up:
        game_main.player.move_up()
    elif movement_down:
        game_main.player.move_down()

    game_main.ball.move_ball()
    game_main.draw_objects()

    pygame.display.update()
    clock.tick(120)
pygame.quit()