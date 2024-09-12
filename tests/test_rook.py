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

    # DIAGONAL WORNG MOVES:

    def test_move_diagonal_desc_right(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,0,rook)
        is_possible=rook.valid_positions(0,0,1,1)
        self.assertFalse(is_possible)
        
    def test_move_diagonal_desc_left(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(0,1,rook)
        is_possible=rook.valid_positions(0,1,1,0)
        self.assertFalse(is_possible)

    def test_move_diagonal_asc_right(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        is_possible=rook.valid_positions(1,1,0,2)
        self.assertFalse(is_possible)

    def test_move_diagonal_asc_left(self):
        board=Board(for_test=True)
        rook=Rook('BLACK',board)
        board.set_piece(1,1,rook)
        is_possible=rook.valid_positions(1,1,0,0)
        self.assertFalse(is_possible)

if __name__=='__main__':
    unittest.main()