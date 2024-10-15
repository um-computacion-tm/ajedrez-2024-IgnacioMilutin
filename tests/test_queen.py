import unittest
from pieces import Piece
from pawn import Pawn
from board import Board
from queen import Queen
from moves import possible_positions_dar, possible_positions_dal, possible_positions_ddr, possible_positions_ddl, possible_positions_hl, possible_positions_hr, possible_positions_va,possible_positions_vd

class TestQueen(unittest.TestCase):

    # STR

    def test_str_white(self):
        board=Board()
        queen=Queen('WHITE',board)
        self.assertEqual(str(queen),'♛')

    def test_str_black(self):
        board=Board()
        queen=Queen('BLAck',board)
        self.assertEqual(str(queen),'♕')

    # DIAGONAL ASCENDANT TO THE RIGHT:

    def test_move_diagonal_ascendant_right(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(4,4,queen)
        possibles=possible_positions_dar(queen,4,4)
        self.assertEqual(possibles,[(3,5),(2,6),(1,7)])
    
    def test_move_diagonal_ascendant_right_with_own_pieces(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4, queen)
        board.set_piece(2,6,Pawn("BLACK", board))
        possibles = possible_positions_dar(queen,4, 4)
        self.assertEqual(
            possibles,
            [(3,5)]
        )

    def test_move_diagonal_ascendant_right_with_enemy_piece(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4, queen)
        board.set_piece(2,6,Pawn("WHITE", board))
        possibles = possible_positions_dar(queen,4, 4)
        self.assertEqual(
            possibles,
            [(3, 5),(2,6)]
        )

    # DIAGONAL ASCENDANT TO THE LEFT:

    def test_move_diagonal_ascendant_left(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(4,3,queen)
        possibles=possible_positions_dal(queen,4,3)
        self.assertEqual(possibles,[(3,2),(2,1),(1,0)])
    
    def test_move_diagonal_ascendant_left_with_own_pieces(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(1,1,Pawn("BLACK", board))
        possibles = possible_positions_dal(queen,4, 4)
        self.assertEqual(
            possibles,
            [(3,3),(2,2)]
        )

    def test_move_diagonal_ascendant_left_with_enemy_piece(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4, queen)
        board.set_piece(1,1,Pawn("WHITE", board))
        possibles = possible_positions_dal(queen,4, 4)
        self.assertEqual(
            possibles,
            [(3,3),(2,2),(1,1)]
        )
        

    # DIAGONAL DESCENDANT TO THE RIGHT:

    def test_move_diagonal_descendant_right(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(3,4,queen)
        possibles=possible_positions_ddr(queen,3,4)
        self.assertEqual(possibles,[(4,5),(5,6),(6,7)])
    
    def test_move_diagonal_descendant_right_with_own_pieces(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(6,6,Pawn("BLACK", board))
        possibles = possible_positions_ddr(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5,5)]
        )

    def test_move_diagonal_descendant_right_with_enemy_piece(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(6,6,Pawn("WHITE", board))
        possibles = possible_positions_ddr(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5, 5),(6,6)]
        )

    # DIAGONAL DESCENDANT TO THE LEFT:

    def test_move_diagonal_descendant_left(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(3,3,queen)
        possibles=possible_positions_ddl(queen,3,3)
        self.assertEqual(possibles,[(4,2),(5,1),(6,0)])
    
    def test_move_diagonal_descendant_left_with_own_pieces(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(6,2,Pawn("BLACK", board))
        possibles = possible_positions_ddl(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5,3)]
        )

    def test_move_diagonal_descendant_left_with_enemy_piece(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(6,2,Pawn("WHITE", board))
        possibles = possible_positions_ddl(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5, 3),(6,2)])
        
    #VERTICAL DESCENDANT:

    def test_move_vertical_desc(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(0,4,queen)
        possibles=possible_positions_vd(queen,0,4)
        self.assertEqual(possibles,[(1,4),(2,4),(3,4),(4,4),(5,4),(6,4),(7,4)])
    
    def test_move_vertical_desc_with_own_pieces(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(7,4,Pawn("BLACK", board))
        possibles = possible_positions_vd(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4)]
        )

    def test_move_vertical_desc_with_enemy_piece(self):
        board = Board(for_test=True)
        queen = Queen("BLACK", board)
        board.set_piece(4,4,queen)
        board.set_piece(7,4,Pawn("WHITE", board))
        possibles = possible_positions_vd(queen,4, 4)
        self.assertEqual(
            possibles,
            [(5, 4),(6,4),(7,4)]
        )
        
    # VERTICAL ASCENDANT: 

    def test_move_vertical_asc(self):
        board=Board(for_test=True)
        queen=Queen('WHITE',board)
        board.set_piece(7,4,queen)
        possibles=possible_positions_va(queen,7,4)
        self.assertEqual(possibles,[(6,4),(5,4),(4,4),(3,4),(2,4),(1,4),(0,4)])

    def test_move_vertical_asc_with_own_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(5,5,queen)
        board.set_piece(3,5,Pawn('BLACK',board))
        possibles=possible_positions_va(queen,5,5)
        self.assertEqual(possibles,[(4,5)])
        
    def test_move_vertical_asc_with_enemy_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(5,5,queen)
        board.set_piece(3,5,Pawn('WHITE',board))
        possibles=possible_positions_va(queen,5,5)
        self.assertEqual(possibles,[(4,5),(3,5)])

    # HORIZONTAL RIGHT:

    def test_move_horizontal_right(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        possibles=possible_positions_hr(queen,4,4)
        self.assertEqual(possibles,[(4,5),(4,6),(4,7)])

    def test_move_horizontal_right_with_own_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        board.set_piece(4,6,Pawn('BLACK',board))
        possibles=possible_positions_hr(queen,4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_horizontal_right_with_enemy_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        board.set_piece(4,6,Pawn('WHITE',board))
        possibles=possible_positions_hr(queen,4,4)
        self.assertEqual(possibles,[(4,5),(4,6)])

    # HORIZONTAL LEFT:

    def test_move_horizontal_left(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        possibles=possible_positions_hl(queen,4,4)
        self.assertEqual(possibles,[(4,3),(4,2),(4,1),(4,0)])

    def test_move_horizontal_left_with_own_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        board.set_piece(4,2,Pawn('BLACK',board))
        possibles=possible_positions_hl(queen,4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_horizontal_left_with_enemy_piece(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        board.set_piece(4,2,Pawn('WHITE',board))
        possibles=possible_positions_hl(queen,4,4)
        self.assertEqual(possibles,[(4,3),(4,2)])

    # VALID POSITIONS:

    def test_valid_positions_queen(self):
        board=Board(for_test=True)
        queen=Queen('BLACK',board)
        board.set_piece(4,4,queen)
        possible=queen.valid_positions(4,4)
        self.assertEqual(possible,[(5,4),(6,4),(7,4),(3,4),(2,4),(1,4),(0,4),(4,5),(4,6),(4,7),(4,3),(4,2),(4,1),(4,0),(3,5),(2,6),(1,7),(3,3),(2,2),(1,1),(0,0),(5,5),(6,6),(7,7),(5,3),(6,2),(7,1)])

if __name__=='__main__':
    unittest.main()