

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
        # For now, just clear the board. We'll place pieces next.
        self.squares = [self.EMPTY] * 64

    def __str__(self) -> str:
        lines = []
        for row in range(8):
            start = row * 8
            end = start + 8
            rank_num = 8 - row
            lines.append(f"{rank_num}  " + " ".join(self.squares[start:end]))
        lines.append("   a b c d e f g h")
        lines.append(f"Turn: {'White' if self.turn == 'w' else 'Black'}")
        return "\n".join(lines)


