import os
import json
import re
from openai import OpenAI
import random

# Set up your OpenAI API key
clientOpenAI = OpenAI(
        # This is the default and can be omitted
        api_key="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",
)


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
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
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def user_move(board):
    while True:
        try:
            row = int(input("Enter row (1-3): ")) -1
            col = int(input("Enter column (1-3): ")) -1
            
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken, try again.")
        except ValueError:
            print("Invalid input, try again.")

def ai_move(board, player):
    #prompt = "it is your turn to move with current Tic-tac-toe board:\n" + "\n".join("|".join(row) for row in board)
    #prompt = prompt + "\n, please response with new board in json"
    #print("prompt:" + prompt)
    while True:
        response = clientOpenAI.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": "You are a helpful, pattern-following assistant designed to output JSON. Let's play tic tac toe!"},
            {"role": "user", "content": f"It's your turn to play tic-tac-toe. Here's the current board:\n{board}\nWhere do you want to place your {player}?"},
        ]
        )
        
        print(response)
        #return [2,1]
        move = json.loads(response.choices[0].message.content.strip())
        print(move)
        row = move['row'] -1
        if 'column' in move:
            col = move['column'] -1
        if 'col' in move:
            col = move['col'] -1    
        if board[row][col] == " ":
            return [row,col]
        else:    
            print("this position has been used, please do again")

    
    #return int(move[0]), int(move[1])

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)

    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        print(f"Player {player}'s turn")

        if player == "X":
            row, col = user_move(board)
        else:
            row, col = ai_move(board, player)
        board[row][col] = player

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
