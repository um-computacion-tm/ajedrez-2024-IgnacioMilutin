from pieces import Piece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King
from exceptions import OutOfBoard, RowOutOfBoard, ColumnOutOfBoard

class Board:
    def __init__(self,for_test = False):
        self.__positions__=[]
        for _ in range(8):
            col=[]
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)
        if not for_test:
            self.rook_board_definition()
            self.pawn_board_definition()
            self.king_board_definition()
            self.queen_board_definition()
            self.bishop_board_definition()
            self.knight_board_definition()
    
    # CREATE THE PRINT OF THE BOARD
    
    def __str__(self):
        board_str = "    0   1   2   3   4   5   6   7\n"
        board_str += "  " + "-" * 33 + "\n"
        for i, row in enumerate(self.__positions__):
            board_str += str(i) + " | "
            for cell in row:
                if cell is not None:
                    board_str += str(cell) + " | "
                else:
                    board_str += "  | "
            board_str += "\n"
            board_str += "  " + "-" * 33 + "\n"
        return board_str

    # GETS THE PIECE OF A SPECIFIC ROW AND COLUMN

    def get_piece(self,row,col):
        if not (0 <= row < 8) and not (0 <= col < 8):
            raise OutOfBoard()
        elif not (0 <= row < 8):
            raise RowOutOfBoard()
        elif not (-1 < col < 8):
            raise ColumnOutOfBoard()
        else: return self.__positions__[row][col]
    
    # SETS A PIECE IN A SPECIFIC ROW AND COLUMN

    def set_piece(self, row, col, piece):
        if not (0 <= row < 8) and not (0 <= col < 8):
            raise OutOfBoard()
        elif not (0 <= row < 8):
            raise RowOutOfBoard()
        elif not (0 <= col < 8):
            raise ColumnOutOfBoard()
        else: self.__positions__[row][col] = piece

    # MOVES A PIECE FROM A CELL TO OTHER CELL

    def move(self,from_row,from_col,to_row,to_col):
        origin=self.get_piece(from_row,from_col)
        self.set_piece(to_row,to_col,origin)
        self.set_piece(from_row,from_col,None)

    # SETS ROOKS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def rook_board_definition(self):
        self.__positions__[0][0]=Rook('BLACK',self)
        self.__positions__[0][7]=Rook('BLACK',self)
        self.__positions__[7][7]=Rook('WHITE',self)
        self.__positions__[7][0]=Rook('WHITE',self)

    # SETS PAWNS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def pawn_board_definition(self):
        self.__positions__[6][0]=Pawn('WHITE',self)
        self.__positions__[6][1]=Pawn('WHITE',self)
        self.__positions__[6][2]=Pawn('WHITE',self)
        self.__positions__[6][3]=Pawn('WHITE',self)
        self.__positions__[6][4]=Pawn('WHITE',self)
        self.__positions__[6][5]=Pawn('WHITE',self)
        self.__positions__[6][6]=Pawn('WHITE',self)
        self.__positions__[6][7]=Pawn('WHITE',self)
        self.__positions__[1][0]=Pawn('BLACK',self)
        self.__positions__[1][1]=Pawn('BLACK',self)
        self.__positions__[1][2]=Pawn('BLACK',self)
        self.__positions__[1][3]=Pawn('BLACK',self)
        self.__positions__[1][4]=Pawn('BLACK',self)
        self.__positions__[1][5]=Pawn('BLACK',self)
        self.__positions__[1][6]=Pawn('BLACK',self)
        self.__positions__[1][7]=Pawn('BLACK',self)
    
    # SETS KINGS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def king_board_definition(self):
        self.__positions__[7][4]=King('WHITE',self)
        self.__positions__[0][4]=King('BLACK',self)

    # SETS QUEENS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def queen_board_definition(self):
        self.__positions__[7][3]=Queen('WHITE',self)
        self.__positions__[0][3]=Queen('BLACK',self)

    # SETS BISHOPS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def bishop_board_definition(self):
        self.__positions__[7][2]=Bishop('WHITE',self)
        self.__positions__[7][5]=Bishop('WHITE',self)
        self.__positions__[0][2]=Bishop('BLACK',self)
        self.__positions__[0][5]=Bishop('BLACK',self)

    # SETS KNIGHTS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def knight_board_definition(self):
        self.__positions__[7][1]=Knight('WHITE',self)
        self.__positions__[7][6]=Knight('WHITE',self)
        self.__positions__[0][1]=Knight('BLACK',self)
        self.__positions__[0][6]=Knight('BLACK',self)