from pieces import Rook

class Board:
    def __init__(self):
        self.__positions__=[]
        for _ in range(8):
            col=[]
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        self.__positions__[0][0]=Rook('BLACK','rook1_black')
        self.__positions__[0][7]=Rook('BLACK','rook2_black')
        self.__positions__[7][7]=Rook('WHITE','rook1_white')
        self.__positions__[7][0]=Rook('WHITE','rook2_white')
    
    def get_piece(self,row,col):
        return self.__positions__[row][col]
    