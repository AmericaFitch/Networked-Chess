class Board:
    Empty = NONE
    def __init__(self):
        self.reset()

    def reset(self):
        self.squares = [self.EMPTY] * 64
        self.turn = "w"
        self.move_history = []
        self.setup_start_position()

    def _setup_start_psotion(self):

    
