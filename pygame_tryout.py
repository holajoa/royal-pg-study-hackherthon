import pygame
import os
from math import sqrt

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
# #pygame.caption('Categorising waste!')

# button variables
RADIUS = 28


# load images
bin_images, waste_images = [], []
for i in range(1, 5):
    bin_image = pygame.image.load(os.path.join('bins', str(i)+'.png'))
    # bin_image = pygame.image.load('bins/', str(i), '.png')
    bin_images.append(bin_image)
    waste_image = pygame.image.load(os.path.join('trash', str(i)+'.png'))
    waste_images.append(waste_image)


# game variables
wastes = []
bins = []

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    win.fill(WHITE)

    # draw buttons
    for i in range(4):
        win.blit(bin_images[i], (160+150*i, 300))
        pygame.draw.circle(win, WHITE, (180+150*i, 325), RADIUS, 3)
        bins.append([180+150*i, 325, str(chr(i+65))])

        win.blit(waste_images[i], (160+150*i, 100))
        pygame.draw.circle(win, WHITE, (180+150*i, 120), RADIUS, 3)
        wastes.append([180+150*i, 120, str(i+1)])

    pygame.display.update()


def click():
    global w_turn, b_turn

    m_x, m_y = pygame.mouse.get_pos()

    if b_turn:
        for bin in bins:
            x, y, b = bin
            dist = sqrt((x - m_x)**2 + (y - m_y)**2)
            if dist <= RADIUS:
                print(b)
                w_turn, b_turn = True, False
                break
        return
    if w_turn:
        for waste in wastes:
            x, y, w = waste
            dist = sqrt((x - m_x)**2 + (y - m_y)**2)
            if dist <= RADIUS:
                print(w)
                b_turn, w_turn = True, False
                break
        return


global b_turn, w_turn
b_turn, w_turn = False, True

while run:

    clock.tick(FPS)

    draw()

    # Loop through all events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click()


pygame.quit()
