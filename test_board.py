import unittest
from board import Board
from pieces import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board()

    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0,0),Rook)
        self.assertIsNone(self.board.get_piece(2,0))

    def test_rooks_creation(self):
        self.assertIsInstance(self.board.get_piece(0,0),Rook)
        self.assertEqual(self.board.get_piece(0,0).__color__,'BLACK')
        self.assertIsInstance(self.board.get_piece(0,7),Rook)
        self.assertEqual(self.board.get_piece(0,7).__color__,'BLACK')
        self.assertIsInstance(self.board.get_piece(7,0),Rook)
        self.assertEqual(self.board.get_piece(7,0).__color__,'WHITE')
        self.assertIsInstance(self.board.get_piece(7,7),Rook)
        self.assertEqual(self.board.get_piece(7,7).__color__,'WHITE')