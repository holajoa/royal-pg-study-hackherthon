import pygame
# import pygame_menu
import os
import pygame_part2


# --- class ---

class Button(object):

    def __init__(self, image, position, size, action=None):

        # create images
        self._images = pygame.transform.scale(image, size)

        # get image size and position
        size = self._images.get_rect().size
        self._rect = pygame.Rect(position, size)
        self._position = position

        self.action = action

    def draw(self, screen):

        # draw selected image
        screen.blit(self._images, self._position)

    def event_handler(self, event):
        # perform action if button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
            if event.button == 1:  # is left button clicked
                if self._rect.collidepoint(event.pos):  # is mouse over button
                    return self.action()
# --- main ---

# setup display

pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The RUBBISH Game")


# load images
TP = pygame.transform.scale(pygame.image.load("titlepage.png"),
    (800, 500))
BG = pygame.transform.scale(pygame.image.load("bg.png"),
    (800, 500))

# list of questions
QUES = ['Is it a Hazardous waste?',
        'Is it Recyclable?',
        'Is it a Food waste?']

# font
ques_font = pygame.font.SysFont("monospace", 24)

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True


def draw():
    # draw the background
    win.blit(BG, (0, 0))

    pygame.display.update()


def game_intro():
    # intro of the game
    intro = True

    while intro:
        # draw titlepage
        win.blit(TP, (0, 0))

        # draw button
        start = pygame.image.load(os.path.join('button', '1.png'))
        but = Button(start, (40, 320), (220, 160), choose_game)
        but.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        
            # button event
            but.event_handler(event)

        pygame.display.update()
        clock.tick(15)
        pass


def button(image,x,y,action=None):
    click = pygame.mouse.get_pressed()
    print(click)
    w, h = image.get_rect().size 

    win.blit(image, (x, y))

    if x+w > click[0] > x and y+h > click[1] > y:
        if action != None:
            action()

def choose_game():
    choose = True
    while choose:
        draw()
        CHOICE = 'Which Game Do You Want To Play?'
        win.blit(ques_font.render(CHOICE, 1, BLACK), (100, 295))

        # draw buttons
        ONE = pygame.image.load(os.path.join('button', '4.png'))
        one = Button(ONE, (80, 320), (220, 160), question1)

        TWO = pygame.image.load(os.path.join('button', '5.png'))
        two = Button(TWO, (310, 320), (220, 160), part2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # button event
            one.event_handler(event)
            two.event_handler(event)
        one.draw(win)
        two.draw(win)

        pygame.display.update()
        clock.tick(30)
        pass

def part2():
    pygame_part2.main()

def question1():
    ques1 = True
    while ques1:
        draw()
        ques1 = ques_font.render(QUES[0], 1, BLACK)
        win.blit(ques1, (100, 295))

        # draw buttons
        YES = pygame.image.load(os.path.join('button', '2.png'))
        yes = Button(YES, (40, 320), (220, 160), result1)
        yes.draw(win)

        NO = pygame.image.load(os.path.join('button', '3.png'))
        no = Button(NO, (200, 320), (220, 160), question2)
        no.draw(win)

        HELP = pygame.image.load(os.path.join('button', '6.png'))
        h = Button(HELP, (380, 320), (220, 160), help1)
        h.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # button event
            yes.event_handler(event)
            no.event_handler(event)
            h.event_handler(event)

        pygame.display.update()
        clock.tick(FPS)
        pass

def question2():
    ques2 = True
    while ques2:
        draw()
        ques2 = ques_font.render(QUES[1], 1, BLACK)
        win.blit(ques2, (100, 295))

        # draw buttons
        YES = pygame.image.load(os.path.join('button', '2.png'))
        yes = Button(YES, (40, 320), (220, 160), result2)
        yes.draw(win)

        NO = pygame.image.load(os.path.join('button', '3.png'))
        no = Button(NO, (200, 320), (220, 160), question3)
        no.draw(win)

        HELP = pygame.image.load(os.path.join('button', '6.png'))
        h = Button(HELP, (380, 320), (220, 160), help2)
        h.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # button event
            yes.event_handler(event)
            no.event_handler(event)
            h.event_handler(event)

        pygame.display.update()
        clock.tick(FPS)
        pass

def question3():
    ques3 = True
    while ques3:
        draw()
        ques3 = ques_font.render(QUES[2], 1, BLACK)
        win.blit(ques3, (100, 295))

        # draw buttons
        YES = pygame.image.load(os.path.join('button', '2.png'))
        yes = Button(YES, (40, 320), (220, 160), result3)
        yes.draw(win)

        NO = pygame.image.load(os.path.join('button', '3.png'))
        no = Button(NO, (200, 320), (220, 160), result4)
        no.draw(win)

        HELP = pygame.image.load(os.path.join('button', '6.png'))
        h = Button(HELP, (380, 320), (220, 160), help3)
        h.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # button event
            yes.event_handler(event)
            no.event_handler(event)
            h.event_handler(event)

        pygame.display.update()
        clock.tick(FPS)
        pass


def result1():
    r1 = True
    while r1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        res1 = pygame.image.load(os.path.join('waste_ppt', 'rubbish1.png'))
        res1 = pygame.transform.scale(res1, (800, 500))
        win.blit(res1, (0, 0))
        pygame.display.update()

def result2():
    r2 = True
    while r2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        res2 = pygame.image.load(os.path.join('waste_ppt', 'rubbish2.png'))
        res2 = pygame.transform.scale(res2, (800, 500))
        win.blit(res2, (0, 0))
        pygame.display.update()

def result3():
    r3 = True
    while r3:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        res3 = pygame.image.load(os.path.join('waste_ppt', 'rubbish3.png'))
        res3 = pygame.transform.scale(res3, (800, 500))
        win.blit(res3, (0, 0))
        pygame.display.update()

def result4():
    r4 = True
    while r4:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        res4 = pygame.image.load(os.path.join('waste_ppt', 'rubbish4.png'))
        res4 = pygame.transform.scale(res4, (800, 500))
        win.blit(res4, (0, 0))
        pygame.display.update()

def help1():
    h1 = True
    while h1:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        help1 = pygame.image.load(os.path.join('waste_ppt', 'hazardous_waste.png'))
        help1 = pygame.transform.scale(help1, (800, 500))
        win.blit(help1, (0, 0))
        pygame.display.update()

def help2():
    h2 = True
    while h2:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        help2 = pygame.image.load(os.path.join('waste_ppt', 'recyclable_wast.png'))
        help2 = pygame.transform.scale(help2, (800, 500))
        win.blit(help2, (0, 0))
        pygame.display.update()
    
def help3():
    h3 = True
    while h3:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        help3 = pygame.image.load(os.path.join('waste_ppt', 'household_food_waste.png'))
        help3 = pygame.transform.scale(help3, (800, 500))
        win.blit(help3, (0, 0))
        pygame.display.update()

def help4():
    h4 = True
    while h4:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

        help4 = pygame.image.load(os.path.join('waste_ppt', 'residual_waste.png'))
        help4 = pygame.transform.scale(help4, (800, 500))
        win.blit(hel4, (0, 0))
        pygame.display.update()

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False

    game_intro()
    choose_game()
pygame.quit()
