import unittest
from pieces import Piece
from pawn import Pawn
from board import Board
from rook import Rook
from moves import possible_positions_va, possible_positions_vd, possible_positions_hr, possible_positions_hl

class TestRook(unittest.TestCase):

    # STR:

    def test_str_white_rook(self):
        board=Board()
        rook=Rook('WHITE',board)
        self.assertEqual(str(rook),'♜')

    def test_str_black_rook(self):
        board=Board()
        rook=Rook('BLAck',board)
        self.assertEqual(str(rook),'♖')

    #VERTICAL DESCENDANT:

    def test_move_vertical_desc_rook(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        board.set_piece(0,4,rook)
        possibles=possible_positions_vd(rook,0,4)
        self.assertEqual(possibles,[(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4)])
    
    def test_move_vertical_desc_with_own_pieces_rook(self):
        board = Board(for_test=True)
        rook = Rook("BLACK", board)
        board.set_piece(4,4, rook)
        board.set_piece(7,4,Pawn("BLACK", board))
        possibles = possible_positions_vd(rook,4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4)]
        )

    def test_move_vertical_desc_with_enemy_piece_rook(self):
        board = Board(for_test=True)
        rook = Rook("BLACK", board)
        board.set_piece(4,4, rook)
        board.set_piece(7,4,Pawn("WHITE", board))
        possibles = possible_positions_vd(rook,4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4),(7,4)]
        )

    # VERTICAL ASCENDANT: 

    def test_move_vertical_asc_rook(self):
        board=Board(for_test=True)
        rook=Rook('WHITE',board)
        board.set_piece(7,4,rook)
        possibles=possible_positions_va(rook,7,4)
        self.assertEqual(possibles,[(6,4),(5,4),(4,4),(3,4),(2,4),(1,4),(0,4)])

    def test_move_vertical_asc_with_own_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(5,5,rook)
        board.set_piece(3,5,Pawn('BLACK',board))
        possibles=possible_positions_va(rook,5,5)
        self.assertEqual(possibles,[(4,5)])
        
    def test_move_vertical_asc_with_enemy_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(5,5,rook)
        board.set_piece(3,5,Pawn('WHITE',board))
        possibles=possible_positions_va(rook,5,5)
        self.assertEqual(possibles,[(4,5),(3,5)])

    # HORIZONTAL RIGHT:

    def test_move_horizontal_right_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possibles=possible_positions_hr(rook,4,4)
        self.assertEqual(possibles,[(4,5),(4,6),(4,7)])

    def test_move_horizontal_right_with_own_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,6,Pawn('BLACK',board))
        possibles=possible_positions_hr(rook,4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_horizontal_right_with_enemy_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,6,Pawn('WHITE',board))
        possibles=possible_positions_hr(rook,4,4)
        self.assertEqual(possibles,[(4,5),(4,6)])

    # HORIZONTAL LEFT:

    def test_move_horizontal_left_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possibles=possible_positions_hl(rook,4,4)
        self.assertEqual(possibles,[(4,3),(4,2),(4,1),(4,0)])

    def test_move_horizontal_left_with_own_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,2,Pawn('BLACK',board))
        possibles=possible_positions_hl(rook,4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_horizontal_left_with_enemy_piece_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        board.set_piece(4,2,Pawn('WHITE',board))
        possibles=possible_positions_hl(rook,4,4)
        self.assertEqual(possibles,[(4,3),(4,2)])


    # VALID POSITIONS:

    def test_valid_positions_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(4,4,rook)
        possible=rook.valid_positions(4,4)
        self.assertEqual(possible,[(5,4),(6,4),(7,4),(3,4),(2,4),(1,4),(0,4),(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0)])

    # DIAGONAL WRONG MOVES:

    def test_wrong_move_diagonal_desc_right_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,0,rook)
        possible_positions=rook.valid_positions(0,0)
        possible=rook.is_row_col_in_valid_positions(1,1,possible_positions)
        self.assertFalse(possible)
        
    def test_wrong_move_diagonal_desc_left_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,1,rook)
        possible_positions=rook.valid_positions(0,1)
        possible=rook.is_row_col_in_valid_positions(1,0,possible_positions)
        self.assertFalse(possible)

    def test_wrong_move_diagonal_asc_right_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        possible_positions=rook.valid_positions(1,1)
        possible=rook.is_row_col_in_valid_positions(0,2,possible_positions)
        self.assertFalse(possible)

    def test_wrong_move_diagonal_asc_left_rook(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        possible_positions=rook.valid_positions(1,1)
        possible=rook.is_row_col_in_valid_positions(0,0,possible_positions)
        self.assertFalse(possible)


if __name__=='__main__':
    unittest.main()