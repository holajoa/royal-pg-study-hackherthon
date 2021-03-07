<<<<<<< HEAD
import pygame
import os


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

# list of categories
CATS = ['Hazardous waste',
        'Recyclable waste',
        'Food waste',
        'Residual waste']

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
        start = pygame.image.load(os.path.join('buttons', '1.png'))
        but = Button(start, (40, 320), (220, 160), choose_game)
        but.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            # button event
            but.event_handler(event)

        pygame.display.update()
        clock.tick(15)


def button(image,x,y,action=None):
    click = pygame.mouse.get_pressed()
    print(click)
    w, h = image.get_rect().size        

    win.blit(image, (x, y))

    if x+w > click[0] > x and y+h > click[1] > y:
         if action != None:
            action() 

def choose_game():
    draw()
    CHOICE = 'Which Game Do You Want To Play?'
    win.blit(ques_font.render(CHOICE, 1, BLACK), (100, 295))
    pygame.display.flip()

def questions(i):
    draw()
    ques = ques_font.render(QUES[i], 1, BLACK)
    win.blit(ques, (100, 295))
    pygame.display.flip()

game_intro()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False

    choose_game()

pygame.quit()
=======
import pygame
import os


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

# list of categories
CATS = ['Hazardous waste',
        'Recyclable waste',
        'Food waste',
        'Residual waste']

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
        start = pygame.image.load(os.path.join('buttons', '1.png'))
        but = Button(start, (40, 320), (220, 160), choose_game)
        but.draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            # button event
            but.event_handler(event)

        pygame.display.update()
        clock.tick(15)


def button(image,x,y,action=None):
    click = pygame.mouse.get_pressed()
    print(click)
    w, h = image.get_rect().size        

    win.blit(image, (x, y))

    if x+w > click[0] > x and y+h > click[1] > y:
         if action != None:
            action() 

def choose_game():
    draw()
    CHOICE = 'Which Game Do You Want To Play?'
    win.blit(ques_font.render(CHOICE, 1, BLACK), (100, 295))
    pygame.display.flip()

def questions(i):
    draw()
    ques = ques_font.render(QUES[i], 1, BLACK)
    win.blit(ques, (100, 295))
    pygame.display.flip()

game_intro()
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False

    
    choose_game()
pygame.quit()
>>>>>>> f4d94a85ead5bcdec56a903623f5ec91849e0faa
