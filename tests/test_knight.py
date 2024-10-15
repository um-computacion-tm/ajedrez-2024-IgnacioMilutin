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
        possibles=knight.possible_positions_var(4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_right_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var(4,4)
        self.assertEqual(possibles,[(2,5)])

    def test_move_ascendant_right_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_var(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_right_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_var(4,4)
        self.assertEqual(possibles,[(2,5)])


    def test_move_ascendant_right_out_of_board_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(2,7,knight)
        possibles=knight.possible_positions_var(2,7)
        self.assertEqual(possibles,[])

    def test_move_ascendant_right_out_of_board_vertical(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,5,knight)
        possibles=knight.possible_positions_var(1,5)
        self.assertEqual(possibles,[])

    def test_move_ascendant_right_out_of_board_vertical_and_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,7,knight)
        possibles=knight.possible_positions_var(1,7)
        self.assertEqual(possibles,[])

    # ASCENDANT TO THE LEFT

    def test_move_ascendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_val(4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_left_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val(4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_val(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_ascendant_left_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(2,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_val(4,4)
        self.assertEqual(possibles,[(2,3)])

    def test_move_ascendant_left_out_of_board_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(2,0,knight)
        possibles=knight.possible_positions_val(2,0)
        self.assertEqual(possibles,[])

    def test_move_ascendant_left_out_of_board_vertical(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,5,knight)
        possibles=knight.possible_positions_val(1,5)
        self.assertEqual(possibles,[])

    def test_move_ascendant_left_out_of_board_vertical_and_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(1,0,knight)
        possibles=knight.possible_positions_val(1,0)
        self.assertEqual(possibles,[])

    # DESCENDANT TO THE RIGHT

    def test_move_descendant_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_vdr(4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_right_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr(4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdr(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_right_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,5,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdr(4,4)
        self.assertEqual(possibles,[(6,5)])

    def test_move_descendant_right_out_of_board_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,7,knight)
        possibles=knight.possible_positions_vdr(5,7)
        self.assertEqual(possibles,[])

    def test_move_descendant_right_out_of_board_vertical(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,5,knight)
        possibles=knight.possible_positions_vdr(6,5)
        self.assertEqual(possibles,[])

    def test_move_descendant_right_out_of_board_vertical_and_right(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,7,knight)
        possibles=knight.possible_positions_vdr(6,7)
        self.assertEqual(possibles,[])

    # DESCENDANT TO THE LEFT

    def test_move_descendant_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_vdl(4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_left_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl(4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("BLACK", board))
        possibles=knight.possible_positions_vdl(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_descendant_left_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(6,3,Pawn("WHITE", board))
        possibles=knight.possible_positions_vdl(4,4)
        self.assertEqual(possibles,[(6,3)])

    def test_move_descendant_left_out_of_board_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,0,knight)
        possibles=knight.possible_positions_vdl(5,0)
        self.assertEqual(possibles,[])

    def test_move_descendant_left_out_of_board_vertical(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,5,knight)
        possibles=knight.possible_positions_vdl(6,5)
        self.assertEqual(possibles,[])

    def test_move_descendant_left_out_of_board_vertical_and_left(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(6,0,knight)
        possibles=knight.possible_positions_vdl(6,0)
        self.assertEqual(possibles,[])


    # HORIZONTAL RIGHT AND ASCENDANT

    def test_move_horizontal_right_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_hra(4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_hra(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_ascendant_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_hra(4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_hra(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_ascendant_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_hra(4,4)
        self.assertEqual(possibles,[(3,6)])

    def test_move_horizontal_right_ascendant_out_of_board_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(0,5,knight)
        possibles=knight.possible_positions_hra(0,5)
        self.assertEqual(possibles,[])

    def test_move_horizontal_right_ascendant_out_of_board_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,6,knight)
        possibles=knight.possible_positions_hra(5,6)
        self.assertEqual(possibles,[])

    def test_move_horizontal_right_ascendant_out_of_board_ascendant_and_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(0,6,knight)
        possibles=knight.possible_positions_hra(0,6)
        self.assertEqual(possibles,[])

        # HORIZONTAL RIGHT AND DESCENDANT

    def test_move_horizontal_right_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_hrd(4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_hrd(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_descendant_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_hrd(4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("BLACK", board))
        possibles=knight.possible_positions_hrd(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_right_descendant_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,6,Pawn("WHITE", board))
        possibles=knight.possible_positions_hrd(4,4)
        self.assertEqual(possibles,[(5,6)])

    def test_move_horizontal_right_descendant_out_of_board_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(7,5,knight)
        possibles=knight.possible_positions_hrd(7,5)
        self.assertEqual(possibles,[])

    def test_move_horizontal_right_descendant_out_of_board_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,6,knight)
        possibles=knight.possible_positions_hrd(5,6)
        self.assertEqual(possibles,[])

    def test_move_horizontal_right_descendant_out_of_board_descendant_and_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(7,6,knight)
        possibles=knight.possible_positions_hrd(7,6)
        self.assertEqual(possibles,[])

    # HORIZONTAL LEFT AND ASCENDANT

    def test_move_horizontal_left_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_hla(4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_hla(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_ascendant_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_hla(4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_hla(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_ascendant_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(3,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_hla(4,4)
        self.assertEqual(possibles,[(3,2)])

    def test_move_horizontal_left_ascendant_out_of_board_ascendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(0,2,knight)
        possibles=knight.possible_positions_hla(0,2)
        self.assertEqual(possibles,[])

    def test_move_horizontal_left_ascendant_out_of_board_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,1,knight)
        possibles=knight.possible_positions_hla(5,1)
        self.assertEqual(possibles,[])

    def test_move_horizontal_left_ascendant_out_of_board_ascendant_and_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(0,1,knight)
        possibles=knight.possible_positions_hla(0,1)
        self.assertEqual(possibles,[])

    # HORIZONTAL LEFT AND DESCENDAT

    def test_move_horizontal_left_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        possibles=knight.possible_positions_hld(4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_white_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_hld(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_descendant_white_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_hld(4,4)
        self.assertEqual(possibles,[(5,2)])

    def test_move_horizontal_left_descendant_black_with_own_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("BLACK", board))
        possibles=knight.possible_positions_hld(4,4)
        self.assertEqual(possibles,[])
    
    def test_move_horizontal_left_descendant_black_with_enemy_piece_in_the_end(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        board.set_piece(5,2,Pawn("WHITE", board))
        possibles=knight.possible_positions_hld(4,4)
        self.assertEqual(possibles,[(5,2)])
    
    def test_move_horizontal_left_descendant_out_of_board_descendant(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(7,2,knight)
        possibles=knight.possible_positions_hld(7,2)
        self.assertEqual(possibles,[])

    def test_move_horizontal_left_descendant_out_of_board_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(5,1,knight)
        possibles=knight.possible_positions_hld(5,1)
        self.assertEqual(possibles,[])

    def test_move_horizontal_left_descendant_out_of_board_descendant_and_horizontal(self):
        board=Board(for_test=True)
        knight=Knight('WHITE',board)
        board.set_piece(7,1,knight)
        possibles=knight.possible_positions_hld(7,1)
        self.assertEqual(possibles,[])

    # VALID POSITIONS:

    def test_valid_positions_knight(self):
        board=Board(for_test=True)
        knight=Knight('BLACK',board)
        board.set_piece(4,4,knight)
        possible=knight.valid_positions(4,4)
        self.assertEqual(possible,[(2,5),(2,3),(6,5),(6,3),(3,6),(5,6),(3,2),(5,2)])

if __name__=='__main__':
    unittest.main()