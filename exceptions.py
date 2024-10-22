class InvalidMove(Exception):
    message = "Invalid piece move"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "Cannot move another player's piece"

class EmptyPosition(InvalidMove):
    message = "This cell is empty"

class InvalidMoveRookMove(InvalidMove):
    message='La torre no se puede mover en esa direccion'

class InvalidMovePawnMove(InvalidMove):
    message='El peon no se puede mover en esa dirección'
    
class OutOfBoard(InvalidMove):
    message = "The indicated position is out of the board"

class RowOutOfBoard(OutOfBoard):
    message='The indicated row is out of the board'

class ColumnOutOfBoard(OutOfBoard):
    message='The indicated column is out of the board'

class InvalidPawnChange(Exception):
    message='Cant change pawn for the given input, please select one of the granted options(Queen, Bishop, Rook or Knight): '