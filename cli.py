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
        chess.draw(from_row,from_col,to_row,to_col)
        chess.move(from_row,from_col,to_row,to_col)
        chess.rules(to_row,to_col)
        
    except Exception as e:
        print(e)

if __name__=='__main__':
    main()