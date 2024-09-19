import unittest
from pawn import Pawn
from board import Board

class TestPawn(unittest.TestCase):

    # STR

    def test_str_white(self):
        board=Board()
        pawn=Pawn('WHITE',board)
        self.assertEqual(str(pawn),'♟')

    def test_str_black(self):
        board=Board()
        pawn=Pawn('BLACK',board)
        self.assertEqual(str(pawn),'♙')

    # POSSIBLE POSITIONS MOVE
    
    def test_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(1,4,pawn)
        possibles = pawn.possible_positions_move(1,4)
        self.assertEqual(
            possibles,
            [(2,4),(3,4)]
        )

    def test_not_initial_black(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(2,4,pawn)
        possibles = pawn.possible_positions_move(2,4)
        self.assertEqual(
            possibles,
            [(3, 4)]
        )

    def test_initial_black_block_by_own_piece(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(1,4,pawn)
        board.set_piece(3,4, Pawn("BLACK", board))
        possibles = pawn.possible_positions_move(1, 4)
        self.assertEqual(
            possibles,
            [(2,4)]
        )

    def test_not_initial_black_block_by_own_piece(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(2,4,pawn)
        board.set_piece(3,4, Pawn("BLACK", board))
        possibles = pawn.possible_positions_move(2, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_initial_black_block_by_enemy_piece(self):
        board=Board(for_test=True)
        pawn=Pawn('BLACK',board)
        board.set_piece(1,4,pawn)
        board.set_piece(3,4,Pawn('WHITE',board))
        possibles=pawn.possible_positions_move(1,4)
        self.assertEqual(possibles,[(2,4)])

    def test_not_initial_black_block_by_enemy_piece(self):
        board=Board(for_test=True)
        pawn=Pawn('BLACK',board)
        board.set_piece(2,4,pawn)
        board.set_piece(3,4,Pawn('WHITE',board))
        possibles=pawn.possible_positions_move(2,4)
        self.assertEqual(possibles,[])

    def test_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(6,4,pawn)
        possibles = pawn.possible_positions_move(6, 4)
        self.assertEqual(
            possibles,
            [(5, 4), (4, 4)]
        )

    def test_not_initial_white(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(5,4,pawn)
        possibles = pawn.possible_positions_move(5, 4)
        self.assertEqual(
            possibles,
            [(4, 4)]
        )

    def test_initial_white_block_by_own_piece(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(6,4,pawn)
        board.set_piece(4, 4, Pawn("WHITE", board))
        possibles = pawn.possible_positions_move(6, 4)
        self.assertEqual(
            possibles,
            [(5,4)]
        )

    def test_not_initial_white_block_by_own_piece(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(5,4,pawn)
        board.set_piece(4, 4, Pawn("WHITE", board))
        possibles = pawn.possible_positions_move(5, 4)
        self.assertEqual(
            possibles,
            []
        )

    def test_initial_white_block_by_enemy_piece(self):
        board=Board(for_test=True)
        pawn=Pawn('WHITE',board)
        board.set_piece(6,4,pawn)
        board.set_piece(4,4,Pawn('BLACK',board))
        possibles=pawn.possible_positions_move(6,4)
        self.assertEqual(possibles,[(5,4)])

    def test_not_initial_white_block_by_enemy_piece(self):
        board=Board(for_test=True)
        pawn=Pawn('WHITE',board)
        board.set_piece(5,4,pawn)
        board.set_piece(4,4,Pawn('BLACK',board))
        possibles=pawn.possible_positions_move(5,4)
        self.assertEqual(possibles,[])

    # POSSIBLE POSITIONS EAT

    def test_eat_black_right(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 4, pawn)
        board.set_piece(4,5,Pawn('WHITE',board))
        possibles = pawn.possible_positions_eat(3, 4)
        self.assertEqual(
            possibles,
            [(4, 5)]
        )
    
    def test_eat_black_left(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3,4, pawn)
        board.set_piece(4,3,Pawn('WHITE',board))
        possibles = pawn.possible_positions_eat(3, 4)
        self.assertEqual(
            possibles,
            [(4, 3)]
        )

    
    def test_eat_black_left_and_right(self):
        board = Board(for_test = True)
        pawn = Pawn("BLACK", board)
        board.set_piece(3, 4, pawn)
        board.set_piece(4,5,Pawn('WHITE',board))
        board.set_piece(4,3,Pawn('WHITE',board))
        possibles = pawn.possible_positions_eat(3, 4)
        self.assertEqual(
            possibles,
            [(4,5),(4, 3)]
        )

    def test_eat_white_right(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(5, 4, pawn)
        board.set_piece(4,5,Pawn('BLACK',board))
        possibles = pawn.possible_positions_eat(5, 4)
        self.assertEqual(
            possibles,
            [(4,5)]
        )

    def test_eat_white_left(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(5, 4, pawn)
        board.set_piece(4,3,Pawn('BLACK',board))
        possibles = pawn.possible_positions_eat(5, 4)
        self.assertEqual(
            possibles,
            [(4,3)]
        )

    def test_eat_white_left_and_right(self):
        board = Board(for_test = True)
        pawn = Pawn("WHITE", board)
        board.set_piece(5, 4, pawn)
        board.set_piece(4,5,Pawn('BLACK',board))
        board.set_piece(4,3,Pawn('BLACK',board))
        possibles = pawn.possible_positions_eat(5, 4)
        self.assertEqual(
            possibles,
            [(4,5),(4, 3)]
        )

if __name__=='__main__':
    unittest.main()