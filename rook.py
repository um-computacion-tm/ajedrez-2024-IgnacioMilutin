from pieces import Piece
from moves import possible_positions_vd,possible_positions_va, possible_positions_hr, possible_positions_hl

class Rook(Piece):
    white_str='♜'
    black_str='♖'

    # TOTAL VALID POSITIONS WHERE TO MOVE A ROOK TO:

    def valid_positions(self,from_row,from_col):
        possible_positions=(possible_positions_vd(self,from_row, from_col)+possible_positions_va(self,from_row, from_col)+possible_positions_hr(self,from_row, from_col)+possible_positions_hl(self,from_row, from_col))
        return possible_positions