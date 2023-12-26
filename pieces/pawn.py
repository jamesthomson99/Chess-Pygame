from pieces.piece import Piece

class Pawn(Piece):
  
  def __init__(self):
    self.has_moved = False

  def get_available_moves(self):
    return