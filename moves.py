# POSSIBLE VERTICAL DESCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_vd(piece,row,col):
        possibles = []
        for next_row in range(row + 1, 8):
            other_piece = piece.__board__.get_piece(next_row, col)
            if other_piece is not None:
                if other_piece.__color__ != piece.__color__:
                    possibles.append((next_row, col))  
                break  
            else:
                possibles.append((next_row, col))  
        return possibles

# POSSIBLE VERTICAL ASCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_va(piece,row,col):
    possibles=[]
    for next_row in range(row-1,-1,-1):
        other_piece = piece.__board__.get_piece(next_row, col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((next_row, col))  
            break  
        else:possibles.append((next_row,col))
    return possibles

# POSSIBLE HORIZONTAL RIGHT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hr(piece,row,col):
    possibles=[]
    for next_col in range(col + 1, 8):
        other_piece = piece.__board__.get_piece(row,next_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((row,next_col))  
            break  
        else:possibles.append((row,next_col))
    return possibles

# POSSIBLE HORIZONTAL LEFT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hl(piece,row,col):
    possibles=[]
    for next_col in range(col-1,-1,-1):
        other_piece = piece.__board__.get_piece(row,next_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((row,next_col))  
            break  
        else:possibles.append((row,next_col))
    return possibles

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_dar(piece,row,col):
    pass

# POSSIBLE DIAGONAL ASCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_dal(piece,row,col):
    pass

# POSSIBLE DIAGONAL DESCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_ddr(piece,row,col):
    pass

# POSSIBLE DIAGONAL DESCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_ddl(piece,row,col):
    pass

