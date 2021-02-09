import colorama
from colorama import Fore, Style

# The GLOBAL VARIABLES
BOARD = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
PLAYER = 'X'
WINNER = None
GAME_STILL_GOING = True

# Initialize the colorama module
colorama.init(autoreset=True)


def display_board() -> None:
    print(f"{BOARD[0]} | {BOARD[1]} | {BOARD[2]}")
    print(f"{BOARD[3]} | {BOARD[4]} | {BOARD[5]}")
    print(f"{BOARD[6]} | {BOARD[7]} | {BOARD[8]}")


def handle_turn() -> None:
    position = None
    valid = False
    while not valid:
        try:
            position = int(input("Choose a position between 1 to 9: ")) - 1
            if BOARD[position] == '-':
                valid = True
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Invalid Choice")
                continue
        except Exception:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid Choice")
            continue

    BOARD[position] = PLAYER
    display_board()


def play_game() -> None:
    """
    Play the game once
    """
    # Display the initial BOARD
    display_board()
    # While the game is still going
    while GAME_STILL_GOING:
        print(f"{PLAYER}\'s Turn")
        handle_turn()
        check_game_over()
        flip_player()
    # Game Over
    if WINNER == 'X':
        print(f"{Fore.GREEN}{Style.BRIGHT}X Won")
    elif WINNER == 'O':
        print(f"{Fore.GREEN}{Style.BRIGHT}O Won")
    else:
        print(f"{Fore.GREEN}{Style.BRIGHT}Tie")


def check_game_over() -> None:
    """
    Check if the game is over or not
    """
    check_win()
    check_tie()


def check_win() -> bool:
    global WINNER, GAME_STILL_GOING
    """
    Check if Someone has won or not
    """
    # Check For Rows
    rows = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    for row in rows:
        if BOARD[row[0]] == BOARD[row[1]] == BOARD[row[2]] != '-':
            WINNER = PLAYER
            GAME_STILL_GOING = False
            return True
    # Check For Columns
    columns = [
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8]
    ]
    for column in columns:
        if BOARD[column[0]] == BOARD[column[1]] == BOARD[column[2]] != '-':
            WINNER = PLAYER
            GAME_STILL_GOING = False
            return True
    # Check For Cross
    cross = [
        [0, 4, 8],
        [2, 4, 6]
    ]
    for cross in cross:
        if BOARD[cross[0]] == BOARD[cross[1]] == BOARD[cross[2]] != '-':
            WINNER = PLAYER
            GAME_STILL_GOING = False
            return True
    else:
        return False


def check_tie() -> None:
    global GAME_STILL_GOING
    if not check_win() and '-' not in BOARD:
        GAME_STILL_GOING = False


def flip_player() -> None:
    global PLAYER
    PLAYER = 'X' if PLAYER == 'O' else 'O'


play_game()
