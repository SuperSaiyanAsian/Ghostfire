import pygame

# Initialize Game
pygame.init()
clock = pygame.time.Clock()

# Game Window Dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Title
pygame.display.set_caption('Ghostfire')

# Game Loop
running = True

while running:

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 'X'/Close Window Button is Clicked
            running = False

    # Ensure game window is always up to date
    pygame.display.update()

    # Set max frame rate of 60fps
    clock.tick(60)

# Exit Game
pygame.quit()