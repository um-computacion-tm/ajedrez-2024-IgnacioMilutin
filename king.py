from pieces import Piece
from moves import all_moves

class King(Piece):
    white_str='♚'
    black_str='♔'

    # FILTERS ALL POSSIBLE KINGS MOVES WITH THE OTHER TEAMS MOVES

    def filter_move(self,possible_positions,all_opponent_moves):
        final_possible_positions=[]
        for move in possible_positions:
            if move not in all_opponent_moves:
                final_possible_positions.append(move)
        return final_possible_positions
    
    # ALL VALID POSITIONS ('for_all_moves' parameter is to avoid recursion when using 'all_moves()' function)

    def valid_positions(self,from_row,from_col,for_all_moves=False):
        possible_positions=self.possible_positions_va(from_row,from_col)+self.possible_positions_vd(from_row,from_col)+self.possible_positions_hr(from_row,from_col)+self.possible_positions_hl(from_row,from_col)+self.possible_positions_dar(from_row,from_col)+self.possible_positions_dal(from_row,from_col)+self.possible_positions_ddr(from_row,from_col)+self.possible_positions_ddl(from_row,from_col)
        if for_all_moves==False:
            full_moves=all_moves(self.__board__,self.get_opposite_color())
            return self.filter_move(possible_positions,full_moves)
        return possible_positions

    # VERTICAL ASCENDANT MOVE

    def possible_positions_va(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row-1,col))
        return possibles
    
    # VERTICAL DESCENDANT MOVE
        
    def possible_positions_vd(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row+1,col))
        return possibles
    
    # HORIZONTAL RIGHT MOVE

    def possible_positions_hr(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row,col+1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row,col+1))
        return possibles
    
    # HORIZONTAL LEFT MOVE
    
    def possible_positions_hl(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row,col-1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row,col-1))
        return possibles
    
    # DIAGONAL ASCENDANT TO THE RIGHT MOVE
    
    def possible_positions_dar(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col+1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row-1,col+1))
        return possibles
    
    # DIAGONAL ASCENDANT TO THE LEFT MOVE

    def possible_positions_dal(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row-1,col-1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row-1,col-1))
        return possibles
    
    # DIAGONAL DESCENDANT TO THE RIGHT MOVE
    
    def possible_positions_ddr(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col+1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row+1,col+1))
        return possibles
    
    # DIAGONAL DESCENDANT TO THE LEFT MOVE

    def possible_positions_ddl(self,row,col):
        possibles=[]
        other_piece=self.__board__.get_piece(row+1,col-1)
        if other_piece is None or other_piece.__color__!=self.__color__:
            possibles.append((row+1,col-1))
        return possibles