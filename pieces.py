class Piece:
    def __init__(self,color,board):
        self.__color__=color
        self.__board__=board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        return self.black_str
        
    def get_color(self):
        return self.__color__
    
    def get_opposite_color(self):
        if self.__color__=='WHITE':
            return 'BLACK'
        return 'WHITE'

    # CHECKS IF TO_ROW AND TO_COL ARE IN POSSIBEL POSITIONS:

    def is_row_col_in_valid_positions(self,to_row,to_col,possible_positions):
        if (to_row,to_col) in possible_positions:
            return True
        False