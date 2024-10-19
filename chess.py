from board import Board
from pawn import Pawn
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from king import King
from exceptions import InvalidMove,EmptyPosition,InvalidTurn,InvalidPawnChange

class Chess:
    def __init__(self):
        self.__board__=Board()
        self.__turn__='WHITE'
    
    # METHOD TO INITIALIZE GAME WITH WHILE

    def is_playing(self):
        return True
    
    # METHOD TO END THE GAME}

    def end_game(self):
        return False

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

    # GIVES THE COLOR OF THE NEXT TURN

    def get_next_turn(self):
        if self.__turn__=='WHITE':
           return 'BLACK'
        else: return 'WHITE'

    # EXECUTION OF CHESS RULES AFTER EVERY MOVE IN CLI: PAWN_CHANGE, END GAME WHEN THERES NO PIECES FOR ONE COLOR, 

    def rules(self, to_row, to_col):
        if self.pawn_change_verification(to_row, to_col):
            self.pawn_change_rule(to_row, to_col)
        self.end_due_to_no_piece_rule()


    # PAWN CHANGE INTO OTHER PIECE RULE

    def pawn_change_rule(self, to_row, to_col):
        while True:  
            new_piece = self.ask_for_piece() 
            try:
                self.pawn_change_action(new_piece, to_row, to_col)  
                break 
            except InvalidPawnChange as pawn_change_exception:
                print(pawn_change_exception) 
                continue  

    # ASKS THE USER WHICH PIECE TO CHANGE THE PAWN TO

    def ask_for_piece(self):
        return input('Type the piece you would like to replace the pawn (Queen, Rook, Bishop or Knight): ')
        
    
    # VERIFIES IF THE PIECE THAT HITTED THE END IS A PAWN

    def pawn_change_verification(self,row,col):
        if (row==7 or row==0) and (isinstance(self.__board__.get_piece(row,col),Pawn)):
            return True

    # PAWN CONVERT TO ANY PIECE

    def pawn_change_action(self, new_piece, row, col):
        pawn = self.__board__.get_piece(row, col)
        pieces = {'queen': Queen, 'rook': Rook, 'bishop': Bishop, 'knight': Knight}
        new_piece_class = pieces.get(new_piece.lower())  
        if new_piece_class:
            self.__board__.set_piece(row, col, new_piece_class(pawn.get_color(), self.__board__))
        else:
            raise InvalidPawnChange()
        
    # RULE FOR ENDING THE GAME GAME WHEN A COLOR RUNS OUT OF PIECES
        
    def end_due_to_no_piece_rule(self):
        if self.end_due_to_no_piece_verification():
            print(f"{self.__turn__} ran out of pieces. ¡{self.get_next_turn()} WINS THE GAME!")
            self.end_game()
        else: return True
        
    # VERIFIES THE STATE OF DE CELL TO CHECK IF THE COLOR HAS NO PIECE

    def end_due_to_no_piece_verification(self):
        for row in range(8):
            for col in range(8):
                if self.cell_evaluation(row, col):
                    return False
        return True
                
    # CHECKS THE STATE OF THE CELL TO SEE IF ITS NONE OR A PIECVE FROM THE OTHER COLOR

    def cell_evaluation(self,row, col):
        cell = self.__board__.get_piece(row, col)
        return cell is not None and cell.get_color() == self.__turn__
