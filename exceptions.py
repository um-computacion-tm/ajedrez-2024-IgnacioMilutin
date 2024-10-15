class InvalidMove(Exception):
    message = "Movimieto de pieza invalido"
    def __str__(self):
        return self.message

class InvalidTurn(InvalidMove):
    message = "No puedes mover pieza de otro jugador"

class EmptyPosition(InvalidMove):
    message = "La posicion esta vacia"

class InvalidMoveRookMove(InvalidMove):
    message='La torre no se puede mover en esa direccion'

class InvalidMovePawnMove(InvalidMove):
    message='El peon no se puede mover en esa dirección'
    
class OutOfBoard(InvalidMove):
    message = "La posicion indicada se encuentra fuera del tablero"

class RowOutOfBoard(OutOfBoard):
    message='La Fila indicada se encuentra fuera del tablero'

class ColumnOutOfBoard(OutOfBoard):
    message='La Columna indicada se encuentra fuera del tablero'

class InvalidPawnChange(Exception):
    message='Cant change pawn for the given input, please select one of the granted options(Queen, Bishop, Rook or Knight): '