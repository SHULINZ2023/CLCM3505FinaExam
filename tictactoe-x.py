import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal \
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check diagonal /
        return True
    return False

def is_full(board):
    # Check if the board is full
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def computer_move(board, player):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = player
            break

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        if player == "X":
            computer_move(board, player)
        else:
            computer_move(board, player)

        if check_win(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break
        turn += 1

if __name__ == "__main__":
    play_game()

