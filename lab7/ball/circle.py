import pygame

pygame.init()


width = 800
height = 600
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

done = False
x = 400
y = 300
RED = (255, 0, 0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_UP] and y > 25:
        y -= 20
    if pressed[pygame.K_DOWN] and y < 575:
        y += 20
    if pressed[pygame.K_RIGHT] and x < 775:
        x += 20
    if pressed[pygame.K_LEFT] and x > 25:
        x -= 20
    


    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, RED, (x, y), 25)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()