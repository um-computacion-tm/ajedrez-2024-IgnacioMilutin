from pieces import Piece

class Pawn(Piece):
    white_str='♟'
    black_str='♙'

    # POSSIBLE POSITIONS TO MOVE PAWN INCLUDIONG MOVE AND EAT
    
    def valid_positions(self,from_row,from_col):
        possible_positions=self.possible_positions_move(from_row, from_col)+self.possible_positions_eat(from_row, from_col)
        return possible_positions
   
    # PAWN EATING A PIECE

    def possible_positions_eat(self,from_row,from_col):
        possible=[]
        colors_and_rows={'BLACK':1,'WHITE':-1}
        col_left=-1
        col_right=1
        move_row=colors_and_rows[self.__color__]
        next_row=from_row+move_row
        other_piece_right=self.__board__.get_piece(next_row,from_col+col_right)
        other_piece_left=self.__board__.get_piece(next_row,from_col+col_left)
        if other_piece_right is not None and other_piece_right.__color__!=self.__color__:
            possible.append((next_row,from_col+col_right))
        if other_piece_left is not None and other_piece_left.__color__!=self.__color__:
            possible.append((next_row,from_col+col_left))
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