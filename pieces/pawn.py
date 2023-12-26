from pieces.piece import Piece

class Pawn(Piece):
  
  def __init__(self, team, position, image):
    super().__init__(team, position, image)
    self.has_moved = False

  def get_available_moves(self):
    return