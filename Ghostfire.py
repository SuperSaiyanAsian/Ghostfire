import pygame
import random
import math

from Ghost import Ghost
from Bullet import Bullet
from Gun import Gun

# Initialize Game
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Load background music and start playing it
pygame.mixer.music.load("BGM.mp3")                      # https://opengameart.org/content/cyberpunk-moonlight-sonata
pygame.mixer.music.play(-1)                             # Play indefinitely

# Load sound effects
gunshot_sound = pygame.mixer.Sound("Gunshot.wav")       # https://opengameart.org/content/shots
win_sound = pygame.mixer.Sound("Win.ogg")               # https://opengameart.org/content/new-thing-get
lose_sound = pygame.mixer.Sound("Lose.wav")             # https://opengameart.org/content/game-over-bad-chest-sfx

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

        # Ensure at least one ghost is blue
        if not ghosts:
            color = 'Blue'

        # Create ghost according to randomized parameters and append it to the list
        ghosts.append(Ghost(x, y, color, speed_x, speed_y))

    return ghosts

def main():
    running = True
    victory = False
    defeat = False

    ghost_amount = 10
    ghosts = create_ghosts(ghost_amount)

    bullets: list[Bullet] = []

    gun_pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 20)
    gun_length = 50
    gun = Gun(gun_pos, gun_length)

    # Set font for victory/defeat message
    font = pygame.font.Font(None, 80)

    # Flag to check that music has been stopped
    music_stopped = False

    while running:
        # Clear the screen by filling it with black before drawing the new frame
        screen.fill('Black')

        # Get mouse position (used for aiming the gun)
        mouse_pos = pygame.mouse.get_pos()

        # Draw the gun and get its angle
        gun_angle = gun.draw(screen, mouse_pos)  

        # Event Handler
        for event in pygame.event.get():
            # 'X'/Close Window Button is Clicked
            if event.type == pygame.QUIT:
                running = False

            #  Mouse button is clicked
            elif event.type == pygame.MOUSEBUTTONDOWN and not victory and not defeat:
                # Play gunshot sound
                gunshot_sound.play()

                # Calculate bullet's starting position
                bullet_start_x = gun_pos[0] + gun.barrel_length * math.cos(gun_angle)
                bullet_start_y = gun_pos[1] + gun.barrel_length * math.sin(gun_angle)

                # Create a bullet that targets the current mouse position
                new_bullet = Bullet(bullet_start_x, bullet_start_y, mouse_pos[0], mouse_pos[1])

                # Append the new bullet to the list
                bullets.append(new_bullet)


        # Draw ghosts accordingly
        for ghost in ghosts:
            if not victory and not defeat: 
                ghost.update(SCREEN_WIDTH, SCREEN_HEIGHT)
            
            ghost.draw(screen)

        # Draw bullets accordingly
        for bullet in bullets:
            bullet.update()
            bullet.draw(screen)

            # Destroy bullets outside the screen
            if bullet.is_outside(SCREEN_WIDTH, SCREEN_HEIGHT):
                bullets.remove(bullet)
            else:
                for ghost in ghosts:
                    # Destroy ghost if hit
                    if ghost.is_hit((bullet.x, bullet.y)):
                        # If a blue ghost was hit, then the player loses
                        if ghost.color == 'Blue': 
                            defeat = True
                        
                        # Destroy ghost
                        ghosts.remove(ghost)

                        # Destroy the bullet that hit the ghost
                        if bullet in bullets:
                            bullets.remove(bullet)
                        break

        # Player wins when there are no more blue ghosts and a blue ghost has never been hit
        if not any(ghost.color != 'Blue' for ghost in ghosts) and not defeat:
            victory = True

        # Display victory or defeat message
        if defeat:
            if not music_stopped:
                # Stop background music
                pygame.mixer.music.stop()

                # Play defeat sound
                lose_sound.play()
                music_stopped = True

            # Display defeat message
            text = font.render("Game Over...", True, 'Red')
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 2))
        elif victory:
            if not music_stopped:
                # Stop background music
                pygame.mixer.music.stop()

                # Play victory sound
                win_sound.play()
                music_stopped = True

            # Display victory message
            text = font.render("You Won!", True, 'White')
            screen.blit(text, ((SCREEN_WIDTH - text.get_width()) / 2, (SCREEN_HEIGHT - text.get_height()) / 2))

        # Ensure game window is always up to date
        pygame.display.update()

        # Set max frame rate of 60fps
        clock.tick(60)

    # Exit Game
    pygame.quit()

if __name__ == "__main__":
    main()