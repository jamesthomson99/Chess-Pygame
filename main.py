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
board_width, board_height = BOARD_SIZE, BOARD_SIZE
smallest_board_dimension = np.min([board_width, board_height])
board_width, board_height = smallest_board_dimension, smallest_board_dimension
square_size = smallest_board_dimension / GRID_SIZE
screen = pygame.display.set_mode((board_width, board_height), pygame.RESIZABLE)
pygame.display.set_caption("Chess")


# Main game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.VIDEORESIZE:
      # Update window size when the window is resized
      board_width, board_height = pygame.display.get_surface().get_size()
      smallest_board_dimension = np.min([board_width, board_height])
      board_width, board_height = smallest_board_dimension, smallest_board_dimension
      square_size = smallest_board_dimension / GRID_SIZE
      screen = pygame.display.set_mode((board_width, board_height), pygame.RESIZABLE)

    # Draw the chessboard
    for row in range(GRID_SIZE):
      for col in range(GRID_SIZE):
        x = col * square_size
        y = row * square_size

        # Alternate colors for chessboard pattern
        color = CREAM if (row + col) % 2 == 0 else BROWN

        pygame.draw.rect(screen, color, (x, y, square_size, square_size))

    # Update the display
    pygame.display.flip()


pygame.quit()
