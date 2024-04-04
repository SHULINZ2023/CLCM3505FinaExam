import random

def print_board(board):
    for i in range(3):
        print(f"Layer {i + 1}:")
        for row in board[i]:
            print(" | ".join(row))
            print("-" * 9)
        print()

def check_winner(board, player):
    # Check layers
    for i in range(3):
        # Check rows and columns
        for j in range(3):
            if all(cell == player for cell in board[i][j]):
                return True
            if all(board[i][k][j] == player for k in range(3)):
                return True
        # Check diagonals
        if all(board[i][k][k] == player for k in range(3)):
            return True
        if all(board[i][k][2 - k] == player for k in range(3)):
            return True
    
    # Check verticals
    for j in range(3):
        for k in range(3):
            if all(board[i][j][k] == player for i in range(3)):
                return True
    
    # Check diagonals across layers
    if all(board[i][i][i] == player for i in range(3)):
        return True
    if all(board[i][i][2 - i] == player for i in range(3)):
        return True
    if all(board[i][2 - i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i][2 - i] == player for i in range(3)):
        return True

    return False

def get_empty_cells(board):
    return [(i, j, k) for i in range(3) for j in range(3) for k in range(3) if board[i][j][k] == " "]

def play_computer_move(board, player):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)
    return None

def play_3d_tic_tac_toe():
    board = [[[" " for _ in range(3)] for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0
    steps = 0

    print("Welcome to 3D Tic-Tac-Toe!")

    while True:
        current_player = players[current_player_index]
        print_board(board)

        row, col, layer = play_computer_move(board, current_player)

        if (row, col, layer) is not None:
            board[layer][row][col] = current_player
            steps += 1

            if check_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins in {steps} steps!")
                break
            elif all(board[i][j][k] != " " for i in range(3) for j in range(3) for k in range(3)):
                print_board(board)
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    play_3d_tic_tac_toe()
