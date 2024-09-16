import pygame as py
import time
import random
import json

py.init()

board = [[0 for x in range(50)] for row in range(25)]


board[0][0] = 1
cols, rows = 50, 25
cell_size = 25
window_size = (cols * cell_size, rows * cell_size)
window = py.display.set_mode(window_size)
py.display.set_caption("Flag game")

character = py.image.load("C:\\Users\\jbt\\Downloads\\lethl.png")
character = py.transform.scale(character, (cell_size * 2, cell_size * 4))

flag = py.image.load("C:\\Users\\jbt\\Downloads\\flag_0.jpg")
flag = py.transform.scale(flag, (100, 90))

grss = py.image.load("C:\\Users\\jbt\\Downloads\\grass.png")
grss = py.transform.scale(grss, (50, 50))

bomb = py.image.load("C:\\Users\\jbt\\Downloads\\bomb.png")
bomb = py.transform.scale(bomb, (50, 50))

x, y = 0, 0

t, b = 1150, 550

l, g = 0, 0

speed = 1


font = py.font.Font('freesansbold.ttf', 40)

lose_text = font.render('You Lose', True, 'black')
lose_textRect = lose_text.get_rect()
win_text = font.render('You Won', True, 'black')
win_textRect = win_text.get_rect()
lose_textRect.center = (window_size[0] // 2, window_size[1] // 2)
win_textRect.center = (window_size[0] // 2, window_size[1] // 2)
display_surface = py.display.set_mode((window_size[0], window_size[1]))

KEYS = [py.K_1, py.K_2, py.K_3, py.K_4, py.K_5, py.K_6, py.K_7, py.K_8, py.K_9]

game_start = 0
grs_amount = 20
grss_graft = []
for i in range(grs_amount):
    grss_x = random.randint(0, cols - 1) * cell_size
    grss_y = random.randint(0, rows - 1) * cell_size
    grss_graft.append((grss_x, grss_y))

bomb_amount = 20
bombs_apper = []
for i in range(bomb_amount):
    bomb_x = random.randint(0, 23)
    bomb_y = random.randint(0, 48)
    if board[bomb_x][bomb_y] == 0:
        bombs_apper.append((bomb_x, bomb_y))
        board[bomb_x][bomb_y] = 3

board[22][47] = 4

grid = False
grid_start_time = 0
grid_duration = 1
running = True

flag_list=[]
for i in range(21,25):
    for j in range(46,50):
        flag_list.append((i,j))


while running:
    window.fill('light green')

    if grid:
        if time.time() - grid_start_time > grid_duration:
            grid = False

        window.fill((68, 69, 71))
        window.blit(character, (x * 25, y * 25))
        window.blit(flag, (t, b))

        for row in range(rows):
            py.draw.line(window, 'light green', (0, row * cell_size), (window_size[0], row * cell_size))
        for col in range(cols):
            py.draw.line(window, 'light green', (col * cell_size, 0), (col * cell_size, window_size[1]))

        for i in bombs_apper:
            window.blit(bomb, (i[1] * cell_size, i[0] * cell_size))

    else:
        for event in py.event.get():
            if event.type == py.QUIT:
                exit()

            for i in KEYS:
                if event.type == py.KEYDOWN:
                    if event.key == i:
                        game_start = py.time.get_ticks()
                if event.type == py.KEYUP:
                    if event.key == i:
                        game_end = py.time.get_ticks()
                        if game_end - game_start < 1000:
                            data = {
                                'player_pos': (x,y),
                                'bomb': bombs_apper,
                                'grass': grss_graft,
                                'board': board
                            }
                            file_data = open('data.txt', 'w')
                            json.dump(data,file_data)
                            file_data.close()

                        else:
                            file_data = open('data.txt', 'r')
                            file = json.load(file_data)
                            bombs_apper = file['bomb']
                            x, y = file['player_pos'][0], file['player_pos'][1]
                            grss_graft = file['grass']
                            board = file['board']
                            file_data.close()

            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    grid = True
                    grid_start_time = time.time()

            keys = py.key.get_pressed()
            if keys[py.K_LEFT] and x > 0:
                board[y][x] = 0
                x -= speed
                board[y][x] = 1
                for i in board:
                    print(i)
            if keys[py.K_RIGHT] and x < 48:
                board[y][x] = 0
                x += speed
                board[y][x] = 1
                for i in board:
                    print(i)
            if keys[py.K_UP] and y > 0:
                board[y][x] = 0
                y -= speed
                board[y][x] = 1
                for i in board:
                    print(i)
            if keys[py.K_DOWN] and y < 21:
                board[y][x] = 0
                y += speed
                board[y][x] = 1
                for i in board:
                    print(i)
            print(x, y)


        for i in grss_graft:
            window.blit(grss, (i[0], i[1]))

        player_pos = []
        for j in (x, x + 2):
            player_pos.append((y + 3, j))

            for i in player_pos:
                if i in bombs_apper:
                    display_surface.fill('white')
                    display_surface.blit(lose_text, lose_textRect)
                    py.display.flip()
                    time.sleep(2)
                    quit()

                if i in flag_list:
                    window.fill('light blue')
                    display_surface.blit(win_text, win_textRect)
                    py.display.flip()
                    time.sleep(2)
                    quit()


        window.blit(character, (x * 25, y * 25))
        window.blit(flag, (t, b))

    py.display.flip()
py.quit()
