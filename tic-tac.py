import os


winning_patters = ["012", "345", "678", "036", "147", "258", "048", "246"]


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def check_if_victory(board: list[str], last_symbol: str) -> bool:
    for pattern in winning_patters:
        matches: int = 0
        for idx in pattern:
            matches += board[int(idx)] == last_symbol
        if matches == 3:
            return True


def game():
    board_game = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    current_board = f"""
        0 | 1 | 2   {board_game[0]} | {board_game[1]} | {board_game[2]}
        ---------
        3 | 4 | 5   {board_game[3]} | {board_game[4]} | {board_game[5]}
        ---------
        6 | 7 | 8   {board_game[6]} | {board_game[7]} | {board_game[8]}
        """

    # Set up turn game to let know the user who goes now
    turn_number = 0

    print("Welcome to the Tic Tac Toe game!")

    # Condition to keep the game running
    while turn_number < 8:
        if turn_number % 2 == 0:
            turn_symbol = "X"
        else:
            turn_symbol = "O"

        print(current_board)
        position = int(input(f"Turn for {turn_symbol} Chose a position: "))
        board_game[position] = turn_symbol

        if check_if_victory(board_game, turn_symbol):
            print(f"Victory the {turn_symbol} player has won")
            break

        # Update the current board after each play
        current_board = f"""
        0 | 1 | 2   {board_game[0]} | {board_game[1]} | {board_game[2]}
        ---------
        3 | 4 | 5   {board_game[3]} | {board_game[4]} | {board_game[5]}
        ---------
        6 | 7 | 8   {board_game[6]} | {board_game[7]} | {board_game[8]}
            """

        turn_number += 1

        # Clearing the Screen
        cls()

    print("Draw")
    print("")


want_play = True
while want_play:
    game()
    value = input("Want to play again [y/n]: ")
    if value == "n":
        want_play = False
    print()
