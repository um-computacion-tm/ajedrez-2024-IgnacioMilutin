import unittest
from chess import Chess
from board import Board
from pawn import Pawn
from rook import Rook
from bishop import Bishop
from king import King
from moves import all_moves

class TestMoves(unittest.TestCase):

    # ALL POSSIBLE MOVES FOR ALL PIECES OF A COLOR

    def test_all_moves_black(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(4,1,Pawn("BLACK", board))
        board.set_piece(0,7,Bishop("BLACK", board))
        board.set_piece(0,0,Rook("BLACK", board))
        positions=all_moves(board,'BLACK')
        self.assertEqual(positions,[(1,0),(2,0),(3,0),(4,0),(5,0),(6,0),(7,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6),(1,6),(2,5),(3,4),(4,3),(5,2),(6,1),(7,0),(5,1)])

    def test_all_moves_white(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(4,1,Pawn("WHITE", board))
        board.set_piece(7,7,Bishop("WHITE", board))
        board.set_piece(7,0,Rook("WHITE", board))
        positions=all_moves(board,'WHITE')
        self.assertEqual(positions,[(3,1),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)])

    def test_all_moves_with_king(self):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(1,4,King("WHITE", board))
        board.set_piece(4,1,Pawn("WHITE", board))
        board.set_piece(7,7,Bishop("WHITE", board))
        board.set_piece(7,0,Rook("WHITE", board))
        positions=all_moves(board,'WHITE')
        self.assertEqual(positions,[(0,4),(2,4),(1,5),(1,3),(0,5),(0,3),(2,5),(2,3),(3,1),(6,0),(5,0),(4,0),(3,0),(2,0),(1,0),(0,0),(7,1),(7,2),(7,3),(7,4),(7,5),(7,6),(6,6),(5,5),(4,4),(3,3),(2,2),(1,1),(0,0)])

if __name__=='__main__':
    unittest.main()