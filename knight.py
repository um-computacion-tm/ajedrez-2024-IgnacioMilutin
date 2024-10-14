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
        if row-2<0 and col+1>7:
            return []
        elif row-2>-1 and col+1<8:
            other_piece=self.__board__.get_piece(row-2,col+1)
            if other_piece is None:
                possibles.append((row-2,col+1))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row-2,col+1))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row-2,col+1))
                else: return[]
        return possibles

    # VERTICAL ASCENDANT TO THE LEFT MOVE

    def possible_positions_val(self,row,col):
        possibles=[]
        if row-2<0 and col-1<0:
            return []
        elif row-2>-1 and col-1>-1:
            other_piece=self.__board__.get_piece(row-2,col-1)
            if other_piece is None:
                possibles.append((row-2,col-1))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row-2,col-1))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row-2,col-1))
                else: return[]
        return possibles
    
    # VERTICAL DESCENDANT TO THE RIGHT MOVE
    
    def possible_positions_vdr(self,row,col):
        possibles=[]
        if row+2>7 and col+1>7:
            return []
        elif row+2<8 and col+1<8:
            other_piece=self.__board__.get_piece(row+2,col+1)
            if other_piece is None:
                possibles.append((row+2,col+1))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row+2,col+1))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row+2,col+1))
                else: return[]
        return possibles
    
    # VERTICAL DESCENDANT TO THE LEFT MOVE
    
    def possible_positions_vdl(self,row,col):
        possibles=[]
        if row+2>7 and col-1<0:
            return []
        elif row+2<8 and col-1>-1:
            other_piece=self.__board__.get_piece(row+2,col-1)
            if other_piece is None:
                possibles.append((row+2,col-1))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row+2,col-1))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row+2,col-1))
                else: return[]
        return possibles
    
    # HORIZONTAL RIGHT AND ASCENDANT MOVE
    
    def possible_positions_hra(self,row,col):
        possibles=[]
        if row-1<0 and col+2>7:
            return []
        elif row-1>-1 and col+2<8:
            other_piece=self.__board__.get_piece(row-1,col+2)
            if other_piece is None:
                possibles.append((row-1,col+2))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row-1,col+2))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row-1,col+2))
                else: return[]
        return possibles
    
    # HORIZONTAL RIGHT AND DESCENDANT MOVE
    
    def possible_positions_hrd(self,row,col):
        possibles=[]
        if row+1>7 and col+2>7:
            return []
        elif row+1<8 and col+2<8:
            other_piece=self.__board__.get_piece(row+1,col+2)
            if other_piece is None:
                possibles.append((row+1,col+2))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row+1,col+2))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row+1,col+2))
                else: return[]
        return possibles
    
    # HORIZONTAL LEFT AND ASCENDANT MOVE
    
    def possible_positions_hla(self,row,col):
        possibles=[]
        if row-1<0 and col-2<0:
            return []
        elif row-1>-1 and col-2>-1:
            other_piece=self.__board__.get_piece(row-1,col-2)
            if other_piece is None:
                possibles.append((row-1,col-2))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row-1,col-2))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row-1,col-2))
                else: return[]
        return possibles
    
    # HORIZONTAL LEFT AND DESCENDANT MOVE
    
    def possible_positions_hld(self,row,col):
        possibles=[]
        if row+1>7 and col-2<0:
            return []
        elif row+1<8 and col-2>-1:
            other_piece=self.__board__.get_piece(row+1,col-2)
            if other_piece is None:
                possibles.append((row+1,col-2))
            elif self.__color__=='BLACK':
                if other_piece is not None and other_piece.__color__=='WHITE':
                    possibles.append((row+1,col-2))
                else: return[]
            else:
                if other_piece is not None and other_piece.__color__=='BLACK':
                    possibles.append((row+1,col-2))
                else: return[]
        return possibles