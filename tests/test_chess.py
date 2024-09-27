import unittest
from chess import Chess
from board import Board
from pawn import Pawn
from exceptions import EmptyPosition,InvalidTurn,InvalidMove

class TestChess(unittest.TestCase):

    # IS_PLAYING

    def test_is_playing(self):
        chess=Chess()
        self.assertTrue(chess.is_playing())
    
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

if __name__=='__main__':
    unittest.main()