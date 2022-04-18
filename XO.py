EMPTY_SYMBOL = '_'
CROSS_SYMBOL = 'X'
CIRCLE_SYMBOL = 'O'
DRAW = 'DRAW'


def make_board():
    return [
        '_', '_', '_',
        '_', '_', '_',
        '_', '_', '_'
    ]


def is_free(board, position):
    return board[position] == EMPTY_SYMBOL


def is_winner(board, player):
    return (
            (board[0] == board[1] == board[2] == player) or
            (board[3] == board[4] == board[5] == player) or
            (board[6] == board[7] == board[8] == player) or
            (board[0] == board[3] == board[6] == player) or
            (board[1] == board[4] == board[7] == player) or
            (board[2] == board[5] == board[8] == player) or
            (board[0] == board[4] == board[8] == player) or
            (board[2] == board[4] == board[6] == player)
    )


def is_full(board):
    for field in board:
        if field == EMPTY_SYMBOL:
            return False
    return True


def is_draw(board):
    return (
            is_full(board) and
            not is_winner(board, CROSS_SYMBOL) and
            not is_winner(board, CIRCLE_SYMBOL)
    )


def is_valid_position(position):
    return position >= 1 and 9 >= position


def next_symbol(symbol):
    if symbol == CROSS_SYMBOL:
        return CIRCLE_SYMBOL
    return CROSS_SYMBOL


def get_game_result(board, player):
    if is_winner(board, player):
        return player
    elif is_draw(board):
        return DRAW
    else:
        return None


def print_board(board):
    print(board[0], board[1], board[2], sep=' ')
    print(board[3], board[4], board[5], sep=' ')
    print(board[6], board[7], board[8], sep=' ')


def play_again():
    onemore = input('Czy chcesz zagrać ponownie? Jeśli tak, wybierz "y">>>')
    if onemore == 'y' or onemore == 'Y':
        return True
    return False


def make_move(board, player):
    while True:
        print_board(board)
        position = input('wprowadź numer od 1 do 9>>>')

        if not position.isdigit():
            print("Niewłaściwa wartość")
            continue

        position = int(position)

        if not is_valid_position(position):
            print('Wybierz liczbę z przedziału od 1 do 9')
            continue

        index = position - 1
        if is_free(board, index):
            board[index] = player
            break
        else:
            print('To miejsce jest zajęte. Spróbuj ponownie')
            continue

def print_game_result(result):
    if result == DRAW:
        print('REMIS')
    elif result is not None:
        print('Wygrał', result)


def get_game_result(board, player):
    if is_winner(board, player):
        return player
    elif is_draw(board):
        return DRAW
    else:
        return None


def run_game():
    board = make_board()  
    player = CROSS_SYMBOL
    history = []
    while True:
        make_move(board, player)
        history.append(board.copy())
        result = get_game_result(board, player)
        if result is not None:
            print_game_result(result)
            break
        player = next_symbol(player)
    return history


def print_history(history):
    i = -1
    while i < (len(history) - 1):
        move = input('Możesz teraz oglądnąć historię swojej gry. Naciśnij "d" aby przejść dalej, lub "c" aby cofnąć>>>')
        if move == 'd' or move == 'D':
            i += 1
            print_board(history[i])
            continue
        elif move == 'c' or move == 'C':
            i -= 1
            print_board(history[i])
            continue


def main():
    while True:
        history = run_game()
        print_history(history)
        if not play_again():
            break
    print('Dziękuję za wspólną grę!')


main()
