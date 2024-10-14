from pieces import Piece
from moves import possible_positions_dal, possible_positions_dar, possible_positions_ddl, possible_positions_ddr, possible_positions_hl, possible_positions_hr, possible_positions_va, possible_positions_vd

class Queen(Piece):
    white_str='♛'
    black_str='♕'
    
    # TOTAL VALID POSITIONS WHERE TO MOVE A QUEEN TO:

    def valid_positions(self,from_row,from_col):
        possible_positions=(possible_positions_vd(self,from_row, from_col)+possible_positions_va(self,from_row, from_col)+possible_positions_hr(self,from_row, from_col)+possible_positions_hl(self,from_row, from_col)+possible_positions_dar(self,from_row, from_col)+possible_positions_dal(self,from_row, from_col)+possible_positions_ddr(self,from_row, from_col)+possible_positions_ddl(self,from_row, from_col))
        return possible_positions