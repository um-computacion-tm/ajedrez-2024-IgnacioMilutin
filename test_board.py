import unittest
from board import Board
from pieces import Rook

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board=Board()

    def test_str_board(self):
        board = Board()
        self.assertEqual(
            str(board),
            (
                "♖      ♖\n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "        \n"
                "♜      ♜\n"
            )
        )
        
    def test_get_piece(self):
        self.assertIsInstance(self.board.get_piece(0,0),Rook)
        self.assertIsNone(self.board.get_piece(2,0))

    def test_rooks_creation(self):
        self.assertIsInstance(self.board.get_piece(0,0),Rook)
        self.assertEqual(self.board.get_piece(0,0).__color__,'BLACK')
        self.assertEqual(self.board.get_piece(0,0).__name__,'rook1_black')
        self.assertIsInstance(self.board.get_piece(0,7),Rook)
        self.assertEqual(self.board.get_piece(0,7).__color__,'BLACK')
        self.assertEqual(self.board.get_piece(0,7).__name__,'rook2_black')
        self.assertIsInstance(self.board.get_piece(7,0),Rook)
        self.assertEqual(self.board.get_piece(7,0).__color__,'WHITE')
        self.assertEqual(self.board.get_piece(7,0).__name__,'rook2_white')
        self.assertIsInstance(self.board.get_piece(7,7),Rook)
        self.assertEqual(self.board.get_piece(7,7).__color__,'WHITE')
        self.assertEqual(self.board.get_piece(7,7).__name__,'rook1_white')

    def test_empty_spaces(self):
        self.assertIsNone(self.board.get_piece(2,0))
        self.assertIsNone(self.board.get_piece(2,1))
        self.assertIsNone(self.board.get_piece(2,2))
        self.assertIsNone(self.board.get_piece(2,3))
        self.assertIsNone(self.board.get_piece(2,4))
        self.assertIsNone(self.board.get_piece(2,5))
        self.assertIsNone(self.board.get_piece(2,6))
        self.assertIsNone(self.board.get_piece(2,7))
        self.assertIsNone(self.board.get_piece(3,0))
        self.assertIsNone(self.board.get_piece(3,1))
        self.assertIsNone(self.board.get_piece(3,2))
        self.assertIsNone(self.board.get_piece(3,3))
        self.assertIsNone(self.board.get_piece(3,4))
        self.assertIsNone(self.board.get_piece(3,5))
        self.assertIsNone(self.board.get_piece(3,6))
        self.assertIsNone(self.board.get_piece(3,7))
        self.assertIsNone(self.board.get_piece(4,0))
        self.assertIsNone(self.board.get_piece(4,1))
        self.assertIsNone(self.board.get_piece(4,2))
        self.assertIsNone(self.board.get_piece(4,3))
        self.assertIsNone(self.board.get_piece(4,4))
        self.assertIsNone(self.board.get_piece(4,5))
        self.assertIsNone(self.board.get_piece(4,6))
        self.assertIsNone(self.board.get_piece(4,7))
        self.assertIsNone(self.board.get_piece(5,0))
        self.assertIsNone(self.board.get_piece(5,1))
        self.assertIsNone(self.board.get_piece(5,2))
        self.assertIsNone(self.board.get_piece(5,3))
        self.assertIsNone(self.board.get_piece(5,4))
        self.assertIsNone(self.board.get_piece(5,5))
        self.assertIsNone(self.board.get_piece(5,6))
        self.assertIsNone(self.board.get_piece(5,7))