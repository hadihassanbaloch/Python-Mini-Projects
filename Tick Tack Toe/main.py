def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter the row (0, 1, 2): "))
        col = int(input(f"Player {players[current_player]}, enter the column (0, 1, 2): "))

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            if is_full(board):
                print_board(board)
                print("The game is a tie!")
                break
            current_player = 1 - current_player
        else:
            print("Cell is already taken, try again.")

if __name__ == "__main__":
    main()