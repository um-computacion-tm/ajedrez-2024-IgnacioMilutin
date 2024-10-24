# GIVES ALL POSSIBLE POSTIONS TO CREATE VALID_POSITIONS FOR PIECES WHICH HAS INDIVIDUALS MOVES

def get_possible_positions(from_row, from_col, movement_functions):
    possible_positions = []
    for move_func in movement_functions:
        possible_positions += move_func(from_row, from_col)
    return possible_positions

# GETS THE VALID POSTIONS OF THE GIVEN PIECE TO USE IN ALL MOVES

def get_piece_valid_positions(board, row, col, color):
    piece = board.get_piece(row, col)
    if not is_valid_piece(piece, color):
        return [] 
    if type(piece).__name__ == 'King':
        return piece.valid_positions(row, col, for_all_moves=True)
    return piece.valid_positions(row, col)

# VERIFIES IF THE PIECE IS A VALID PIECE TO USE (ISNT NONE OR THE OTHER COLOR)

def is_valid_piece(piece, color):
    return piece is not None and piece.get_color() == color

# LIST OF ALL POSSIBLE MOVES FOR ALL PIECES OF A COLOR

def all_moves(board, color):
    all_moves = []
    for row in range(8):
        for col in range(8):
            all_moves += get_piece_valid_positions(board, row, col, color)
    return all_moves

# CHECKS THE SITUATION OF THE NEW POSITION

def check_new_position(piece, new_position, other_piece, possibles):
    if other_piece:
        if other_piece.__color__ != piece.__color__:
            possibles.append(new_position)
        return False
    possibles.append(new_position)
    return True

# GET TO START AND STEP FOR RANGE OF EACH VERTICAL AND HORIZONTAL MOVEMENT

def start_and_step_vertical_and_horizontal(direction, row, col):
    directions = {'va': (row-1, -1, -1),'hl': (col-1, -1, -1),'vd': (row+1, 8, 1),'hr': (col+1, 8, 1)}
    return directions[direction]

def get_new_position(direction, piece, position, next_row_or_col):
    row, col = position
    if direction in ['va','vd']:
        return (next_row_or_col, col), piece.__board__.get_piece(next_row_or_col, col)
    else:
        return (row, next_row_or_col), piece.__board__.get_piece(row, next_row_or_col)

# POSIBLE POSITIONS VERTICAL ASCENDANT, HORIZONTAL LEFT, VERTICAL DESCENDANT AND HORIZONTAL RIGHT POSTIONS TO MOVE A PIECE TO

def possible_positions_vertical_and_horizontal(piece, row, col, direction):
    possibles=[]
    start,end,step = start_and_step_vertical_and_horizontal(direction, row, col)
    position=(row, col)
    for next_row_or_col in range(start, end, step):
        new_position,other_piece = get_new_position(direction, piece, position, next_row_or_col)
        if not check_new_position(piece, new_position, other_piece, possibles):
            break
    return possibles

# POSSIBLE VERTICAL DESCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_vd(piece,row,col):
    return possible_positions_vertical_and_horizontal(piece,row,col,'vd')

# POSSIBLE VERTICAL ASCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_va(piece,row,col):
    return possible_positions_vertical_and_horizontal(piece,row,col,'va')

# POSSIBLE HORIZONTAL RIGHT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hr(piece,row,col):
    return possible_positions_vertical_and_horizontal(piece,row,col,'hr')

# POSSIBLE HORIZONTAL LEFT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hl(piece,row,col):
    return possible_positions_vertical_and_horizontal(piece,row,col,'hl')

# GET TO START, END AND STEP FOR RANGE OF EACH DIAGONAL MOVEMENT

def start_end_step_diagonal(direction, row, col):
    directions = {'dar': (row-1, -1, -1, 1),'ddr': (row+1, 8, 1, 1),'dal': (row-1, -1, -1, -1),'ddl': (row+1, 8, 1, -1)}
    return directions[direction]

# CHECKS STATE OF THE NEW POSITIONS

def process_position(piece, next_row, next_col, possibles):
    if next_col < 0 or next_col > 7:
        return False
    new_position = (next_row, next_col)
    other_piece = piece.__board__.get_piece(next_row, next_col)
    return check_new_position(piece, new_position, other_piece, possibles)

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT, DIAGONAL DESCENDANT TO THE RIGHT,DIAGONAL ASCENDANT TO THE LEFT AND DIAGONAL DESCENDANT TO THE LEFT TO A PIECE TO

def possible_positions_diagonal(piece, row, col, direction):
    possibles = []
    start, end, step, col_step = start_end_step_diagonal(direction, row, col)
    next_col = col + col_step
    for next_row in range(start, end, step):
        if not process_position(piece, next_row, next_col, possibles):
            break
        next_col += col_step
    return possibles

# VALID POSITIONS FOR ROOK AND BISHOP

def valid_positions_rook_and_bishop(piece,from_row,from_col):
    possible_positions=[]
    piece_moves={'Rook':[possible_positions_vd,possible_positions_va,possible_positions_hr,possible_positions_hl],
                 'Bishop':[possible_positions_dar,possible_positions_dal,possible_positions_ddr,possible_positions_ddl]}
    moves=piece_moves.get(type(piece).__name__)
    for move in moves:
        possible_positions+=move(piece,from_row,from_col)
    return possible_positions

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_dar(piece,row,col):
    return possible_positions_diagonal(piece,row,col,'dar')

# POSSIBLE DIAGONAL DESCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_ddr(piece,row,col):
    return possible_positions_diagonal(piece,row,col,'ddr')

# POSSIBLE DIAGONAL ASCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_dal(piece,row,col):
    return possible_positions_diagonal(piece,row,col,'dal')

# POSSIBLE DIAGONAL DESCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_ddl(piece,row,col):
    return possible_positions_diagonal(piece,row,col,'ddl')