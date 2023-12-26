import pygame
import sys
import numpy as np

from pieces.piece import Piece
from pieces.pawn import Pawn
from pieces.rook import Rook
from pieces.knight import Knight 
from pieces.bishop import Bishop
from pieces.queen import Queen
from pieces.king import King
from constants import *

pygame.init()

# Set image as icon 
icon = pygame.image.load('images/icon_small.png') 
pygame.display.set_icon(icon)

# Create the Pygame window
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess")

# Main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # Draw the chessboard
    for row in range(GRID_SIZE):
      for col in range(GRID_SIZE):
        x = col * SQUARE_SIZE
        y = row * SQUARE_SIZE

        # Alternate colors for chessboard pattern
        color = CREAM if (row + col) % 2 == 0 else BROWN

        pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    # Update the display
    pygame.display.flip()


pygame.quit()
