# LIST OF ALL POSSIBLE MOVES FOR ALL PIECES OF A COLOR

def all_moves(board,color):
    all_moves=[]
    for row in range(8):
        for col in range(8):
            piece=board.get_piece(row,col)
            if piece is None or piece.get_color() != color:
                continue
            if type(piece).__name__=='King':
                all_moves+=piece.valid_positions(row,col,for_all_moves=type(piece).__name__=='King')
            else: all_moves+=piece.valid_positions(row,col)
    return all_moves

# POISBLE POSITIONS VERTICAL ASCENDANT, HORIZONTAL LEFT, VERTICAL DESCENDANT AND HORIZONTAL RIGHT POSTIONS TO MOVE A PIECE TO

def possible_positions_vertical_and_horizontal(piece, row, col, direction):
    possibles = []
    directions = {'va': (row - 1, -1, -1),'hl': (col - 1, -1, -1),'vd': (row + 1, 8, 1),'hr': (col + 1, 8, 1)}
    start, end, step = directions[direction]
    for next_row_or_col in range(start, end, step):
        new_position = (next_row_or_col, col) if direction in ('va', 'vd') else (row, next_row_or_col)
        other_piece = piece.__board__.get_piece(*new_position)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append(new_position)
            break
        possibles.append(new_position)
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

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT, DIAGONAL DESCENDANT TO THE RIGHT,DIAGONAL ASCENDANT TO THE LEFT AND DIAGONAL DESCENDANT TO THE LEFT TO A PIECE TO

def possible_positions_diagonal(piece,row,col,direction):
    possibles=[]
    directions={'dar':(row-1,-1,-1,1),'ddr':(row+1,8,1,1),'dal':(row-1,-1,-1,-1),'ddl':(row+1,8,1,-1)}
    start,end,step,col_step=directions[direction]
    next_col=col+col_step
    for next_row in range(start,end,step):
        if next_col>7 or next_col<0:
            break
        other_piece = piece.__board__.get_piece(next_row,next_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((next_row,next_col))  
            break
        else:possibles.append((next_row,next_col))
        next_col+=col_step
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