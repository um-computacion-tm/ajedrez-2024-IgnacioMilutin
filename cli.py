from chess import Chess

class InvalidMove(Exception):
    pass

def main():
    chess=Chess()
    while chess.is_playing():
        play(chess)

def play(chess):
    try:
        print(chess.show_board())
        print("turn: ",chess.turn)
        from_row=int(input('From row: ')),
        from_col=int(input('From col: ')),
        to_row=int(input('To row: ')),
        to_col=int(input('to col: '))

        chess.move(from_row,
                from_col,
                to_row,
                to_col)
        
    except InvalidMove as E:
        print('Su movimiento es invalido')

    except Exception as e:
        print('Error',e)


if __name__=='__main__':
    main()