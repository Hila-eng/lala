import pygame
import time
import random

pygame.init()


board = [[0 for x in range(50)] for row in range(25)]

for i in board:
    print(i)


board[0][0] = 1
cols, rows = 50, 25
cell_size = 25
window_size = (cols * cell_size, rows * cell_size)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Flag game")

character = pygame.image.load("C:\\Users\\jbt\\Downloads\\lethl.png")
character = pygame.transform.scale(character, (cell_size*2, cell_size*4))

flag = pygame.image.load("C:\\Users\\jbt\\Downloads\\flag.png")
flag = pygame.transform.scale(flag, (50, 50))

grss = pygame.image.load("C:\\Users\\jbt\\Downloads\\grass.png")
grss = pygame.transform.scale(grss, (50, 50))

bomb = pygame.image.load("C:\\Users\\jbt\\Downloads\\bomb.png")
bomb = pygame.transform.scale(bomb, (50, 50))


x, y = 0,0

t, b =700, 500


speed = 1

grs_amount = 20
grss_graft = []

for i in range(grs_amount):
    grss_x = random.randint(0, cols - 1) * cell_size
    grss_y = random.randint(0, rows - 1) * cell_size
    grss_graft.append((grss_x, grss_y))

bomb_amount = 20
bombs_apper = []
for i in range(bomb_amount):
    bomb_x = random.randint(0, cols - 1) * cell_size
    bomb_y = random.randint(0, rows - 1) * cell_size
    bombs_apper.append((bomb_x, bomb_y))

grid = False
grid_start_time = 0
grid_duration = 1
running = True


while running:
    window.fill('light green')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                grid = True
                grid_start_time = time.time()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            board[y][x] = 0
            x -= speed
            board[y][x] = 1
            for i in board:
                print(i)
        if keys[pygame.K_RIGHT] and x < 48:
            board[y][x] = 0
            x += speed
            board[y][x] = 1
            for i in board:
                print(i)
        if keys[pygame.K_UP] and y > 0:
            board[y][x] = 0
            y -= speed
            board[y][x] = 1
            for i in board:
                print(i)
        if keys[pygame.K_DOWN] and y < 21:
            board[y][x] = 0
            y += speed
            board[y][x] = 1
            for i in board:
                print(i)
        print(x, y)



    if grid:
        if time.time() - grid_start_time > grid_duration:
            grid = False

        window.fill((68, 69, 71))
        # window.blit(character, (x, y))
        window.blit(flag, (t, b))

        for row in range(rows):
            pygame.draw.line(window, 'light green', (0, row * cell_size), (window_size[0], row * cell_size))
        for col in range(cols):
            pygame.draw.line(window, 'light green', (col * cell_size, 0), (col * cell_size, window_size[1]))

        for i in bombs_apper:
            window.blit(bomb, (i[0], i[1]))


    for i in grss_graft:
        window.blit(grss, (i[0], i[1]))



    window.blit(character, (x*25, y*25))

    window.blit(flag, (t, b))



    pygame.display.flip()

pygame.quit()
