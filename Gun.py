import pygame
import math

# Gun class defining the gun's drawing
class Gun:
    # Initialize new Gun instances
    def __init__(self, base_pos, barrel_length = 50):
        self.base_pos = base_pos
        self.barrel_length = barrel_length

    # Draw the gun and calculate its angle based on the current mouse position
    def draw(self, surface, mouse_pos):
        # Calculate the angle from the gun’s base to the mouse position
        angle = math.atan2(mouse_pos[1] - self.base_pos[1], mouse_pos[0] - self.base_pos[0])

        # Calculate the tip of the gun by extending a line from its base by barrel_length in the direction of the calculated angle
        tip_x = self.base_pos[0] + self.barrel_length * math.cos(angle)
        tip_y = self.base_pos[1] + self.barrel_length * math.sin(angle)

        # Draw the gun's base (white circle)
        pygame.draw.circle(surface, 'White', self.base_pos, 10)

        # Draw the gun's barrel (white line)
        pygame.draw.line(surface, 'White', self.base_pos, (tip_x, tip_y), 9)

        # Return the angle so it can be used when firing bullets
        return angle  
