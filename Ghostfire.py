import pygame
import random

from Ghost import Ghost

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

# ----------------- GAME LOOP -----------------

# Generate a list of ghosts
def create_ghosts(num_ghosts):
    # Initialize an empty list of Ghosts
    ghosts: list[Ghost] = []

    # Create the specified number of ghosts
    for _ in range(num_ghosts):
        # Randomly select x and y coordinates within the screen such that ghosts are not spawned too close to the sides and bottom
        x = random.randint(40, SCREEN_WIDTH - 40)
        y = random.randint(50, SCREEN_HEIGHT - 200)

        # Randomly choose speeds
        speed_x = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])
        speed_y = random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])

        # Randomly assign color (30% chance to be blue)
        color = 'Blue' if random.random() < 0.3 else 'Red'

        # Create ghost according to randomized parameters and append it to the list
        ghosts.append(Ghost(x, y, color, speed_x, speed_y))

    return ghosts

def main():
    running = True
    ghosts = create_ghosts(10)

    while running:
        # Clear the screen by filling it with black before drawing the new frame
        screen.fill('Black')

        # Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # 'X'/Close Window Button is Clicked
                running = False

        # Draw each ghost accordingly
        for ghost in ghosts:
            ghost.update(SCREEN_WIDTH, SCREEN_HEIGHT)
            ghost.draw(screen)

        # Ensure game window is always up to date
        pygame.display.update()

        # Set max frame rate of 60fps
        clock.tick(60)

    # Exit Game
    pygame.quit()

if __name__ == "__main__":
    main()