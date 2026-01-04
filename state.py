
class Board:
        """A minimal chess board state.

    Representation:
      - 64-square 1D array, index = row*8 + col
      - row 0 is rank 8 (Black's back rank), row 7 is rank 1 (White's back rank)
      - pieces are single-character codes:
          White: P N B R Q K
          Black: p n b r q k
          Empty: .
    """

    EMPTY = "."

    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = [self.EMPTY] * 64
        self.turn = "w"
        self.move_history = []

     self.setup_start_position()

    def setup_start_position(self):
        self.squares = [self.EMPTY] * 64

    
