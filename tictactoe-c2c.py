import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def play_computer_move(board, player):
    empty_cells = get_empty_cells(board)
    if empty_cells:
        return random.choice(empty_cells)
    return None

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player_index = 0

    print("Welcome to Tic-Tac-Toe!")

    while True:
        current_player = players[current_player_index]
        print_board(board)
        print("===============================")
        row, col = play_computer_move(board, current_player)

        if (row, col) is not None:
            board[row][col] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print("===============================")
                print(f"{current_player} wins!")
                break
            elif all(board[i][j] != " " for i in range(3) for j in range(3)):
                print_board(board)
                print("===============================")
                print("It's a tie!")
                break

            current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    play_tic_tac_toe()
