import unittest
from pieces import Pawn
from board import Board
from rook import Rook

class TestRook(unittest.TestCase):
    def test_str(self):
        board=Board()
        rook=Rook('WHITE',board)
        self.assertEqual(str(rook),'♜')

    #VERTICAL DESCENDANT:

    def test_move_vertical_desc(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        board.set_piece(0,4,rook)
        possibles=rook.possible_positions_vd(0,4)
        self.assertEqual(possibles,[(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4)])
    
    def test_move_vertical_desc_with_own_pieces(self):
        board = Board(for_test=True)
        rook = Rook("BLACK", board)
        board.set_piece(4,4, rook)
        board.set_piece(7,4,Pawn("BLACK", board))
        possibles = rook.possible_positions_vd(4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4)]
        )

    def test_move_vertical_desc_with_enemy_piece(self):
        board = Board(for_test=True)
        rook = Rook("BLACK", board)
        board.set_piece(4,4, rook)
        board.set_piece(7,4,Pawn("WHITE", board))
        possibles = rook.possible_positions_vd(4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4),(7,4)]
        )

    # VERTICAL ASCENDANT: 

    def test_move_vertical_asc(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        board.set_piece(7,4,rook)
        possibles=rook.possible_positions_va(7,4)
        self.assertEqual(possibles,[(6,4),(5,4),(4,4),(3,4),(2,4),(1,4),(0,4)])

    def test_move_vertical_asc_with_own_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(5,5,rook)
        board.set_piece(3,5,Pawn('BLACK',board))
        possibles=rook.possible_positions_va(5,5)
        self.assertEqual(possibles,[(4,5)])
        
    def test_move_vertical_asc_with_enemy_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(5,5,rook)
        board.set_piece(3,5,Pawn('WHITE',board))
        possibles=rook.possible_positions_va(5,5)
        self.assertEqual(possibles,[(4,5),(3,5)])

    # HORIZONTAL RIGHT:

    def test_move_horizontal_right(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possibles=rook.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5),(4,6),(4,7)])

    def test_move_horizontal_right_with_own_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,6,Pawn('BLACK',board))
        possibles=rook.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_horizontal_right_with_enemy_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,6,Pawn('WHITE',board))
        possibles=rook.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5),(4,6)])

    # HORIZONTAL LEFT:

    def test_move_horizontal_left(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possibles=rook.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3),(4,2),(4,1),(4,0)])

    def test_move_horizontal_left_with_own_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,2,Pawn('BLACK',board))
        possibles=rook.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_horizontal_left_with_enemy_piece(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,2,Pawn('WHITE',board))
        possibles=rook.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3),(4,2)])


    # VALID POSITIONS:

    def test_valid_positions(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible=rook.valid_positions(4,4)
        self.assertEqual(possible,[(5,4),(6,4),(7,4),(3,4),(2,4),(1,4),(0,4),(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0)])

    # IS TO_ROW AND TO_COL IN VALID POSITIONS:

    def test_is_row_col_in_valid_postions_true_path(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible_positions=rook.valid_positions(4,4)
        validation=rook.is_row_col_in_valid_postions(3,4,possible_positions)
        self.assertTrue(validation)

    def test_is_row_col_in_valid_postions_false_path(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible_positions=rook.valid_positions(4,4)
        validation=rook.is_row_col_in_valid_postions(3,3,possible_positions)
        self.assertFalse(validation)

    # DIAGONAL WORNG MOVES:

    def test_move_diagonal_desc_right(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,0,rook)
        possible_positions=rook.valid_positions(0,0)
        possible=rook.is_row_col_in_valid_postions(1,1,possible_positions)
        self.assertFalse(possible)
        
    def test_move_diagonal_desc_left(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,1,rook)
        possible_positions=rook.valid_positions(0,1)
        possible=rook.is_row_col_in_valid_postions(1,0,possible_positions)
        self.assertFalse(possible)

    def test_move_diagonal_asc_right(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        possible_positions=rook.valid_positions(1,1)
        possible=rook.is_row_col_in_valid_postions(0,2,possible_positions)
        self.assertFalse(possible)

    def test_move_diagonal_asc_left(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        possible_positions=rook.valid_positions(1,1)
        possible=rook.is_row_col_in_valid_postions(0,0,possible_positions)
        self.assertFalse(possible)


if __name__=='__main__':
    unittest.main()