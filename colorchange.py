import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click to Change Color")

# Define colors
colors = [(255, 0, 0),  # Red
          (0, 255, 0),  # Green
          (0, 0, 255)]  # Blue
color_index = 0

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change color on click
            color_index = (color_index + 1) % len(colors)
            screen.fill(colors[color_index])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()