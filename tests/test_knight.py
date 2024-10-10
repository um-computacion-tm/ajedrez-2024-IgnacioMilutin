import unittest
from pieces import Piece
from pawn import Pawn
from board import Board
from knight import Knight

class TestKnight(unittest.TestCase):

    # STR:

    def test_str_white(self):
        board=Board()
        knight=Knight('WHITE',board)
        self.assertEqual(str(knight),'♞')

    def test_str_black(self):
        board=Board()
        knight=Knight('BLAck',board)
        self.assertEqual(str(knight),'♘')

    # ASCENDANT TO THE RIGHT

    def test_move_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("WHITE", board))
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("BLACK", board))
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("BLACK", board))
        board.set_piece(2,4,Pawn("WHITE", board))
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_right_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=possible_positions_var(knight,4,4)
        self.assertEqual(possibles,[(2,5)])

    # ASCENDANT TO THE LEFT

    def test_move_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("WHITE", board))
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("BLACK", board))
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,4,Pawn("BLACK", board))
        board.set_piece(2,4,Pawn("WHITE", board))
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_left_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=possible_positions_val(knight,4,4)
        self.assertEqual(possibles,[(2,3)])

    # DESCENDANT TO THE RIGHT

    def test_move_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("WHITE", board))
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("BLACK", board))
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("BLACK", board))
        board.set_piece(6,4,Pawn("WHITE", board))
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_right_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=possible_positions_vdr(knight,4,4)
        self.assertEqual(possibles,[(6,5)])

    # DESCENDANT TO THE LEFT

    def test_move_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("WHITE", board))
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("BLACK", board))
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,4,Pawn("BLACK", board))
        board.set_piece(6,4,Pawn("WHITE", board))
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_left_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=possible_positions_vdl(knight,4,4)
        self.assertEqual(possibles,[(6,3)])

    # HORIZONTAL RIGHT AND ASCENDANT

    def test_move_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("WHITE", board))
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("BLACK", board))
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("BLACK", board))
        board.set_piece(4,6,Pawn("WHITE", board))
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_ascendant_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        possibles=possible_positions_hra(knight,4,4)
        self.assertEqual(possibles,[(3,6)])

        # HORIZONTAL RIGHT AND DESCENDANT

    def test_move_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("WHITE", board))
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("BLACK", board))
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,5,Pawn("BLACK", board))
        board.set_piece(4,6,Pawn("WHITE", board))
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_descendant_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        possibles=possible_positions_hrd(knight,4,4)
        self.assertEqual(possibles,[(5,6)])

    # HORIZONTAL LEFT AND ASCENDANT

    def test_move_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("WHITE", board))
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("BLACK", board))
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("BLACK", board))
        board.set_piece(4,2,Pawn("WHITE", board))
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_ascendant_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        possibles=possible_positions_hla(knight,4,4)
        self.assertEqual(possibles,[(3,2)])

    # HORIZONTAL LEFT AND DESCENDAT

    def test_move_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_with_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("WHITE", board))
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_with_enemy_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("BLACK", board))
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_with_enemy_and_own_piece_in_the_middle(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(4,3,Pawn("BLACK", board))
        board.set_piece(4,2,Pawn("WHITE", board))
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_descendant_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        possibles=possible_positions_hld(knight,4,4)
        self.assertEqual(possibles,[(5,2)])

    # VALID POSITIONS:

    def test_valid_positions_rook(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        possible=knight.valid_positions(4,4)
        self.assertEqual(possible,[(2,5),(2,3),(6,5),(6,3),(3,6),(5,6),(3,2),(5,2)])