import pygame
import random
import time

pygame.init()


board = [[0 for x in range(50)] for row in range(25)]


cols, rows = 50, 25
cell_size = 25
window_size = (cols * cell_size, rows * cell_size)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Flag game")

character = pygame.image.load("C:\\Users\\jbt\\Downloads\\lethl.png")
character = pygame.transform.scale(character, (cell_size, cell_size))

flag = pygame.image.load("C:\\Users\\jbt\\Downloads\\flag.png")
flag = pygame.transform.scale(flag, (50, 50))

grss = pygame.image.load("C:\\Users\\jbt\\Downloads\\grass.png")
grss = pygame.transform.scale(grss, (50, 50))

x, y = cols // 2 * cell_size, rows // 2 * cell_size

t, b = 22, 25

speed = 1

grid = False
grid_start_time = 0
grid_duration = 1
running = True
grs_amount = 10
grss_graft = []

for i in range(grs_amount):
    grss_x = random.randint(0, cols - 1) * cell_size
    grss_y = random.randint(0, rows - 1) * cell_size
    grss_graft.append((grss_x, grss_y))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                grid = True
                grid_start_time = time.time()

    if grid:
        if time.time() - grid_start_time > grid_duration:
            show_grid = False

        for row in range(rows):
            pygame.draw.line(window, 'black', (0, row * cell_size), (window_size[0], row * cell_size))
        for col in range(cols):
            pygame.draw.line(window, 'black', (col * cell_size, 0), (col * cell_size, window_size[1]))

    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x < window_size[0] - cell_size:
            x += speed
        if keys[pygame.K_UP] and y > 0:
            y -= speed
        if keys[pygame.K_DOWN] and y < window_size[1] - cell_size:
            y += speed


        window.fill('light green')

        for i in grss_graft:
            window.blit(grss, (i[0], i[1]))

        window.blit(character, (x, y))

        window.blit(flag, (t, b))


    pygame.display.flip()

pygame.quit()
