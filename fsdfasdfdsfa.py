import sys
import random
import time
import pygame
# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Play Button Example")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 74)

# Create a text surface for the button
play_text = font.render('Play', True, black)
play_rect = play_text.get_rect(center=(screen_width // 2, screen_height // 2))

def game_loop():
    # The game loop would go here
    print("Game started!")

def main_menu():
    while True:
        screen.fill(white)

        # Draw the play button
        pygame.draw.rect(screen, green, play_rect.inflate(20, 20))
        screen.blit(play_text, play_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    game_loop()

        # Update the display
        pygame.display.flip()

# Run the main menu
main_menu()