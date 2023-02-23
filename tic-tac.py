import os


winning_patters = ["012", "345", "678", "036", "147", "258", "048", "246"]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


board_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
current_board = f"""
            0 | 1 | 2   {board_game[0]} | {board_game[1]} | {board_game[2]}
            ---------
            3 | 4 | 5   {board_game[3]} | {board_game[4]} | {board_game[5]}
            ---------
            6 | 7 | 8   {board_game[6]} | {board_game[7]} | {board_game[8]}
            """


def print_board(board_game):
    current_board = f"""
            0 | 1 | 2   {board_game[0]} | {board_game[1]} | {board_game[2]}
            ---------
            3 | 4 | 5   {board_game[3]} | {board_game[4]} | {board_game[5]}
            ---------
            6 | 7 | 8   {board_game[6]} | {board_game[7]} | {board_game[8]}
            """
    print(current_board)


def check_if_victory(board: list[str], last_symbol: str) -> bool:
    for pattern in winning_patters:
        matches: int = 0
        for idx in pattern:
            matches += board[int(idx)] == last_symbol
        if matches == 3:
            return True


def game():
    board_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

    # Set up turn game to let know the user who goes now
    turn_number = 0

    print("\nWelcome to the Tic Tac Toe game!!!")

    # Condition to keep the game running
    while turn_number < 8:
        if turn_number % 2 == 0:
            turn_symbol = "X"
        else:
            turn_symbol = "O"

        print_board(board_game)

        position: int = int(input(f"Turn for {turn_symbol} Chose a position: "))
        #Check if position is in range
        while position < 0 or position > 8:
            print("Sorry you can't play that position.")
            position: int = int(input(f"Turn for {turn_symbol} Try again:"))
            continue

        # Check if position it's available
        if board_game[position] != "_":
            print("Sorry that position it's already taken.")
            position: int = int(input(f"Turn for {turn_symbol} Try again: "))
            continue

        board_game[position] = turn_symbol

        if check_if_victory(board_game, turn_symbol):
            print(f"Victory! The {turn_symbol} player has won")
            break

        # Update the current board after each play
        print_board(board_game)

        turn_number += 1

        # Clearing the Screen
        cls()

    print("It's a draw you can try again.")
    print("")


want_play = True
while want_play:
    game()
    value = input("Want to play again [y/n]: ")
    while value != "y" or value != "n":
        value = input("Want to play again [y/n]: ")

    if value == "n":
        want_play = False
    print()
