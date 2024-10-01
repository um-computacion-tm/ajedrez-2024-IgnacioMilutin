import unittest
from pieces import Piece
from pawn import Pawn
from board import Board
from bishop import Bishop
from moves import possible_positions_dar, possible_positions_dal, possible_positions_ddr, possible_positions_ddl

class TestBishop(unittest.TestCase):

    # STR

    def test_str_white(self):
        board=Board()
        bishop=Bishop('WHITE',board)
        self.assertEqual(str(bishop),'♝')

    def test_str_black(self):
        board=Board()
        bishop=Bishop('BLAck',board)
        self.assertEqual(str(bishop),'♗')

    # DIAGONAL ASCENDANT TO THE RIGHT:

    def test_move_diagonal_ascendant_right(self):
        board=Board(for_test=True)
        bishop=Bishop('WHITE',board)
        board.set_piece(4,4,bishop)
        possibles=possible_positions_dar(bishop,4,4)
        self.assertEqual(possibles,[(3,5),(2,6),(1,7)])
    
    def test_move_diagonal_ascendant_right_with_own_pieces(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(2,6,Pawn("BLACK", board))
        possibles = possible_positions_dar(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(3,5)]
        )

    def test_move_diagonal_ascendant_right_with_enemy_piece(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(2,6,Pawn("WHITE", board))
        possibles = possible_positions_dar(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(3, 5),(2,6)]
        )

    # DIAGONAL ASCENDANT TO THE LEFT:

    def test_move_diagonal_ascendant_left(self):
        board=Board(for_test=True)
        bishop=Bishop('WHITE',board)
        board.set_piece(4,4,bishop)
        possibles=possible_positions_dal(bishop,4,4)
        self.assertEqual(possibles,[(3,3),(2,2),(1,1),(0,0)])
    
    def test_move_diagonal_ascendant_left_with_own_pieces(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(1,1,Pawn("BLACK", board))
        possibles = possible_positions_dal(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(3,3),(2,2)]
        )

    def test_move_diagonal_ascendant_left_with_enemy_piece(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(1,1,Pawn("WHITE", board))
        possibles = possible_positions_dal(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(3,3),(2,2),(1,1)]
        )

    # DIAGONAL DESCENDANT TO THE RIGHT:

    def test_move_diagonal_descendant_right(self):
        board=Board(for_test=True)
        bishop=Bishop('WHITE',board)
        board.set_piece(4,4,bishop)
        possibles=possible_positions_ddr(bishop,4,4)
        self.assertEqual(possibles,[(5,5),(6,6),(7,7)])
    
    def test_move_diagonal_descendant_right_with_own_pieces(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(6,6,Pawn("BLACK", board))
        possibles = possible_positions_ddr(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(5,5)]
        )

    def test_move_diagonal_descendant_right_with_enemy_piece(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(6,6,Pawn("WHITE", board))
        possibles = possible_positions_ddr(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(5, 5),(6,6)]
        )

    # DIAGONAL DESCENDANT TO THE LEFT:

    def test_move_diagonal_descendant_left(self):
        board=Board(for_test=True)
        bishop=Bishop('WHITE',board)
        board.set_piece(4,4,bishop)
        possibles=possible_positions_ddl(bishop,4,4)
        self.assertEqual(possibles,[(5,3),(6,2),(7,1)])
    
    def test_move_diagonal_descendant_left_with_own_pieces(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(6,2,Pawn("BLACK", board))
        possibles = possible_positions_ddl(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(5,3)]
        )

    def test_move_diagonal_descendant_left_with_enemy_piece(self):
        board = Board(for_test=True)
        bishop = Bishop("BLACK", board)
        board.set_piece(4,4, bishop)
        board.set_piece(6,2,Pawn("WHITE", board))
        possibles = possible_positions_ddl(bishop,4, 4)
        self.assertEqual(
            possibles,
            [(5, 3),(6,2)])
        
    # VALID POSITIONS:

    def test_valid_positions_rook(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        board.set_piece(4,4,bishop)
        possible=bishop.valid_positions(4,4)
        self.assertEqual(possible,[(3,5),(2,6),(1,7),(3,3),(2,2),(1,1),(0,0),(5,5),(6,6),(7,7),(5,3),(6,2),(7,1)])

    # VERTICAL WRONG MOVES:

    def test_wrong_move_vertical_ascendant(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        board.set_piece(4,4,bishop)
        possible_positions=bishop.valid_positions(4,4)
        possible=bishop.is_row_col_in_valid_positions(3,4,possible_positions)
        self.assertFalse(possible)
        
    def test_wrong_move_vertical_descendant(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        board.set_piece(4,4,bishop)
        possible_positions=bishop.valid_positions(4,4)
        possible=bishop.is_row_col_in_valid_positions(5,4,possible_positions)
        self.assertFalse(possible)

    # HORIZONTAL WRONG MOVES:

    def test_wrong_move_horizontal_right(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        board.set_piece(4,4,bishop)
        possible_positions=bishop.valid_positions(4,4)
        possible=bishop.is_row_col_in_valid_positions(4,5,possible_positions)
        self.assertFalse(possible)
        
    def test_wrong_move_horizontal_left(self):
        board=Board(for_test=True)
        bishop=Bishop('BLACK',board)
        board.set_piece(4,4,bishop)
        possible_positions=bishop.valid_positions(4,4)
        possible=bishop.is_row_col_in_valid_positions(4,3,possible_positions)
        self.assertFalse(possible)