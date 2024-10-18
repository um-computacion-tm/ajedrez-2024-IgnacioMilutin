from pieces import Piece
from moves import possible_positions_vd,possible_positions_va, possible_positions_hr, possible_positions_hl,valid_positions_rook_and_bishop

class Rook(Piece):
    white_str='♜'
    black_str='♖'

    # TOTAL VALID POSITIONS WHERE TO MOVE A ROOK TO:
    
    def valid_positions(self,from_row,from_col):
      return valid_positions_rook_and_bishop(self,from_row,from_col)