from board import Board
from exceptions import InvalidMove,EmptyPosition,InvalidTurn

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
        if not piece:
            raise EmptyPosition()
        if not piece.get_color() == self.__turn__:
            raise InvalidTurn()
        if not piece.valid_postions(from_row, from_col, to_row, to_col):
            raise InvalidMove()
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