from pieces.piece import Piece

class Bishop(Piece):

  def __init__(self, team, position, image):
    super().__init__(team, position, image)

  def get_available_moves(self):
    return