from pieces import Piece
from moves import get_possible_positions

class Pawn(Piece):
    white_str='♟'
    black_str='♙'

    # POSSIBLE POSITIONS TO MOVE PAWN INCLUDIONG MOVE AND EAT
    
    def valid_positions(self,from_row,from_col):
        movement_functions = [
            self.possible_positions_move, 
            self.possible_positions_eat]
        return get_possible_positions(from_row, from_col, movement_functions)
   
    # PAWN EATING A PIECE
    
    def possible_positions_eat(self,from_row,from_col):
        possible=[]
        colors_and_rows={'BLACK':1,'WHITE':-1}
        cols=[1,-1]
        move_row=colors_and_rows[self.__color__]
        next_row=from_row+move_row
        for next_col in cols:
            other_piece=self.__board__.get_piece(next_row,from_col+next_col)
            if other_piece is not None and other_piece.__color__!=self.__color__:
                possible.append((next_row,from_col+next_col))
        return possible
    

    # MOVING A PAWN RULES

    def possible_positions_move(self,from_row,from_col):
        colors_and_rows={'BLACK':(1,1),'WHITE':(-1,6)}
        move_row,start=colors_and_rows[self.__color__]
        next_row=from_row+move_row
        if self.__board__.get_piece(next_row,from_col) is None:
            possibles=[(next_row,from_col)]
            if from_row==start and self.__board__.get_piece(next_row+move_row,from_col) is None:
                possibles.append((next_row+move_row,from_col))
            return possibles
        else: return []