import unittest
from unittest.mock import patch
from cli import play, InvalidMove
from chess import Chess
from board import Board
from pawn import Pawn
from exceptions import InvalidPawnChange

class TestCli(unittest.TestCase):

    # USER INPUTS FOR MOVING FROM ROW,COL TO ROW,COL

    @patch('builtins.input',side_effect=['6','0','5','0'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    def test_happy_path(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,2)
        self.assertEqual(mock_chess_move.call_count,1)

    @patch('builtins.input',side_effect=['hola','1','2','2'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    def test_wrong_entry_1(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,1)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,0)

    @patch('builtins.input',side_effect=['1','hola','2','2'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    def test_wrong_entry_2(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,2)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,0)

    @patch('builtins.input',side_effect=['1','1','hola','2'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    def test_wrong_entry_3(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,3)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,0)

    @patch('builtins.input',side_effect=['1','1','2','hola'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    def test_wrong_entry_4(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,0)

    @patch('builtins.input',side_effect=['1','1','2','2'])
    @patch('builtins.print')
    @patch.object(Chess,'move',side_effect=InvalidMove())
    def test_invalid_move(self,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,1)

    @patch('builtins.input',side_effect=['1','4','0','4','Queen'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    @patch.object(Chess,'pawn_change_action')
    @patch.object(Chess,'pawn_change_verification',return_value=True)
    def test_valid_pawn_change_entry(self,mock_chess_pawn_change_verification,mock_chess_pawn_change_action,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(1,4,Pawn("WHITE", board))
        play(chess)
        self.assertEqual(mock_input.call_count,5)
        self.assertEqual(mock_print.call_count,2)
        self.assertEqual(mock_chess_move.call_count,1)
        self.assertEqual(mock_chess_pawn_change_action.call_count,1)
        self.assertEqual(mock_chess_pawn_change_verification.call_count,1)
    
    @patch('builtins.input',side_effect=['1','4','0','4','hola','Queen'])
    @patch('builtins.print')
    @patch.object(Chess,'move')
    @patch.object(Chess,'pawn_change_action',side_effect=[InvalidPawnChange(), True])
    @patch.object(Chess,'pawn_change_verification',return_value=True)
    def test_non_valid_pawn_change_entry(self,mock_chess_pawn_change_verification,mock_chess_pawn_change_action,mock_chess_move,mock_print,mock_input):
        chess=Chess()
        board=Board(for_test=True)
        chess.__board__=board
        board.set_piece(1,4,Pawn("WHITE", board))
        play(chess)
        self.assertEqual(mock_input.call_count,6)
        self.assertEqual(mock_print.call_count,3)
        self.assertEqual(mock_chess_move.call_count,1)
        self.assertEqual(mock_chess_pawn_change_action.call_count,2)
        self.assertEqual(mock_chess_pawn_change_verification.call_count,1)


if __name__=='__main__':
    unittest.main()