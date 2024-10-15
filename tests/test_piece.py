import unittest
from pieces import Piece
from board import Board
from rook import Rook
from pawn import Pawn
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight



class TestPiece(unittest.TestCase):

    # STR

    def test_str_white_rook(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        self.assertEqual(str(rook),'♜')

    def test_str_black_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertEqual(rook.__str__(),'♖')

    def test_str_white_pawn(self):
        board=Board(for_test=True)
        pawn=Pawn('WHITE',board)
        self.assertEqual(str(pawn),'♟')

    def test_str_black_pawn(self):
        board=Board(for_test=True)
        pawn=Pawn('BLACK',board)
        self.assertEqual(pawn.__str__(),'♙')

    def test_str_white_knight(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        self.assertEqual(str(knight),'♞')

    def test_str_black_knight(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        self.assertEqual(knight.__str__(),'♘')

    def test_str_white_bishop(self):
        board=Board(for_test=True)
        bishop=Bishop('WHITE',board)
        self.assertEqual(str(bishop),'♝')

    def test_str_black_bishop(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        self.assertEqual(bishop.__str__(),'♗')

    def test_str_white_king(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        self.assertEqual(str(king),'♚')

    def test_str_black_king(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        self.assertEqual(king.__str__(),'♔')

    def test_str_white_queen(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        self.assertEqual(str(queen),'♛')

    def test_str_black_queen(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        self.assertEqual(queen.__str__(),'♕')
    

    # GET_COLOR

    def test_get_color_white(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        self.assertEqual(rook.get_color(),'WHITE')

    def test_get_color_black(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertEqual(rook.get_color(),'BLACK')

    # GET_OPPOSITE_COLOR

    def test_get_opposite_color_white_piece(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        self.assertEqual(rook.get_opposite_color(),'BLACK')

    def test_get_opposite_color_black_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertEqual(rook.get_opposite_color(),'WHITE')

    # IS TO_ROW AND TO_COL IN VALID POSITIONS:

    def test_is_row_col_in_valid_postions_true_path(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible_positions=rook.valid_positions(4,4)
        validation=rook.is_row_col_in_valid_positions(3,4,possible_positions)
        self.assertTrue(validation)

    def test_is_row_col_in_valid_postions_false_path(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible_positions=rook.valid_positions(4,4)
        validation=rook.is_row_col_in_valid_positions(3,3,possible_positions)
        self.assertFalse(validation)

if __name__=='__main__':
    unittest.main()