from pieces import Piece

class Knight(Piece):
    white_str='♞'
    black_str='♘'

    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_var_and_hra(from_row, from_col)+self.possible_positions_val_and_hla(from_row, from_col)+self.possible_positions_vdr_and_hrd(from_row, from_col)+self.possible_positions_vdl_and_hld(from_row, from_col)
        return possible_positions
    
    # CHECKS AND UPDATES STATE OF THE NEXT MOVE FOR VERTICAL DESCENDANT TO THE RIGHT AND HORIZONTAL RIGHT AND DESCENDANT
    
    def process_move_vdr_and_hrd(self, row, col, row_to_add, col_to_add, possibles):
        new_row, new_col = row + row_to_add, col + col_to_add
        if not (0 <= new_row <= 7 and 0 <= new_col <= 7): 
            return
        other_piece = self.__board__.get_piece(new_row, new_col)
        if other_piece is None or other_piece.__color__ != self.__color__: 
            possibles.append((new_row, new_col))

    # CALCULATES VERTICAL DESCENDANT TO THE RIGHT AND HORIZONTAL RIGHT AND DESCENDANT MOVES

    def possible_positions_vdr_and_hrd(self, row, col):
        possibles = []
        rows_and_cols_to_add = [(2, 1), (1, 2)]
        for row_to_add, col_to_add in rows_and_cols_to_add:
            self.process_move_vdr_and_hrd(row, col, row_to_add, col_to_add, possibles)
        return possibles
    
    # CALCULATES VERTICAL DESCENDANT TO THE LEFT AND HORIZONTAL LEFT AND DESCENDANT MOVES

    def possible_positions_vdl_and_hld(self,row,col):
        possibles=[]
        rows_and_cols_to_add_and_sub=[(2,1),(1,2)]
        for row_to_add,col_to_sub in rows_and_cols_to_add_and_sub:
            new_row,new_col=row+row_to_add, col-col_to_sub
            if new_row>7 or new_col<0:
                continue
            other_piece=self.__board__.get_piece(row+row_to_add,col-col_to_sub)
            if other_piece is None or other_piece.__color__!=self.__color__:
                possibles.append((row+row_to_add,col-col_to_sub))
        return possibles
    
    # CALCULATES VERTICAL ASCENDANT TO THE LEFT AND HORIZONTAL LEFT AND ASCENDANT MOVES

    def possible_positions_val_and_hla(self,row,col):
        possibles=[]
        rows_and_cols_to_sub=[(2,1),(1,2)]
        for row_to_sub,col_to_sub in rows_and_cols_to_sub:
            new_row,new_col=row-row_to_sub, col-col_to_sub
            if new_row<0 or new_col<0:
                continue
            other_piece=self.__board__.get_piece(row-row_to_sub,col-col_to_sub)
            if other_piece is None or other_piece.__color__!=self.__color__:
                possibles.append((row-row_to_sub,col-col_to_sub))
        return possibles
    
    # CALCULATES VERTICAL ASCENDANT TO THE RIGHT AND HORIZONTAL RIGHT AND ASCENDANT MOVES

    def possible_positions_var_and_hra(self,row,col):
        possibles=[]
        rows_and_cols_to_sub_and_add=[(2,1),(1,2)]
        for row_to_sub,col_to_add in rows_and_cols_to_sub_and_add:
            new_row,new_col=row-row_to_sub, col+col_to_add
            if new_row<0 or new_col>7:
                continue
            other_piece=self.__board__.get_piece(row-row_to_sub,col+col_to_add)
            if other_piece is None or other_piece.__color__!=self.__color__:
                possibles.append((row-row_to_sub,col+col_to_add))
        return possibles
