import pygame

pygame.init()

# Game Window Dimensions
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

# Game Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

# Game Loop
while running:

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()