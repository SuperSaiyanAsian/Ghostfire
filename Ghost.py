import pygame

# Helper function to draw the ghost
def draw_ghost(surface, color, center, width = 40, height = 50):
    # Midpoint coordinates of the ghost
    x, y = center

    # Calculate the top-left (tl) corner coordinates of the bounding box for the ghost
    tl_x = x - width / 2
    tl_y = y - height / 2

    # List of points that outline the shape of the ghost (values are fractional multiples of the width and height, making the shape scaleable)
    points = [
        (tl_x, tl_y + height * 0.5),
        (tl_x + width * 0.2, tl_y),
        (tl_x + width * 0.8, tl_y),
        (tl_x + width, tl_y + height * 0.5),
        (tl_x + width * 0.9, tl_y + height * 0.85),
        (tl_x + width * 0.75, tl_y + height * 0.75),
        (tl_x + width * 0.60, tl_y + height),
        (tl_x + width * 0.50, tl_y + height * 0.8),
        (tl_x + width * 0.40, tl_y + height),
        (tl_x + width * 0.25, tl_y + height * 0.75),
        (tl_x + width * 0.10, tl_y + height * 0.85)
    ]

    # Draw the ghost shape on the specified surface using the defined color and points
    pygame.draw.polygon(surface, color, points)

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
