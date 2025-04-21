import pygame
import math

# Bullet class defining a bullet's movement, drawing, and destruction
class Bullet:
    # Initialize new Bullet instances
    def __init__(self, x, y, target_x, target_y, speed = 10, radius = 5):
        angle = math.atan2(target_y - y, target_x - x)

        self.x = x
        self.y = y
        self.speed_x = speed * math.cos(angle)
        self.speed_y = speed * math.sin(angle)
        self.radius = radius

    # Move the bullet
    def update(self):
        # Increment the bullet's position by the respective speeds
        self.x += self.speed_x
        self.y += self.speed_y

    # Draw the bullet (white circle) on a given surface
    def draw(self, surface):
        pygame.draw.circle(surface, 'White', (self.x, self.y), self.radius)

    # Check if bullet is outside the game window, destroying it if so
    def is_outside(self, width, height):
        return self.x < 0 or self.x > width or self.y < 0 or self.y > height
