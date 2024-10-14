import unittest
from king import King
from board import Board
from pawn import Pawn
from knight import Knight

class TestKing(unittest.TestCase):

    # STR

    def test_str_white(self):
        board=Board()
        king=King('WHITE',board)
        self.assertEqual(str(king),'♚')

    def test_str_black(self):
        board=Board()
        king=King('BLACK',board)
        self.assertEqual(str(king),'♔')

    # VERTICAL ASCENDANT ONE BOX MOVE

    def test_move_vertical_ascendant(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_va(4,4)
        self.assertEqual(possibles,[(3,4)])

    def test_move_white_piece_vertical_ascendant_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,4,Pawn("BLACK", board))
        possibles=king.possible_positions_va(4,4)
        self.assertEqual(possibles,[(3,4)])

    def test_move_black_piece_vertical_ascendant_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,4,Pawn("WHITE", board))
        possibles=king.possible_positions_va(4,4)
        self.assertEqual(possibles,[(3,4)])

    def test_move_white_piece_vertical_ascendant_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,4,Pawn("WHITE", board))
        possibles=king.possible_positions_va(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_vertical_ascendant_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,4,Pawn("BLACK", board))
        possibles=king.possible_positions_va(4,4)
        self.assertEqual(possibles,[])

    # VERTICAL DESCENDANT ONE BOX MOVE

    def test_move_vertical_descendant(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_vd(4,4)
        self.assertEqual(possibles,[(5,4)])

    def test_move_white_piece_vertical_descendant_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,4,Pawn("BLACK", board))
        possibles=king.possible_positions_vd(4,4)
        self.assertEqual(possibles,[(5,4)])

    def test_move_black_piece_vertical_descendant_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,4,Pawn("WHITE", board))
        possibles=king.possible_positions_vd(4,4)
        self.assertEqual(possibles,[(5,4)])

    def test_move_white_piece_vertical_descendant_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,4,Pawn("WHITE", board))
        possibles=king.possible_positions_vd(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_vertical_descendant_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,4,Pawn("BLACK", board))
        possibles=king.possible_positions_vd(4,4)
        self.assertEqual(possibles,[])

    # HORIZONTAL RIGHT ONE BOX MOVE

    def test_move_horizontal_right(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_white_piece_horizontal_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(4,5,Pawn("BLACK", board))
        possibles=king.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_black_piece_horizontal_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(4,5,Pawn("WHITE", board))
        possibles=king.possible_positions_hr(4,4)
        self.assertEqual(possibles,[(4,5)])

    def test_move_white_piece_horizontal_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(4,5,Pawn("WHITE", board))
        possibles=king.possible_positions_hr(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_horizontal_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(4,5,Pawn("BLACK", board))
        possibles=king.possible_positions_hr(4,4)
        self.assertEqual(possibles,[])

    # HORIZONTAL LEFT ONE BOX MOVE

    def test_move_horizontal_left(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_white_piece_horizontal_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(4,3,Pawn("BLACK", board))
        possibles=king.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_black_piece_horizontal_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(4,3,Pawn("WHITE", board))
        possibles=king.possible_positions_hl(4,4)
        self.assertEqual(possibles,[(4,3)])

    def test_move_white_piece_horizontal_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(4,3,Pawn("WHITE", board))
        possibles=king.possible_positions_hl(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_horizontal_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(4,3,Pawn("BLACK", board))
        possibles=king.possible_positions_hl(4,4)
        self.assertEqual(possibles,[])

    # DIAGONAL ASCENDANT RIGHT ONE BOX MOVE

    def test_move_diagonal_ascendant_right(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_dar(4,4)
        self.assertEqual(possibles,[(3,5)])

    def test_move_white_piece_diagonal_ascendant_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,5,Pawn("BLACK", board))
        possibles=king.possible_positions_dar(4,4)
        self.assertEqual(possibles,[(3,5)])

    def test_move_black_piece_diagonal_ascendant_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,5,Pawn("WHITE", board))
        possibles=king.possible_positions_dar(4,4)
        self.assertEqual(possibles,[(3,5)])

    def test_move_white_piece_diagonal_ascendant_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,5,Pawn("WHITE", board))
        possibles=king.possible_positions_dar(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_diagonal_ascendant_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,5,Pawn("BLACK", board))
        possibles=king.possible_positions_dar(4,4)
        self.assertEqual(possibles,[])

    # DIAGONAL ASCENDANT LEFT ONE BOX MOVE

    def test_move_diagonal_ascendant_left(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_dal(4,4)
        self.assertEqual(possibles,[(3,3)])

    def test_move_white_piece_diagonal_ascendant_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,3,Pawn("BLACK", board))
        possibles=king.possible_positions_dal(4,4)
        self.assertEqual(possibles,[(3,3)])

    def test_move_black_piece_diagonal_ascendant_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,3,Pawn("WHITE", board))
        possibles=king.possible_positions_dal(4,4)
        self.assertEqual(possibles,[(3,3)])

    def test_move_white_piece_diagonal_ascendant_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(3,3,Pawn("WHITE", board))
        possibles=king.possible_positions_dal(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_diagonal_ascendant_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(3,3,Pawn("BLACK", board))
        possibles=king.possible_positions_dal(4,4)
        self.assertEqual(possibles,[])

    # DIAGONAL DESCENDANT RIGHT ONE BOX MOVE

    def test_move_diagonal_descendant_right(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_ddr(4,4)
        self.assertEqual(possibles,[(5,5)])

    def test_move_white_piece_diagonal_descendant_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,5,Pawn("BLACK", board))
        possibles=king.possible_positions_ddr(4,4)
        self.assertEqual(possibles,[(5,5)])

    def test_move_black_piece_diagonal_descendant_right_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,5,Pawn("WHITE", board))
        possibles=king.possible_positions_ddr(4,4)
        self.assertEqual(possibles,[(5,5)])

    def test_move_white_piece_diagonal_descendant_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,5,Pawn("WHITE", board))
        possibles=king.possible_positions_ddr(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_diagonal_descendant_right_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,5,Pawn("BLACK", board))
        possibles=king.possible_positions_ddr(4,4)
        self.assertEqual(possibles,[])

    # DIAGONAL DESCENDANT LEFT ONE BOX MOVE

    def test_move_diagonal_descendant_left(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        possibles=king.possible_positions_ddl(4,4)
        self.assertEqual(possibles,[(5,3)])

    def test_move_white_piece_diagonal_descendant_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,3,Pawn("BLACK", board))
        possibles=king.possible_positions_ddl(4,4)
        self.assertEqual(possibles,[(5,3)])

    def test_move_black_piece_diagonal_descendant_left_with_enemy_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,3,Pawn("WHITE", board))
        possibles=king.possible_positions_ddl(4,4)
        self.assertEqual(possibles,[(5,3)])

    def test_move_white_piece_diagonal_descendant_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('WHITE',board)
        board.set_piece(4,4,king)
        board.set_piece(5,3,Pawn("WHITE", board))
        possibles=king.possible_positions_ddl(4,4)
        self.assertEqual(possibles,[])

    def test_move_black_piece_diagonal_descendant_left_with_own_piece(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,3,Pawn("BLACK", board))
        possibles=king.possible_positions_ddl(4,4)
        self.assertEqual(possibles,[])

    # VALID_POSITIONS
    
    def test_valid_positions_king_no_danger(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(4,3),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_vertical_ascendant(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(1,5,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(5,4),(4,5),(4,3),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_vertical_descendant(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(7,3,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(4,5),(4,3),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_horizontal_right(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,7,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,3),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_horizontal_left(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,1,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_diagonal_ascendant_right(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(1,6,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(4,3),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_diagonal_ascendant_left(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(1,2,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(4,3),(3,5),(5,5),(5,3)])

    def test_valid_positions_king_danger_diagonal_descendant_right(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(7,6,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(4,3),(3,5),(3,3),(5,3)])

    def test_valid_positions_king_danger_diagonal_descendant_left(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(7,2,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(4,5),(4,3),(3,5),(3,3),(5,5)])

    def test_valid_positions_king_danger_vertical_two_sides(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(1,5,Knight("WHITE", board))
        board.set_piece(7,3,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(4,5),(4,3),(3,5),(3,3),(5,5),(5,3)])

    def test_valid_positions_king_danger_horizontal_two_sides(self):
        board=Board(for_test=True)
        king=King('BLACK',board)
        board.set_piece(4,4,king)
        board.set_piece(5,7,Knight("WHITE", board))
        board.set_piece(5,1,Knight("WHITE", board))
        possible=king.valid_positions(4,4)
        self.assertEqual(possible,[(3,4),(5,4),(3,5),(3,3),(5,5),(5,3)])