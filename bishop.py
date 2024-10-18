from pieces import Piece
from moves import possible_positions_dar, possible_positions_dal, possible_positions_ddr, possible_positions_ddl,valid_positions_rook_and_bishop

class Bishop(Piece):
    white_str='♝'
    black_str='♗'

    # TOTAL VALID POSITIONS WHERE TO MOVE A BISHOP TO:

    def valid_positions(self,from_row,from_col):
        return valid_positions_rook_and_bishop(self,from_row,from_col)