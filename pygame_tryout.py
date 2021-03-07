import pygame
import os
from math import sqrt
import random as rnd

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
# #pygame.caption('Categorising waste!')

# button variables
RADIUS = 28


# load images, generate random image
bin_images, waste_images = [], []
stock = {'A': 5, 'B': 7, 'C': 6, 'D': 3}  # number of images for each bin
for i in ['A', 'B', 'C', 'D']:
    bin_image = pygame.image.load(os.path.join('bins', str(i)+'.png'))
    bin_images.append(bin_image)
    rnd_num = rnd.randint(1, stock[i])
    waste_image = pygame.image.load(os.path.join('trash', i+'_'+str(rnd_num)+'.png'))
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
    global w_turn, b_turn, count, ans_chars

    m_x, m_y = pygame.mouse.get_pos()

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
                    w_turn, b_turn = True, False
                    count += 1
                    break
        return
    if w_turn:
        for waste in wastes:
            x, y, w = waste
            dist = sqrt((x - m_x)**2 + (y - m_y)**2)
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


global b_turn, w_turn, count
b_turn, w_turn = False, True
count = 0
ans_chars = []

while run:

    clock.tick(FPS)

    draw()


    # Loop through all events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # Initialise bins, wastes and solution pairs
            bins_ = [bin_[-1] for bin_ in bins[:4]]
            wastes_in_order = [waste_[-1] for waste_ in wastes[:4]]  # in some order
            solution = [[], [], [], []]
            for i in range(4):
                solution[i].append(wastes_in_order[i])
                solution[i].append(bins_[i])
            print(solution)

            click()
            print('current decisions:', ans_chars)
            # print('solutions:', solution)
            if count == 8:
                print('------------------All pairs complete------------------')
                ans_pairs = [[ans_chars[2*k], ans_chars[2*k+1]] for k in range(4)]
                if sorted(ans_pairs) == sorted(solution):
                    print('All correct - well done!')
                else:
                    print('Some are mismatched - please try again:(')
                count = 0
                ans_chars = []


pygame.quit()
