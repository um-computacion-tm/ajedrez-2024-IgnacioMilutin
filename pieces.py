class Piece:
    def __init__(self,color,name):
        self.__color__=color
        self.__name__=name

class Rook(Piece):
    def __init__(self,color,name):
        super().__init__(color,name)

    def __str__(self):
        if self.__color__ == "WHITE":
            return "♜"
        else:
            return "♖"
        
class Pawn(Piece):
    ...
