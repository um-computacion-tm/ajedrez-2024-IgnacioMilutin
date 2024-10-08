class Piece:
    def __init__(self,color,board):
        self.__color__=color
        self.__board__=board

    def __str__(self):
        if self.__color__ == "WHITE":
            return self.white_str
        else: return self.black_str
        
    def get_color(self):
        return self.__color__
    
class Pawn(Piece):
    def __init__(self,color,board):
        super().__init__(color,board)
    
    def __str__(self):
        if self.__color__=="WHITE":
            return "♟"
        else: return "♙"
