from pieces import Piece
from moves import possible_positions_dar, possible_positions_dal, possible_positions_ddr, possible_positions_ddl

class Bishop(Piece):
    white_str='♝'
    black_str='♗'

    # TOTAL VALID POSITIONS WHERE TO MOVE A BISHOP TO:

    def valid_positions(self,from_row,from_col):
        possible_positions=(possible_positions_dar(self,from_row, from_col)+possible_positions_dal(self,from_row, from_col)+possible_positions_ddr(self,from_row, from_col)+possible_positions_ddl(self,from_row, from_col))
        return possible_positions