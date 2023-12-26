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


def create_board():
  # Create empty board
  board = [[None] * GRID_SIZE for i in range(GRID_SIZE)]
  print(board)
  
  # Create pawns
  for i in range(GRID_SIZE):
    board[i][1] = Pawn('black', (1, i), None)
    board[i][GRID_SIZE - 2] = Pawn('white', (GRID_SIZE - 2, i), None)

  # Create rooks
  board[0][0] = Rook('black', (0, 0), None)
  board[GRID_SIZE - 1][0] = Rook('black', (0, GRID_SIZE - 1), None)
  board[0][GRID_SIZE - 1] = Rook('white', (GRID_SIZE - 1, 0), None)
  board[GRID_SIZE - 1][GRID_SIZE - 1] = Rook('white', (GRID_SIZE - 1, GRID_SIZE - 1), None)

  # Create knights
  board[1][0] = Knight('black', (0, 1), None)
  board[GRID_SIZE - 2][0] = Knight('black', (0, GRID_SIZE - 2), None)
  board[1][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, 1), None)
  board[GRID_SIZE - 2][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, GRID_SIZE - 2), None)

  # Create knights
  board[2][0] = Knight('black', (0, 2), None)
  board[GRID_SIZE - 3][0] = Knight('black', (0, GRID_SIZE - 3), None)
  board[2][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, 2), None)
  board[GRID_SIZE - 3][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, GRID_SIZE - 3), None)

  # Create bishops
  board[3][0] = Knight('black', (0, 3), None)
  board[GRID_SIZE - 4][0] = Knight('black', (0, GRID_SIZE - 4), None)
  board[3][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, 3), None)
  board[GRID_SIZE - 4][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, GRID_SIZE - 4), None)

  # Create queens
  board[4][0] = Knight('black', (0, 4), None)
  board[4][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, 4), None)

  # Create kings
  board[5][0] = Knight('black', (0, 5), None)
  board[5][GRID_SIZE - 1] = Knight('white', (GRID_SIZE - 1, 5), None)

  return board


def draw_pieces(screen, board):
  for row_index in range(len(board)):
    for col_index in range(len(board[0])):
      if board[row_index][col_index]:
        piece_color = WHITE if board[row_index][col_index].team == 'white' else BLACK
        pygame.draw.rect(screen, piece_color, (row_index * SQUARE_SIZE, col_index * SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE / 2))


pygame.init()

# Set image as icon 
icon = pygame.image.load('images/icon_small.png') 
pygame.display.set_icon(icon)

# Create the Pygame window
screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
pygame.display.set_caption("Chess")

# Create board
board = create_board()

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
        square_color = CREAM if (row + col) % 2 == 0 else BROWN
        pygame.draw.rect(screen, square_color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    draw_pieces(screen, board)

    # Update the display
    pygame.display.flip()


pygame.quit()



  