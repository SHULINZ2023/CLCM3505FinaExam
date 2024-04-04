import os
import json
import re
from openai import OpenAI
import anthropic


clientClaude = anthropic.Client(api_key="<YOUR CLAUDE3 API TOKEN>")

clientOpenAI = OpenAI(
        # This is the default and can be omitted
        api_key="<YOUR OPENAI API TOKEN>",
)

def _claude3Move(message):
        
    response = clientClaude.messages.create(
        model="claude-2.1",
        max_tokens=1024,
        system="Respond only in json.", 
        messages=[
            {"role": "user", "content": message} 
        ]
    )

    #print(response.content)
    return response.content



def _openAIMove(message):



    chat_completion = clientOpenAI.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="gpt-3.5-turbo",
    )

    # Regular expression pattern to extract the message content
    pattern = r"content='(.*?)'"

    # Extracting the message content using regular expression
    message_match = re.search(pattern, str(chat_completion))

    if message_match:
        message_content = message_match.group(1)
        #print("OpenAI Move:", message_content)
        return message_content
    else:
        print("No message content found in the input string.")


msg = "Hello there! Let's play tic-tac-toe. I go first with X at position 5. Now you go and response in json."
firstMove = _openAIMove(msg)
print("OpenAI: " + firstMove)

secondMove = "My move is this: " + firstMove + " Now your move next and return in json."
secondMove = _claude3Move(secondMove) 
print("Claude3AI: " + str(secondMove[0]))