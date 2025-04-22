def initialize_board(num_rows, num_cols):
    return [['-' for _ in range(num_cols)] for _ in range(num_rows)]

def print_board(board):
    for row in reversed(board):
        print(' '.join(row))

def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':
            board[row][col] = chip_type
            return row
    return -1

def check_if_winner(board, col, row, chip_type):
    # Check horizontal
    count = 0
    for c in range(len(board[0])):
        if board[row][c] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    # Check vertical
    count = 0
    for r in range(len(board)):
        if board[r][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

def play_game():
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    board = initialize_board(num_rows, num_cols)
    print_board(board)
    print("\nPlayer 1: x")
    print("Player 2: o")
    player_turn = 1
    moves = 0

    while True:
        current_player = "Player 1" if player_turn == 1 else "Player 2"
        current_chip = 'x' if player_turn == 1 else 'o'
        col = int(input(f"{current_player}: Which column would you like to choose? "))
        row = insert_chip(board, col, current_chip)
        moves += 1
        print_board(board)

        if check_if_winner(board, col, row, current_chip):
            print(f"{current_player} won the game!")
            break

        if moves == num_rows * num_cols:
            print("Draw. Nobody wins.")
            break

        player_turn = 2 if player_turn == 1 else 1

if __name__ == "__main__":
    play_game()
