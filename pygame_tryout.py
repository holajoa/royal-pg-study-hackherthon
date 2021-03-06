import pygame
import os
from math import sqrt
import random as rnd
from numpy.random import permutation
import time

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
empty_surface = pygame.Surface((WIDTH, HEIGHT))
pygame.display.set_caption('Categorising waste!')

# button variables
RADIUS = 28


# load images, generate random image
bin_images, waste_images = [], []
stock = {'A': 5, 'B': 6, 'C': 7, 'D': 3}  # number of images for each bin


def load_images():
    perm = permutation(list(range(4)))
    for i in ['A', 'B', 'C', 'D']:
        bin_image = pygame.image.load(os.path.join('bins', str(i)+'.png'))
        bin_images.append(bin_image)
        rnd_num = rnd.randint(1, stock[i])
        waste_image = pygame.image.load(
            os.path.join('trash', i+'_'+str(rnd_num)+'.png')
        )
        waste_images.append(waste_image)
    return waste_images, bin_images, perm


# game variables
global b_turn, w_turn, count, perm
wastes = []
bins = []
b_turn, w_turn = False, True
count = 0
ans_chars = []

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 62, 112)


# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


# text variable
FONT = pygame.font.SysFont('comicsans', 24)
BIN_FONT = pygame.font.SysFont('comicsans', 16)


def draw():
    global perm
    win.fill(WHITE)

    # display text
    text = 'Click a piece of waste first, and match it with the right bin'
    text = FONT.render(text, 1, BLACK)
    win.blit(text, (190, 50))

    # draw buttons

    for i in range(4):
        win.blit(bin_images[i], (160+150*i, 300))
        pygame.draw.circle(win, WHITE, (180+150*i, 325), RADIUS, 3)
        bins.append([180+150*i, 325, str(chr(i+65))])

    # increased y-coordinate by 20
        win.blit(waste_images[i], (160+150*perm[i], 120))
        pygame.draw.circle(win, WHITE, (180+150*perm[i], 140), RADIUS, 3)
        wastes.append([180+150*perm[i], 140, str(i+1)])

    # display bin text
    for e, i in enumerate(
        ['Hazardous Waste', 'Recyclable Waste', 'Food Waste', 'Residual Waste']
    ):
        text = BIN_FONT.render(i, 1, BLACK)
        if e == 0 or e == 1:
            win.blit(text, (135+150*e, 360))
        else:
            win.blit(text, (145+150*e, 360))

    pygame.display.update()


def click():
    global w_turn, b_turn, count, ans_chars

    m_x, m_y = pygame.mouse.get_pos()
    global x_w, y_w

    if w_turn:
        for waste in wastes:
            x_w, y_w, w = waste
            dist = sqrt((x_w - m_x)**2 + (y_w - m_y)**2)
            if dist <= RADIUS:
                if w in ans_chars:
                    print('Already paired - choose another waste!')
                    break
                else:
                    ans_chars.append(w)
                    b_turn, w_turn = True, False
                    count += 1
                    break
        return

    if b_turn:
        for bin in bins:
            x, y, b = bin
            dist = sqrt((x - m_x)**2 + (y - m_y)**2)
            if dist <= RADIUS:
                if b in ans_chars:
                    print('Already paired - choose another bin!')
                    break
                else:
                    ans_chars.append(b)
                    pygame.draw.line(win, BLACK, (x_w, y_w), (x, y))
                    w_turn, b_turn = True, False
                    count += 1
                    break
        return


# main routine
waste_images, bin_images, perm = load_images()
draw()

while run:

    clock.tick(FPS)

    # Loop through all events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Initialise bins, wastes and solution pairs
            bins_ = [bin_[-1] for bin_ in bins[:4]]
            wastes_in_order = [waste_[-1] for waste_ in wastes[:4]]
            solution = [[], [], [], []]
            for i in range(4):
                solution[i].append(wastes_in_order[i])
                solution[i].append(bins_[i])

            click()
            pygame.display.update()

            # print('current decisions:', ans_chars)
            # print('solutions:', solution)
            if count == 8:
                print('------------------All pairs complete------------------')
                ans_pairs = [[ans_chars[2*k], ans_chars[2*k+1]]
                             for k in range(4)]
                if sorted(ans_pairs) == sorted(solution):
                    print('All correct - well done!')
                    # rect1 = pygame.Rect(280, 190, 100, 30)
                    # rect1.fill(BLUE)
                    text = 'All correct - well done!'
                    rect1 = pygame.Rect(290, 190, 200, 30)
                    pygame.draw.rect(win, BLUE, rect1)
                    text = FONT.render(text, 1, WHITE)
                    win.blit(text, (300, 200))
                    pygame.display.update()
                    continue
                    # draw()
                else:
                    print('Some are mismatched - please try again:(')
                    text = 'Some are mismatched - please try again:('
                    rect2 = pygame.Rect(290, 195, 350, 30)
                    pygame.draw.rect(win, BLUE, rect2)
                    text = FONT.render(text, 1, WHITE)
                    win.blit(text, (300, 200))
                    pygame.display.update()
                    time.sleep(3)
                    draw()
                count = 0
                ans_chars = []


pygame.quit()