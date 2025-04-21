import pygame

# Draw a ghost
def draw_ghost(surface, color, center, width = 40, height = 50):
    # Midpoint coordinates of the ghost
    x, y = center

    # Determine dimensions for the ghost
    head_radius = width / 2             # Radius is half the width so the head covers the full width of the ghost
    head_center = (x, y - height / 4)   # Center of the head
    base_bottom = y + height / 4        # Base y-coordinate for the bottom of the ghost
    spike_depth = height / 6            # How deep the body spikes go

    # Draw the head using a circle
    pygame.draw.circle(surface, color, head_center, head_radius)

    # The body starts at the left head point, 
    # moves through a series of points to create a spiky bottom,
    # then goes back up to the right head point
    body_points = [
        (x - head_radius, head_center[1]),                      # Left of head
        (x - head_radius * 0.8, base_bottom + spike_depth),     # Down
        (x - head_radius * 0.6, base_bottom - spike_depth),     # Up
        (x - head_radius * 0.4, base_bottom + spike_depth),     # Down
        (x - head_radius * 0.2, base_bottom - spike_depth),     # Up
        (x, base_bottom + spike_depth),                         # Down (Center)
        (x + head_radius * 0.2, base_bottom - spike_depth),     # Up
        (x + head_radius * 0.4, base_bottom + spike_depth),     # Down
        (x + head_radius * 0.6, base_bottom - spike_depth),     # Up
        (x + head_radius * 0.8, base_bottom + spike_depth),     # Down
        (x + head_radius, head_center[1])                       # Right of head
    ]

    # Draw the body using a polygon
    pygame.draw.polygon(surface, color, body_points)

# Ghost class representing an individual ghost with movement, drawing, and collision behaviors
class Ghost:
    # Initializes new Ghost instances
    def __init__(self, x, y, color, speed_x, speed_y, width = 40, height = 50):
        self.x = x
        self.y = y
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.width = width
        self.height = height

    # Adjust ghost's position and handle bouncing off screen edges
    def update(self, screen_width, screen_height):
        # Increment the ghost’s position by the respective speeds
        self.x += self.speed_x
        self.y += self.speed_y

        # Check if the ghost’s bounding box touches the left or right edges of the screen, reversing speed accordingly to bounce
        if self.x - self.width/2 <= 0 or self.x + self.width/2 >= screen_width:
            self.speed_x = -self.speed_x
        if self.y - self.height/2 <= 0 or self.y + self.height/2 >= screen_height:
            self.speed_y = -self.speed_y

    # Render the ghost on the given surface using its current position, color, and size
    def draw(self, surface):
        draw_ghost(surface, self.color, (self.x, self.y), self.width, self.height)

    # Check if a given point is inside the ghost’s area to determine a hit
    def is_hit(self, point):
        # Rectangular region (rect) that approximates the ghost’s shape based on its center and dimensions
        rect = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)

        # Check if the given point is within the rectangle
        return rect.collidepoint(point)
