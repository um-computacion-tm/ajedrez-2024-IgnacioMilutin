import unittest
from chess import Chess
from exceptions import EmptyPosition,InvalidTurn,InvalidMove

class TestChess(unittest.TestCase):

    # IS_PLAYING

    
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

    # TURNS TEST

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


if __name__=='__main__':
    unittest.main()