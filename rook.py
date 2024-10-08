from pieces import Piece

class Rook(Piece):
    white_str='♜'
    black_str='♖'

    # TOTAL VALID POSITIONS WHERE TO MOVE A ROOK TO:

    def valid_positions(self,from_row,from_col):
        possible_positions=(self.possible_positions_vd(from_row, from_col)+self.possible_positions_va(from_row, from_col)+self.possible_positions_hr(from_row, from_col)+self.possible_positions_hl(from_row, from_col))
        return possible_positions
    
    # CHECKS IF TO_ROW AND TO_COL ARE IN POSSIBEL POSITIONS:

    def is_row_col_in_valid_postions(self,to_row,to_col,possible_positions):
        if (to_row,to_col) in possible_positions:
            return True
        else: False
        
    # POSSIBLE VERTICAL DESCENDANT POSITIONS TO MOVE A ROOK TO:

    def possible_positions_vd(self,row,col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))  
                break  
            else:
                possibles.append((next_row, col))  
        return possibles

    # POSSIBLE VERTICAL ASCENDANT POSITIONS TO MOVE A ROOK TO:

    def possible_positions_va(self,row,col):
        possibles=[]
        for next_row in range(row-1,-1,-1):
            other_piece = self.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((next_row, col))  
                break  
            else:possibles.append((next_row,col))
        return possibles

    # POSSIBLE HORIZONTAL RIGHT POSITIONS TO MOVE A ROOK TO:

    def possible_positions_hr(self,row,col):
        possibles=[]
        for next_col in range(col + 1, 8):
            other_piece = self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row,next_col))  
                break  
            else:possibles.append((row,next_col))
        return possibles

    # POSSIBLE HORIZONTAL LEFT POSITIONS TO MOVE A ROOK TO:

    def possible_positions_hl(self,row,col):
        possibles=[]
        for next_col in range(col-1,-1,-1):
            other_piece = self.__board__.get_piece(row,next_col)
            if other_piece is not None:
                if other_piece.__color__ != self.__color__:
                    possibles.append((row,next_col))  
                break  
            else:possibles.append((row,next_col))
        return possibles