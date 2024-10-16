from pieces import Piece

class Knight(Piece):
    white_str='♞'
    black_str='♘'

    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_var(from_row, from_col)+self.possible_positions_val(from_row, from_col)+self.possible_positions_vdr(from_row, from_col)+self.possible_positions_vdl(from_row, from_col)+self.possible_positions_hra(from_row, from_col)+self.possible_positions_hrd(from_row, from_col)+self.possible_positions_hla(from_row, from_col)+self.possible_positions_hld(from_row, from_col)
        return possible_positions
    
    # VERTICAL ASCENDANT TO THE RIGHT MOVE

    def possible_positions_var(self,row,col):
        possibles=[]
        if row-2<0 or col+1>7:
            return []
        other_piece=self.__board__.get_piece(row-2,col+1)
        if other_piece is None:
            possibles.append((row-2,col+1))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row-2,col+1))
        return possibles
    
    # VERTICAL ASCENDANT TO THE LEFT MOVE

    def possible_positions_val(self,row,col):
        possibles=[]
        if row-2<0 or col-1<0:
            return []
        other_piece=self.__board__.get_piece(row-2,col-1)
        if other_piece is None:
            possibles.append((row-2,col-1))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row-2,col-1))
        return possibles
    
    # VERTICAL DESCENDANT TO THE RIGHT MOVE
    
    def possible_positions_vdr(self,row,col):
        possibles=[]
        if row+2>7 or col+1>7:
            return []
        other_piece=self.__board__.get_piece(row+2,col+1)
        if other_piece is None:
            possibles.append((row+2,col+1))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row+2,col+1))
        return possibles
    
    # VERTICAL DESCENDANT TO THE LEFT MOVE
    
    def possible_positions_vdl(self,row,col):
        possibles=[]
        if row+2>7 or col-1<0:
            return []
        other_piece=self.__board__.get_piece(row+2,col-1)
        if other_piece is None:
            possibles.append((row+2,col-1))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row+2,col-1))
        return possibles
    
    # HORIZONTAL RIGHT AND ASCENDANT MOVE
    
    def possible_positions_hra(self,row,col):
        possibles=[]
        if row-1<0 or col+2>7:
            return []
        other_piece=self.__board__.get_piece(row-1,col+2)
        if other_piece is None:
            possibles.append((row-1,col+2))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row-1,col+2))
        return possibles
    
    # HORIZONTAL RIGHT AND DESCENDANT MOVE
    
    def possible_positions_hrd(self,row,col):
        possibles=[]
        if row+1>7 or col+2>7:
            return []
        other_piece=self.__board__.get_piece(row+1,col+2)
        if other_piece is None:
            possibles.append((row+1,col+2))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row+1,col+2))
        return possibles
    
    # HORIZONTAL LEFT AND ASCENDANT MOVE

    def possible_positions_hla(self,row,col):
        possibles=[]
        if row-1<0 or col-2<0:
            return []
        other_piece=self.__board__.get_piece(row-1,col-2)
        if other_piece is None:
            possibles.append((row-1,col-2))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row-1,col-2))
        return possibles
    
    # HORIZONTAL LEFT AND DESCENDANT MOVE
    
    def possible_positions_hld(self,row,col):
        possibles=[]
        if row+1>7 or col-2<0:
            return []
        other_piece=self.__board__.get_piece(row+1,col-2)
        if other_piece is None:
            possibles.append((row+1,col-2))
        elif other_piece.__color__!=self.__color__:
            possibles.append((row+1,col-2))
        return possibles