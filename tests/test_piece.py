import unittest
from pieces import Piece
from board import Board
from rook import Rook


class TestPiece(unittest.TestCase):

    # STR

    def test_str_white(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        self.assertEqual(rook.__str__(),'♜')

    def test_str_black(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertEqual(rook.__str__(),'♖')

    # GET_COLOR

    def test_get_color_white(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        self.assertEqual(rook.get_color(),'WHITE')

    def test_get_color_black(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        self.assertEqual(rook.get_color(),'BLACK')


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