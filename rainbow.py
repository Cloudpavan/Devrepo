import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Click to Change Rainbow Color")

# Define colors
rainbow_colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0),
                  (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]  # Rainbow colors

# Main loop
running = True
color_index = 0
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Change color on click
            color_index = (color_index + 1) % len(rainbow_colors)
            screen.fill(rainbow_colors[color_index])

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
