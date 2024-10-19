import unittest
from unittest.mock import patch
from chess import Chess
from pawn import Pawn
from board import Board
from king import King
from queen import Queen
from bishop import Bishop
from rook import Rook
from knight import Knight
from exceptions import EmptyPosition,InvalidTurn,InvalidMove,InvalidPawnChange

class TestChess(unittest.TestCase):

    # IS_PLAYING

    def test_is_playing(self):
        chess=Chess()
        self.assertTrue(chess.is_playing())

    # END_AGME

    def test_end_game(self):
        chess=Chess()
        self.assertFalse(chess.end_game())
    
    # MOVE

    def test_move_with_empty_position(self):
        chess=Chess()
        with self.assertRaises(EmptyPosition) as exc:
            chess.move(4,4,5,4)
        self.assertEqual(exc.exception.message,"La posicion esta vacia")

    def test_move_with_wrong_turn(self):
        chess=Chess()
        with self.assertRaises(InvalidMove) as exc:
            chess.move(0,0,2,2)
        self.assertEqual(exc.exception.message,"No puedes mover pieza de otro jugador")
    
    def test_move_with_move_to_an_invalid_position(self):
        chess=Chess()
        with self.assertRaises(InvalidMove) as exc:
            chess.move(7,0,5,1)
        self.assertEqual(exc.exception.message,"Movimieto de pieza invalido")

    def test_move_good_path(self):
        chess=Chess()
        chess.move(6,4,5,4)
        self.assertIsInstance(chess.__board__.get_piece(5,4),Pawn)
        self.assertEqual(chess.turn(),'BLACK')

    def test_move_moving_a_king(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(4,4,King('WHITE',board))
        chess.move(4,4,5,4)
        self.assertIsInstance(chess.__board__.get_piece(5,4),King)
        self.assertEqual(chess.turn(),'BLACK')

    # TURNS TEST

    def test_turn_method(self):
        chess=Chess()
        chess.__turn__='BLACK'
        self.assertEqual(chess.turn(),'BLACK')

    def test_first_turn(self):
        chess=Chess()
        self.assertEqual(chess.turn(),'WHITE')

    def test_change_turn_white_to_black(self):
        chess=Chess()
        chess.change_turn()
        self.assertEqual(chess.turn(),'BLACK')

    def test_change_turn_black_to_white(self):
        chess=Chess()
        chess.__turn__='BLACK'
        chess.change_turn()
        self.assertEqual(chess.turn(),'WHITE')

    # GET NEXT TURN

    def test_get_next_turn_actual_turn_white(self):
        chess=Chess()
        self.assertEqual(chess.get_next_turn(),'BLACK')

    def test_get_next_turn_actual_turn_black(self):
        chess=Chess()
        chess.__turn__='BLACK'
        self.assertEqual(chess.get_next_turn(),'WHITE')

    # SHOW BOARD

    def test_show_board(self):
        chess=Chess()
        self.assertEqual(chess.show_board(),
            (
                "    0   1   2   3   4   5   6   7\n"
                "  ---------------------------------\n"
                "0 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ | \n"
                "  ---------------------------------\n"
                "1 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | \n"
                "  ---------------------------------\n"
                "2 |   |   |   |   |   |   |   |   | \n"
                "  ---------------------------------\n"
                "3 |   |   |   |   |   |   |   |   | \n"
                "  ---------------------------------\n"
                "4 |   |   |   |   |   |   |   |   | \n"
                "  ---------------------------------\n"
                "5 |   |   |   |   |   |   |   |   | \n"
                "  ---------------------------------\n"
                "6 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | \n"
                "  ---------------------------------\n"
                "7 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ | \n"
                "  ---------------------------------\n"
            ))
        
    # PAWN_CHANGE_VERIFICATION

    def test_pawn_verification_its_a_pawn_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,Pawn("BLACK", board))
        self.assertTrue(chess.pawn_change_verification(7,4))
    
    def test_pawn_verification_its_a_pawn_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        self.assertTrue(chess.pawn_change_verification(0,4))

    def test_pawn_verification_its_not_a_pawn_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,King("BLACK", board))
        self.assertFalse(chess.pawn_change_verification(0,4))

    def test_pawn_verification_its_not_a_pawn_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,King("WHITE", board))
        self.assertFalse(chess.pawn_change_verification(7,4))

    def test_pawn_verification_its_a_pawn_white_piece_change_not_in_the_end(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(1,4,Pawn("WHITE", board))
        self.assertFalse(chess.pawn_change_verification(1,4))

    def test_pawn_verification_its_a_pawn_black_piece_change_not_in_the_end(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(6,4,Pawn("BLACK", board))
        self.assertFalse(chess.pawn_change_verification(6,4))

    # PAWN_CHANGE_ACTION

    def test_pawn_action_convert_to_queen_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,Pawn("BLACK", board))
        chess.pawn_change_action('Queen',7,4)
        self.assertIsInstance(board.get_piece(7,4),Queen)
        self.assertEqual(board.get_piece(7,4).get_color(),'BLACK')

    def test_pawn_action_convert_to_bishop_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,Pawn("BLACK", board))
        chess.pawn_change_action('Bishop',7,4)
        self.assertIsInstance(board.get_piece(7,4),Bishop)
        self.assertEqual(board.get_piece(7,4).get_color(),'BLACK')

    def test_pawn_action_convert_to_rook_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,Pawn("BLACK", board))
        chess.pawn_change_action('Rook',7,4)
        self.assertIsInstance(board.get_piece(7,4),Rook)
        self.assertEqual(board.get_piece(7,4).get_color(),'BLACK')

    def test_pawn_action_convert_to_knight_black_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(7,4,Pawn("BLACK", board))
        chess.pawn_change_action('Knight',7,4)
        self.assertIsInstance(board.get_piece(7,4),Knight)
        self.assertEqual(board.get_piece(7,4).get_color(),'BLACK')

    def test_pawn_action_convert_to_queen_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        chess.pawn_change_action('Queen',0,4)
        self.assertIsInstance(board.get_piece(0,4),Queen)
        self.assertEqual(board.get_piece(0,4).get_color(),'WHITE')

    def test_pawn_action_convert_to_bishop_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        chess.pawn_change_action('Bishop',0,4)
        self.assertIsInstance(board.get_piece(0,4),Bishop)
        self.assertEqual(board.get_piece(0,4).get_color(),'WHITE')

    def test_pawn_action_convert_to_rook_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        chess.pawn_change_action('Rook',0,4)
        self.assertIsInstance(board.get_piece(0,4),Rook)
        self.assertEqual(board.get_piece(0,4).get_color(),'WHITE')


    def test_pawn_action_convert_to_knight_white_piece_change(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        chess.pawn_change_action('Knight',0,4)
        self.assertIsInstance(board.get_piece(0,4),Knight)
        self.assertEqual(board.get_piece(0,4).get_color(),'WHITE')

    def test_pawn_action_wrong_entry(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(0,4,Pawn("WHITE", board))
        with self.assertRaises(InvalidPawnChange) as exc:
            chess.pawn_change_action('hola',0,4)
        self.assertEqual(exc.exception.message,"Cant change pawn for the given input, please select one of the granted options(Queen, Bishop, Rook or Knight): ")

    # END_GAME 

    @patch('builtins.print')
    def test_end_game_due_to_no_piece_rule_white_wins(self,mock_print):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(5,4,Pawn("WHITE", board))
        chess.move(5,4,4,4)
        execution=chess.end_due_to_no_piece_rule()
        self.assertFalse(execution)
        mock_print.assert_called_with('BLACK ran out of pieces. ¡WHITE WINS THE GAME!')

    @patch('builtins.print')
    def test_end_game_due_to_no_piece_rule_black_wins(self,mock_print):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        chess.__turn__='BLACK'
        board.set_piece(3,4,Pawn("BLACK", board))
        chess.move(3,4,4,4)
        execution=chess.end_due_to_no_piece_rule()
        self.assertFalse(execution)
        mock_print.assert_called_with('WHITE ran out of pieces. ¡BLACK WINS THE GAME!')

    def test_end_game_due_to_no_piece_rule_white_dont_win(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(5,4,Pawn("WHITE", board))
        board.set_piece(3,4,Pawn("BLACK", board))
        chess.move(5,4,4,4)
        execution=chess.end_due_to_no_piece_rule()
        self.assertTrue(execution)

    def test_end_game_due_to_no_piece_rule_black_dont_win(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        chess.__turn__='BLACK'
        board.set_piece(5,4,Pawn("WHITE", board))
        board.set_piece(3,4,Pawn("BLACK", board))
        chess.move(3,4,4,4)
        execution=chess.end_due_to_no_piece_rule()
        self.assertTrue(execution)
        

if __name__=='__main__':
    unittest.main()