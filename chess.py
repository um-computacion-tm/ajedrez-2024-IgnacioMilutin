from board import Board
from pawn import Pawn
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from exceptions import InvalidMove,EmptyPosition,InvalidTurn,InvalidPawnChange

class Chess:
    def __init__(self):
        self.__board__=Board()
        self.__turn__='WHITE'
    
    # METHOD TO INITIALIZE GAME WITH WHILE

    def is_playing(self):
        return True

    # USES RULES FROM EVERY PIECE AND BOARD TO MOVE AND CHANGE TURNS

    def move(self,from_row,from_col,to_row,to_col):
        piece = self.__board__.get_piece(from_row, from_col)
        if piece==None:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        possible=piece.valid_positions(from_row,from_col)
        if not piece.is_row_col_in_valid_positions(to_row,to_col,possible):
            raise InvalidMove()
        else:
            self.__board__.move(from_row, from_col, to_row, to_col)
            self.change_turn()
    
    # GET THE CURRENT TURN

    def turn(self):
        return self.__turn__
    
    # SHOWS THE BOARD OF THE GAME

    def show_board(self):
        return str(self.__board__)
    
    # CHANGES THE TURN

    def change_turn(self):
        if self.__turn__=='WHITE':
            self.__turn__='BLACK'
        else: self.__turn__='WHITE'

    # EXECUTION  OF CHESS RULES AFTER EVERY MOVE IN CLI: PAWN_CHANGE

    def rules(self, to_row, to_col):
        if self.pawn_change_verification(to_row, to_col):
            while True:
                new_piece = input('Type the piece you would like to replace the pawn (Queen, Rook, Bishop or Knight): ')
                try:
                    self.pawn_change_action(new_piece, to_row, to_col)
                    break
                except Exception as pawn_change_exception:
                    print(pawn_change_exception)
                    continue

    # VERIFIES IF THE PIECE THAT HITTED THE END IS A PAWN

    def pawn_change_verification(self,row,col):
        if (row==7 or row==0) and (isinstance(self.__board__.get_piece(row,col),Pawn)):
            return True

    # PAWN CONVERT TO ANY PIECE

    def pawn_change_action(self,new_piece,row,col):
        pawn=self.__board__.get_piece(row,col)
        pieces={'queen':Queen,'rook':Rook,'bishop':Bishop,'knight':Knight}
        new_piece=pieces.get(new_piece.lower())
        if new_piece:
            self.__board__.set_piece(row,col,new_piece(pawn.get_color(),self.__board__))
        else:
            raise InvalidPawnChange()