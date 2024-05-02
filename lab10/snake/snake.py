import pygame
import random
from color_palette import *
from collections import namedtuple
import psycopg2

pygame.init()

conn = psycopg2.connect(
    host="localhost",
    database="snake",
    user="postgres",
    password="1324"
)

cur = conn.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS scores(
 
   username varchar(100),
   user_score int,
   user_level int
   )'''
)
conn.commit()
font = pygame.font.SysFont("Vergena", 30, True)
bigfont = pygame.font.SysFont("Vergena", 50, True)


# Directions
class Direction():
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'
    UP = 'UP'
    DOWN = 'DOWN'

# Getting Positions 
Point = namedtuple('Point', 'x y')

# Variables 
CELL = 20
SPEED = 7
running = True
game_over = False
SCORE = 0
LEVEL = 0
#background music
back_sound = pygame.mixer.music
back_sound.load('a.mp3')
back_sound.play(-1)
back_sound.set_volume(0.1)

def insertname(username):
    cur.execute(
        "INSERT INTO scores VALUES('{}', 0, 0)".format(username)
    )
    conn.commit()


def upd(user):
    cur.execute(
        "SELECT * FROM scores WHERE username = '{}'".format(user)
    )
    row = cur.fetchone()
    cur.execute(
        "UPDATE scores SET user_score = '{}', user_level = '{}' WHERE username = '{}'".format
        (max(row[1], SCORE), max(row[2], LEVEL), user)
    )
    conn.commit()


print("Enter your name")
username = input()
cur.execute("SELECT count(*) FROM scores WHERE username='{}'".format(username))
conn.commit()
if cur.fetchone()[0] == 0:
    insertname(username)
    conn.commit()
else:
    cur.execute("SELECT * FROM scores WHERE username = '{}'".format(username))
    data = cur.fetchone()
    print("User's max score:{}".format(data[1]))
    print("User's max level:{}".format(data[2]))
# Main Class
class Game:
    def __init__(self, WIDTH=800, HEIGHT=600):
        # Initializing 
        global SCORE
        global LEVEL
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Snake')


        # Starting positions, directions 
        self.direction = Direction.RIGHT
        self.head = Point(self.WIDTH // 2, self.HEIGHT // 2)
        # The initial snake with a length of 3 with its body coordinates 
        self.snake = [self.head,
                      Point(self.head.x - CELL, self.head.y),
                      Point(self.head.x - (2 * CELL), self.head.y)]
        SCORE = 0
        LEVEL = 0
        self.food = None
        self.food_move()

    # Snake Movement 
    def move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += CELL
        elif direction == Direction.LEFT:
            x -= CELL
        elif direction == Direction.DOWN:
            y += CELL
        elif direction == Direction.UP:
            y -= CELL
        self.head = Point(x, y)
               
    # Moving Food to random positions 
    def food_move(self):
        x = random.randint(0, (self.WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (self.HEIGHT - CELL) // CELL) * CELL
        self.food = Point(x, y)
        if self.food in self.snake:
            self.food_move()
            
    # Snake Turns and the Exit Condition 
    def play_step(self):
        global SCORE
        global LEVEL
        # User Inputs From Keyboard 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_p:
                    paused = True
                    while paused:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.QUIT
                                quit()
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_c:
                                    paused = False
                                elif event.key == pygame.K_s:
                                    upd(username)
                                    pygame.QUIT
                                    quit()
                                elif event.key == pygame.K_q:
                                    pygame.QUIT
                                    quit()
                        font = pygame.font.SysFont("Vergena", 80, True)
                        self.screen.fill(colorYELLOW)
                        text1 = font.render("To continue press c", True, (colorWHITE))
                        text2 = font.render("To save and quit press s", True, (colorWHITE))
                        text3 = font.render("To quit press q", True, (colorWHITE))
                        pygame.draw.rect(self.screen,  (colorBLUE), pygame.Rect(80, 100, 670, 350))
                        self.screen.blit(text1, (140, 150))
                        self.screen.blit(text2, (90, 250))
                        self.screen.blit(text3, (200, 350))
                        pygame.display.update()

        # Move 
        self.move(self.direction)  # Update The Head
        self.snake.insert(0, self.head)

        # Check If Game Over 
        if self.collision():
            global game_over
            game_over = True

        # Place New Food 
        if self.head == self.food:
            SCORE += 1
            self.food_move()
            if SCORE//5 > LEVEL:
                global SPEED
                LEVEL = SCORE//5
                SPEED += 3
        else:
            self.snake.pop()

        # Update Interface

        self.update()
        self.clock.tick(SPEED)

    def collision(self):
        # Hits Boundary 
        if self.head.x > self.WIDTH - CELL or self.head.x < 0 or self.head.y > self.HEIGHT - CELL or self.head.y < 0:
            upd(username)
            pygame.display.flip()
            back_sound.stop()
            pygame.mixer.Sound('fail.mp3').play().set_volume(0.3)
            return True
        # Hits Itself 
        global game_over
        if self.head in self.snake[1:]:
            upd(username)
            pygame.display.flip()
            back_sound.stop()
            pygame.mixer.Sound('fail.mp3').play().set_volume(0.3)
            return True

        return False

    def update(self):
        colors = [colorGRAY, colorGRAY]
        for i in range(self.HEIGHT // 2):
            for j in range(self.WIDTH // 2):
                pygame.draw.rect(self.screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

        pygame.draw.rect(self.screen, (colorYELLOW), pygame.Rect(self.head.x, self.head.y, CELL, CELL))
        pygame.draw.rect(self.screen, (colorBLACK), pygame.Rect(self.head.x + 4, self.head.y + 4, 6, 6))
        pygame.draw.rect(self.screen, (colorBLACK), pygame.Rect(self.head.x + 4, self.head.y + 12, 6, 6))

        for skin in self.snake[1:]:
            pygame.draw.rect(self.screen,  (colorBLACK), pygame.Rect(skin.x, skin.y, CELL, CELL))
            pygame.draw.rect(self.screen, (colorGREEN), pygame.Rect(skin.x + 4, skin.y + 4, 12, 12))

        pygame.draw.rect(self.screen, (colorRED), pygame.Rect(self.food.x, self.food.y, CELL, CELL))

        text1 = font.render(f"Score: {SCORE}", True, (colorBLACK))
        text2 = font.render(f"Level: {LEVEL}", True, (colorBLACK))
        self.screen.blit(text1, (self.WIDTH//2 - 20, 10))
        self.screen.blit(text2, (self.WIDTH//2 - 20, 30))
        if self.collision():
            text3 = bigfont.render(f"Press ANY key to Restart", True, (colorBLUE))
            self.screen.blit(text3, (self.HEIGHT // 2 - 100, self.WIDTH // 2 - 100))
        pygame.display.flip()

    




# Game Loop
game = Game()
while running:
    score = game.play_step()   
    # game_over

    if game_over == True:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                # Restart Conditions 
                elif event.type == pygame.KEYDOWN:
                    SPEED = 7
                    game = Game()
                    pygame.mixer.stop()
                    back_sound = pygame.mixer.music
                    back_sound.load('a.mp3')
                    back_sound.play(-1)
                    back_sound.set_volume(0.1)
                    game_over = False

pygame.quit()
exit()
