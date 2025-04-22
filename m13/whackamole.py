#

import pygame
import random

# Constants
CELL_SIZE = 32
GRID_WIDTH = 20
GRID_HEIGHT = 16
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH  # 640
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT  # 512
LINE_COLOR = (0, 0, 0)  # Black grid lines

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-A-Mole")
        clock = pygame.time.Clock()

        # Load and scale the mole image
        mole_image = pygame.image.load("mole.png")
        mole_image = pygame.transform.scale(mole_image, (CELL_SIZE, CELL_SIZE))

        # Start the mole in the top-left corner
        mole_x = 0
        mole_y = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Check if the mole was clicked
                    if mole_x <= mouse_x < mole_x + CELL_SIZE and mole_y <= mouse_y < mole_y + CELL_SIZE:
                        # Move to a new random position
                        new_col = random.randrange(GRID_WIDTH)
                        new_row = random.randrange(GRID_HEIGHT)
                        mole_x = new_col * CELL_SIZE
                        mole_y = new_row * CELL_SIZE

            # Fill background
            screen.fill("light green")

            # Draw grid lines
            for x in range(0, SCREEN_WIDTH, CELL_SIZE):
                pygame.draw.line(screen, LINE_COLOR, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
                pygame.draw.line(screen, LINE_COLOR, (0, y), (SCREEN_WIDTH, y))

            # Draw the mole
            screen.blit(mole_image, (mole_x, mole_y))

            # Update display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
