from chess import Chess
from exceptions import InvalidMove

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
        if chess.pawn_change_verification(to_row,to_col)==True:
            while True:
                try:
                    new_piece=input('Type the piece you would like to replace the pawn(Queen, Rook, Bishop or Knight): ')
                    chess.pawn_change_action(new_piece,to_row,to_col)
                    break
                except Exception as pawn_change_exception: 
                    print(pawn_change_exception)
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()