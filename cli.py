from chess import Chess
from exceptions import InvalidMove, InvalidPawnChange

def main():
    chess=Chess()
    while chess.is_playing():
        play(chess)

# USER INTERFACE FOR PLAYING THE GAME

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ",chess.turn())
        from_row=int(input('From row: '))
        from_col=int(input('From col: '))
        to_row=int(input('To row: '))
        to_col=int(input('To col: '))
        chess.move(from_row,from_col,to_row,to_col)
        chess.rules(to_row,to_col)
        
    except Exception as e:
        print(e)

#def ask_for_piece_to_change_pawn_to(self):
#    return input('Type the piece you would like to replace the pawn(Queen, Rook, Bishop or Knight): ')
 

if __name__=='__main__':
    main()