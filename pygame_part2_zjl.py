import pygame
import os
import math

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Waste categorization game')

# button
NUM = 8
im_size = (90, 90)
im_size_big = (110, 110)
startx = 100
starty_b = 70
starty_w = 300
starty2 = 300
gap = 90  # each bin 45 width
x_co = [startx + i*gap*2 for i in range(4)] + [startx + i*gap*2 for i in range(4)]
y_co = [starty_b] * 4 + [starty_w] * 4

# font
# FONT = pygame.font.SysFont('comicsans', 14)
# text = FONT.render('xx', 1, BLACK)

# images 100-190, 280-370, 460-550, 640-730, 730~
WHITE = (255,255,255)
BLACK = (0,0,0)
image_lst = []  # Surface(color, size)

def draw1(x_co, i):
    # 点击垃圾桶后图片变大
    if i < 4:
        pic_name = f'bin{i}.png'
    else:
        pic_name = f'waste{i-4}.png'
    image1 = pygame.image.load(pic_name)
    image1 = pygame.transform.scale(image1, im_size_big)
    y_co = (starty_b-10) if i < 4 else (starty_w-10)
    win.blit(image1, (x_co[i]-10, y_co))
    pygame.display.update()

def draw2(x_co):
    # win.fill(WHITE)
    
    for i in range(int(NUM/2)):
        image1 = pygame.image.load(f'bin{i+1}.png')
        image1 = pygame.transform.scale(image1, im_size)
        image_lst.append(image1)
        win.blit(image1, (x_co[i], starty_b))
    # pygame.draw.line(win, BLACK, (0,0), (100,100))  # line(surface, color, start_pos, end_pos, width=1)
    for i in range(int(NUM/2)):
        image1 = pygame.image.load(f'waste{i+1}.png')
        image1 = pygame.transform.scale(image1, im_size)
        image_lst.append(image1)
        win.blit(image1, (x_co[i], starty_w))

    pygame.display.update()


status = 0
# clock
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)

    # bg image
    win.fill(WHITE)
    image1 = pygame.image.load('icl.jpg')
    image1 = pygame.transform.scale(image1, (WIDTH, HEIGHT))
    win.blit(image1, (0, 0))  # fill image
    draw2(x_co)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for i in range(NUM):
                dis = math.sqrt((m_x - x_co[i])**2 + (m_y - y_co[i])**2)
                if (dis < im_size[0]) & (m_x >= x_co[i]) & (m_y >= y_co[i]):
                    status = 1
                    print('yes')
                    draw2(x_co)
                    draw1(x_co, i)
                # elif status % 2 == 1:
                #     draw1(x_co, i)
                else: 
                    draw2(x_co)


pygame.quit()