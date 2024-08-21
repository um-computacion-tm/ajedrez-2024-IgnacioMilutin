import unittest
from chess import Chess

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess=Chess()
        
    def test_first_turn(self):
        self.assertEqual(self.chess.turn(),'WHITE')

    def test_change_turn_white_to_black(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(),'BLACK')

    def test_change_turn_black_to_white(self):
        self.chess.__turn__='BLACK'
        self.chess.change_turn()
        self.assertEqual(self.chess.turn(),'WHITE')
