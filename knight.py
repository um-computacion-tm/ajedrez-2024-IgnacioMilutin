from pieces import Piece

class Knight(Piece):
    white_str='♞'
    black_str='♘'

    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_var_and_hra(from_row, from_col)+self.possible_positions_val_and_hla(from_row, from_col)+self.possible_positions_vdr_and_hrd(from_row, from_col)+self.possible_positions_vdl_and_hld(from_row, from_col)
        return possible_positions
    
    # VERTICAL DESCENDANT TO THE RIGHT AND HORIZONTAL RIGHT AND DESCENDANT MOVES

    def possible_positions_vdr_and_hrd(self,row,col):
        possibles=[]
        rows_and_cols_to_sum=[(2,1),(1,2)]
        for row_to_sum,col_to_sum in rows_and_cols_to_sum:
            if row+row_to_sum>7 or col+col_to_sum>7:
                continue
            other_piece=self.__board__.get_piece(row+row_to_sum,col+col_to_sum)
            if other_piece is None:
                possibles.append((row+row_to_sum,col+col_to_sum))
            elif other_piece.__color__!=self.__color__:
                possibles.append((row+row_to_sum,col+col_to_sum))
        return possibles
    
    # VERTICAL DESCENDANT TO THE LEFT AND HORIZONTAL LEFT AND DESCENDANT MOVES

    def possible_positions_vdl_and_hld(self,row,col):
        possibles=[]
        rows_and_cols_to_sum=[(2,1),(1,2)]
        for row_to_sum,col_to_sum in rows_and_cols_to_sum:
            if row+row_to_sum>7 or col-col_to_sum<0:
                continue
            other_piece=self.__board__.get_piece(row+row_to_sum,col-col_to_sum)
            if other_piece is None:
                possibles.append((row+row_to_sum,col-col_to_sum))
            elif other_piece.__color__!=self.__color__:
                possibles.append((row+row_to_sum,col-col_to_sum))
        return possibles
    
    # VERTICAL ASCENDANT TO THE LEFT AND HORIZONTAL LEFT AND ASCENDANT MOVES

    def possible_positions_val_and_hla(self,row,col):
        possibles=[]
        rows_and_cols_to_sum=[(2,1),(1,2)]
        for row_to_sum,col_to_sum in rows_and_cols_to_sum:
            if row-row_to_sum<0 or col-col_to_sum<0:
                continue
            other_piece=self.__board__.get_piece(row-row_to_sum,col-col_to_sum)
            if other_piece is None:
                possibles.append((row-row_to_sum,col-col_to_sum))
            elif other_piece.__color__!=self.__color__:
                possibles.append((row-row_to_sum,col-col_to_sum))
        return possibles
    
    # VERTICAL ASCENDANT TO THE RIGHT AND HORIZONTAL RIGHT AND ASCENDANT MOVES

    def possible_positions_var_and_hra(self,row,col):
        possibles=[]
        rows_and_cols_to_sum=[(2,1),(1,2)]
        for row_to_sum,col_to_sum in rows_and_cols_to_sum:
            if row-row_to_sum<0 or col+col_to_sum>7:
                continue
            other_piece=self.__board__.get_piece(row-row_to_sum,col+col_to_sum)
            if other_piece is None:
                possibles.append((row-row_to_sum,col+col_to_sum))
            elif other_piece.__color__!=self.__color__:
                possibles.append((row-row_to_sum,col+col_to_sum))
        return possibles
