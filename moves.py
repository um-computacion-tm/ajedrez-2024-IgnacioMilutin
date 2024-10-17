# LIST OF ALL POSSIBLE MOVES FOR ALL PIECES OF A COLOR

def all_moves(board,color):
        all_moves=[]
        for row in range(8):
            for col in range(8):
                piece=board.get_piece(row,col)
                if piece is None:
                    continue
                if piece.get_color()==color:
                    if type(piece).__name__=='King':
                        all_moves+=piece.valid_positions(row,col,for_all_moves=True)
                    else: all_moves+=piece.valid_positions(row,col)
                else: continue
        return all_moves

# POISBLE POSITIONS VERTICAL ASCENDANT, HORIZONTAL LEFT, VERTICAL DESCENDANT AND HORIZONTAL RIGHT POSTIONS TO MOVE A PIECE TO

def possible_positions_va_vd_hr_hl(piece,row,col,direction):
    possibles=[]
    if direction=='va':
        start,end,step=row-1,-1,-1
    if direction=='hl':
        start,end,step=col-1,-1,-1
    if direction=='vd':
        start,end,step=row+1,8,1
    if direction=='hr':
        start,end,step=col+1,8,1
    for next_row_or_col in range(start,end,step):
        if direction=='va' or direction=='vd':
            other_piece = piece.__board__.get_piece(next_row_or_col, col)
            new_position=(next_row_or_col,col)
        else: 
            other_piece = piece.__board__.get_piece(row,next_row_or_col)
            new_position=(row,next_row_or_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append(new_position)
            break
        possibles.append(new_position)
    return possibles

# POSSIBLE VERTICAL ASCENDANT AND HORIZONTAL LEFT POSITIONS TO MOVE A PIECE TO

#def possible_positions_va_and_hl(piece,row,col,va):
    possibles=[]
    if va:
        start=row-1
    else: start=col-1
    for next_row_or_col in range(start,-1,-1):
        if va:
            other_piece = piece.__board__.get_piece(next_row_or_col, col)
            new_position=(next_row_or_col,col)
        else: 
            other_piece = piece.__board__.get_piece(row,next_row_or_col)
            new_position=(row,next_row_or_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append(new_position)
            break
        possibles.append(new_position)
    return possibles

# POSSIBLE VERTICAL DESCENDANT AND HORIZONTAL RIGHT POSITIONS TO MOVE A PIECE TO

#def possible_positions_vd_and_hr(piece,row,col,vd):
    possibles=[]
    if vd:
        start=row+1
    else: start=col+1
    for next_row_or_col in range(start,8):
        if vd:
            other_piece = piece.__board__.get_piece(next_row_or_col, col)
            new_position=(next_row_or_col,col)
        else: 
            other_piece = piece.__board__.get_piece(row,next_row_or_col)
            new_position=(row,next_row_or_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append(new_position)
            break
        possibles.append(new_position)
    return possibles


# POSSIBLE VERTICAL DESCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_vd(piece,row,col):
    return possible_positions_va_vd_hr_hl(piece,row,col,'vd')

# POSSIBLE VERTICAL ASCENDANT POSITIONS TO MOVE A PIECE TO:

def possible_positions_va(piece,row,col):
    return possible_positions_va_vd_hr_hl(piece,row,col,'va')

# POSSIBLE HORIZONTAL RIGHT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hr(piece,row,col):
    return possible_positions_va_vd_hr_hl(piece,row,col,'hr')

# POSSIBLE HORIZONTAL LEFT POSITIONS TO MOVE A PIECE TO:

def possible_positions_hl(piece,row,col):
    return possible_positions_va_vd_hr_hl(piece,row,col,'hl')

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT AND DIAGONAL DESCENDANT TO THE RIGHT TO A PIECE TO

def possible_positions_dar_and_ddr(piece,row,col,dar):
    possibles=[]
    next_col=col+1
    if dar:
        start,end,step=row-1,-1,-1
    else: 
        start,end,step,=row+1,8,1
    for next_row in range(start,end,step):
        if next_col==8:
            break
        other_piece = piece.__board__.get_piece(next_row,next_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((next_row,next_col))  
            break  
        else:possibles.append((next_row,next_col))
        next_col+=1
    return possibles

# POSSIBLE DIAGONAL ASCENDANT TO THE LEFT AND DIAGONAL DESCENDANT TO THE LEFT POSITIONS TO A PIECE TO

def possible_positions_dal_and_ddl(piece,row,col,dal):
    possibles=[]
    next_col=col-1
    if dal:
        start,end,step=row-1,-1,-1
    else: 
        start,end,step,=row+1,8,1
    for next_row in range(start,end,step):
        if next_col==-1:
            break
        other_piece = piece.__board__.get_piece(next_row,next_col)
        if other_piece is not None:
            if other_piece.__color__ != piece.__color__:
                possibles.append((next_row,next_col))  
            break  
        else:possibles.append((next_row,next_col))
        next_col-=1
    return possibles

# POSSIBLE DIAGONAL ASCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_dar(piece,row,col):
    return possible_positions_dar_and_ddr(piece,row,col,dar=True)

# POSSIBLE DIAGONAL DESCENDANT TO THE RIGHT POSITIONS TO A PIECE TO:

def possible_positions_ddr(piece,row,col):
    return possible_positions_dar_and_ddr(piece,row,col,dar=False)

# POSSIBLE DIAGONAL ASCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_dal(piece,row,col):
    return possible_positions_dal_and_ddl(piece,row,col,dal=True)

# POSSIBLE DIAGONAL DESCENDANT TO THE LEFT POSITIONS TO A PIECE TO:

def possible_positions_ddl(piece,row,col):
    return possible_positions_dal_and_ddl(piece,row,col,dal=False)