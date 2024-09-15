import unittest
from chess import Chess
from exceptions import EmptyPosition,InvalidTurn,InvalidMove

class TestChess(unittest.TestCase):
    
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

    # MOVE


if __name__=='__main__':
    unittest.main()