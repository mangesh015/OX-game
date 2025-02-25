def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    # Initialize the board with numbers 1-9
    board = [[str(3 * i + j + 1) for j in range(3)] for i in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn")
        move = int(input("Enter the number of the cell (1-9): "))

        if move < 1 or move > 9:
            print("Invalid move, try again.")
            continue

        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] in players:
            print("Cell already taken, try again.")
            continue

        board[row][col] = players[current_player]
        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break

        if check_draw(board):
            print("The game is a draw!")
            break

        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()
