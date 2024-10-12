from pieces import Piece
from chess import Chess
from moves import all_moves

class King(Piece):
    white_str='♚'
    black_str='♔'

    # ALL VALID POSITIONS

    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_va(from_row,from_col)+self.possible_positions_vd(from_row,from_col)+self.possible_positions_hr(from_row,from_col)+self.possible_positions_hl(from_row,from_col)+self.possible_positions_dar(from_row,from_col)+self.possible_positions_dal(from_row,from_col)+self.possible_positions_ddr(from_row,from_col)+self.possible_positions_ddl(from_row,from_col)
        all_moves=all_moves(self,self.get_color())
        possible_positions=[item for item in possible_positions if item not in all_moves]
        return possible_positions

    # VERTICAL ASCENDANT MOVE

    def possible_positions_va(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col)
        if other_piece is None:
            possibles.append((row-1,col))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row-1,col))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row-1,col))
            else: return[]
        return possibles
    
    # VERTICAL DESCENDANT MOVE
        
    def possible_positions_vd(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col)
        if other_piece is None:
            possibles.append((row+1,col))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row+1,col))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row+1,col))
            else: return[]
        return possibles
    
    # HORIZONTAL RIGHT MOVE

    def possible_positions_hr(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row,col+1)
        if other_piece is None:
            possibles.append((row,col+1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row,col+1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row,col+1))
            else: return[]
        return possibles
    
    # HORIZONTAL LEFT MOVE
    
    def possible_positions_hl(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row,col-1)
        if other_piece is None:
            possibles.append((row,col-1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row,col-1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row,col-1))
            else: return[]
        return possibles
    
    # DIAGONAL ASCENDANT TO THE RIGHT MOVE
    
    def possible_positions_dar(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col+1)
        if other_piece is None:
            possibles.append((row-1,col+1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row-1,col+1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row-1,col+1))
            else: return[]
        return possibles
    
    # DIAGONAL ASCENDANT TO THE LEFT MOVE

    def possible_positions_dal(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col-1)
        if other_piece is None:
            possibles.append((row-1,col-1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row-1,col-1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row-1,col-1))
            else: return[]
        return possibles
    
    # DIAGONAL DESCENDANT TO THE RIGHT MOVE
    
    def possible_positions_ddr(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col+1)
        if other_piece is None:
            possibles.append((row+1,col+1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row+1,col+1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row+1,col+1))
            else: return[]
        return possibles
    
    # DIAGONAL DESCENDANT TO THE LEFT MOVE

    def possible_positions_ddl(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col-1)
        if other_piece is None:
            possibles.append((row+1,col-1))
        elif self.__color__=='BLACK':
            if other_piece is not None and other_piece.__color__=='WHITE':
                possibles.append((row+1,col-1))
            else: return[]
        else:
            if other_piece is not None and other_piece.__color__=='BLACK':
                possibles.append((row+1,col-1))
            else: return[]
        return possibles