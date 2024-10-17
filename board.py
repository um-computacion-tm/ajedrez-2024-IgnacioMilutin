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
        if 0 < row > 7 and 0 < col > 7:
            raise OutOfBoard()
        if 0 < row > 7:
            raise RowOutOfBoard()
        if 0 < col > 7:
            raise ColumnOutOfBoard()
        return self.__positions__[row][col]
    
    # SETS A PIECE IN A SPECIFIC ROW AND COLUMN

    def set_piece(self, row, col, piece):
        if 0 < row > 7 and 0 < col > 7:
            raise OutOfBoard()
        if 0 < row > 7:
            raise RowOutOfBoard()
        if 0 < col > 7:
            raise ColumnOutOfBoard()
        self.__positions__[row][col] = piece

    # MOVES A PIECE FROM A CELL TO OTHER CELL

    def move(self,from_row,from_col,to_row,to_col):
        origin=self.get_piece(from_row,from_col)
        self.set_piece(to_row,to_col,origin)
        self.set_piece(from_row,from_col,None)

    # DEFINTION TO SET BISHOP, KNIGHT AND ROOK IN THEIR INITIAL POSITIONS

    def board_definition_for_bishop_rook_and_knight(self,type_piece):
        rows_and_colors=[(0,'BLACK'),(7,'WHITE')]
        cols_knight=[1,6]
        cols_bishop=[2,5]
        cols_rook=[7,0]
        for (row,color) in rows_and_colors:
            if type_piece==Knight:
                cols=cols_knight
            if type_piece==Rook:
                cols=cols_rook
            if type_piece==Bishop:
                cols=cols_bishop
            for col in cols:
                self.__positions__[row][col]=type_piece(color,self)
        
    # SETS PAWNS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def pawn_board_definition(self):
        rows_and_colors=[(1,'BLACK'),(6,'WHITE')]
        cols=[0,1,2,3,4,5,6,7]
        for (row,color) in rows_and_colors:
            for col in cols:
                self.__positions__[row][col]=Pawn(color,self)

    # DEFINITION TO SET KING AND QUEEN IN THEIR INITIAL POSITIONS

    def board_definition_for_king_and_queen(self,type_piece):
        rows_and_colors=[(7,'WHITE'),(0,'BLACK')]
        for (row,color) in rows_and_colors:
            if type_piece==King:
                col=4
            else: col=3
            self.__positions__[row][col]=type_piece(color,self)

    # SETS KINGS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def king_board_definition(self):    
        self.board_definition_for_king_and_queen(King)

    # SETS QUEENS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def queen_board_definition(self):
        self.board_definition_for_king_and_queen(Queen)

    # SETS ROOKS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def rook_board_definition(self):
        self.board_definition_for_bishop_rook_and_knight(Rook)

    # SETS BISHOPS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def bishop_board_definition(self):
        self.board_definition_for_bishop_rook_and_knight(Bishop)

    # SETS KNIGHTS IN THEIR INITIAL POSITIONS WHEN STARTING THE BOARD 

    def knight_board_definition(self):
        self.board_definition_for_bishop_rook_and_knight(Knight)