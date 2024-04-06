import os
import json
import re
from openai import OpenAI
import random
import requests
import google.generativeai as genai

# Set up your OpenAI API key
clientOpenAI = OpenAI(
        # This is the default and can be omitted
        api_key="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",
)
genai.configure(api_key="AIzaSyCFRg-6LRLgd2GkOwFm_mBJNXZ_B9lSJ4A")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

def send_request(prompt):
    """
    Sends a request to the Bard API with the provided prompt.

    Args:
        prompt: The text prompt to send to the API.

    Returns:
        A dictionary containing the API response, or None on error.
    """

    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

    convo = model.start_chat(history=[])
    convo.send_message(prompt)
    return convo.last.text




def bardai_move(board,player):
    """
    Gets a move suggestion from Bard for the current board state.

    Args:
        board: A list representing the current Tic-Tac-Toe board.

    Returns:
        An integer representing the suggested move (1-9), or None on error.
    """
    prompt = f"Current Tic-Tac-Toe board is: \n{board}\n. It's Bard's turn {player}. What's the best move? please response with json format\"row\":,\"col\": "
    while True:
        response = send_request(prompt)
        newres = response.replace('```','',10).replace('json','',10)
        move = json.loads(newres)
        row = move['row']
        if 'column' in move:
            col = move['column']
        if 'col' in move:
            col = move['col']   
        if board[row][col] == " ":
            return [row,col]
        else:    
            print("this position has been used, please do again")
        
def openai_move(board, player):
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
        
        #print(response)
        #return [2,1]
        move = json.loads(response.choices[0].message.content.strip())
        #print(move)
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



def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    random.shuffle(players)

    turn = 0
    while True:
        print_board(board)
        player = players[turn % 2]
        

        if player == "X":
            print(f"Player BardAI's turn")
            row, col = bardai_move(board,player)
        else:
            print(f"Player OpenAI's turn")
            row, col = openai_move(board, player)
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
