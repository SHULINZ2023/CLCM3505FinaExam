import numpy as np
import os
import json
import re
from openai import OpenAI
import random

# Set up your OpenAI API key
clientOpenAI = OpenAI(
        # This is the default and can be omitted
        api_key="",
)
class TicTacToe3D:
    def __init__(self):
        self.board = np.zeros((3, 3, 3), dtype=int)
        self.current_player = 0

    def display_board(self):
        print("Current Board:")
        for i in range(3):
            print("-" * 9)
            for j in range(3):
                print("|", end=" ")
                for k in range(3):
                    if self.board[i][j][k] == 0:
                        print(" ", end=" ")
                    elif self.board[i][j][k] == 1:
                        print("X", end=" ")
                    else:
                        print("O", end=" ")
                print("|")
        print("-" * 9)

    def make_move(self, row, col, depth):
        if self.board[row][col][depth] == 0:
            self.board[row][col][depth] = self.current_player
            #self.current_player = 3 - self.current_player
            return True
        else:
            print("Invalid move! Try again.")
            return False

    def check_winner(self):
        for i in range(3):
            # Check rows
            for j in range(3):
                if self.board[i][j][0] == self.board[i][j][1] == self.board[i][j][2] != 0:
                    return self.board[i][j][0]

            # Check columns
            for k in range(3):
                if self.board[i][0][k] == self.board[i][1][k] == self.board[i][2][k] != 0:
                    return self.board[i][0][k]

            # Check diagonals
            if self.board[i][0][0] == self.board[i][1][1] == self.board[i][2][2] != 0:
                return self.board[i][0][0]
            if self.board[i][0][2] == self.board[i][1][1] == self.board[i][2][0] != 0:
                return self.board[i][0][2]

        # Check depth
        for j in range(3):
            for k in range(3):
                if self.board[0][j][k] == self.board[1][j][k] == self.board[2][j][k] != 0:
                    return self.board[0][j][k]

        return 0  # No winner yet

    def is_board_full(self):
        return np.all(self.board != 0)

    def play_human(self,player):
        self.current_player = player
        while True:
            self.display_board()
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))
            depth = int(input("Enter depth (0-2): "))
            if self.make_move(row, col, depth):
                winner = self.check_winner()
                if winner != 0:
                    self.display_board()
                    print(f"Player {winner} wins!")
                    break
                elif self.is_board_full():
                    self.display_board()
                    print("It's a tie!")
                    break
            break
    def play_openai(self,player):
        #prompt = "it is your turn to move with current Tic-tac-toe board:\n" + "\n".join("|".join(row) for row in board)
        #prompt = prompt + "\n, please response with new board in json"
        #print("prompt:" + prompt)
        self.current_player = player
        print(self.board)
        while True:
            response = clientOpenAI.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful, pattern-following assistant designed to output JSON with \"row\":,\"col\":,\"depth\":. Let's play 3D tic tac toe!"},
                {"role": "user", "content": f"It's your turn to play tic-tac-toe. Here's the current board:\n{self.board}\nWhere do you want to place your {self.current_player}?"},
            ]
            )
            
            print(response)
            #return [2,1,0]
            move = json.loads(response.choices[0].message.content.strip())
            print(move)
            row = move['row'] -1
            if 'column' in move:
                col = move['column'] -1
            if 'col' in move:
                col = move['col'] -1    
            if 'depth' in move:
                depth = move['depth'] -1      
            
            if self.make_move(row, col, depth):
                winner = self.check_winner()
                if winner != 0:
                    self.display_board()
                    print(f"Player {winner} wins!")
                    break
                elif self.is_board_full():
                    self.display_board()
                    print("It's a tie!")
                    break
                break
            else:    
                print("this position has been used, please do again")


def main():
    game = TicTacToe3D()
    players = [1, 2]
    #random.shuffle(players)
    turn = 0
    while True:
        player = players[turn % 2]
        print(player)
        if player == 1:
            game.play_openai(player)
        elif player == 2:
            game.play_human(player)
        else:
            print("Invalid choice. Please enter 'o' or 'h'.")
        turn +=1    

if __name__ == "__main__":
    main()
