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

    # VERTICAL DESCENDANT RIGHT AND HORIZONTAL RIGHT DESCENDANT TOGETHER

    def test_move_vertical_descendant_right_and_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_with_only_vertical_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,6,knight)
        possibles=knight.possible_positions_vdr_and_hrd(4,6)
        self.assertEqual(possibles,[(6,7)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_with_only_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,4,knight)
        possibles=knight.possible_positions_vdr_and_hrd(6,4)
        self.assertEqual(possibles,[(7,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_own_piece_in_the_end_in_vertical_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_own_piece_in_the_end_in_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_enemy_piece_in_the_end_in_vertical_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_enemy_piece_in_the_end_in_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_white_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_own_piece_in_the_end_in_vertical_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_own_piece_in_the_end_in_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_enemy_piece_in_the_end_in_vertical_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_enemy_piece_in_the_end_in_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    def test_move_vertical_descendant_right_and_horizontal_right_descendant_black_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr_and_hrd(4,4)
        self.assertEqual(possibles,[(6,5),(5,6)])

    # VERTICAL DESCENDANT TO THE LEFT AND HORIZONTAL LEFT AND DESCENDANT TOGETHER

    def test_move_vertical_descendant_left_and_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_with_only_vertical_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,1,knight)
        possibles=knight.possible_positions_vdl_and_hld(4,1)
        self.assertEqual(possibles,[(6,0)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_with_only_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,4,knight)
        possibles=knight.possible_positions_vdl_and_hld(6,4)
        self.assertEqual(possibles,[(7,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_own_piece_in_the_end_in_vertical_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_own_piece_in_the_end_in_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_enemy_piece_in_the_end_in_vertical_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_enemy_piece_in_the_end_in_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_white_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_own_piece_in_the_end_in_vertical_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_own_piece_in_the_end_in_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_enemy_piece_in_the_end_in_vertical_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_enemy_piece_in_the_end_in_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])

    def test_move_vertical_descendant_left_and_horizontal_left_descendant_black_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl_and_hld(4,4)
        self.assertEqual(possibles,[(6,3),(5,2)])


    # VERTICAL ASCENDANT TO THE LEFT AND HORIZONTAL LEFT AND ASCENDANT TOGETHER

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_with_only_vertical_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,1,knight)
        possibles=knight.possible_positions_val_and_hla(4,1)
        self.assertEqual(possibles,[(2,0)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_with_only_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,4,knight)
        possibles=knight.possible_positions_val_and_hla(1,4)
        self.assertEqual(possibles,[(0,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_own_piece_in_the_end_in_vertical_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_own_piece_in_the_end_in_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_enemy_piece_in_the_end_in_vertical_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_enemy_piece_in_the_end_in_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_white_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_own_piece_in_the_end_in_vertical_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_own_piece_in_the_end_in_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_enemy_piece_in_the_end_in_vertical_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_enemy_piece_in_the_end_in_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    def test_move_vertical_ascendant_left_and_horizontal_left_ascendant_black_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val_and_hla(4,4)
        self.assertEqual(possibles,[(2,3),(3,2)])

    # VERTICAL ASCENDANT RIGHT AND HORIZONTAL RIGHT ASCENDANT TOGETHER

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_with_only_vertical_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,6,knight)
        possibles=knight.possible_positions_var_and_hra(4,6)
        self.assertEqual(possibles,[(2,7)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_with_only_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,4,knight)
        possibles=knight.possible_positions_var_and_hra(1,4)
        self.assertEqual(possibles,[(0,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_own_piece_in_the_end_in_vertical_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_own_piece_in_the_end_in_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_enemy_piece_in_the_end_in_vertical_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_enemy_piece_in_the_end_in_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_white_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_own_piece_in_the_end_in_vertical_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_own_piece_in_the_end_in_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_own_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_enemy_piece_in_the_end_in_vertical_ascendant_right(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_enemy_piece_in_the_end_in_horizontal_right_ascendantt(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    def test_move_vertical_ascendant_right_and_horizontal_right_ascendant_black_piece_with_enemy_piece_in_the_end_in_both_ends(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var_and_hra(4,4)
        self.assertEqual(possibles,[(2,5),(3,6)])

    # VALID POSITIONS:

    def test_valid_positions_knight(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        possible=knight.valid_positions(4,4)
        self.assertEqual(possible,[(2,5),(3,6),(2,3),(3,2),(6,5),(5,6),(6,3),(5,2)])

if __name__=='__main__':
    unittest.main()