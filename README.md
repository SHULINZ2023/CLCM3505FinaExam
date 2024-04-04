# GenAI Clash in the Tic-tac-toe Challenge

### Objective: Develop a Tic-tac-toe game featuring two GenAI opponents, where each GenAI employs strategic decision-making algorithms to compete against each other. 


This project aims to develop a Tic-tac-toe game that will be played between two artificially intelligent agents, referred to as GenAI. The game will follow the traditional rules of Tic-tac-toe, where players take turns marking spaces on a 3x3 grid with their respective symbols. Each GenAI will be programmed to make strategic decisions based on the current state of the game, with the ultimate objective of achieving three of their symbols in a row, either horizontally, vertically, or diagonally. The development of this game will involve designing and implementing algorithms for player moves, handling game logic, and providing a user-friendly interface for interaction. Additionally, the performance of the GenAI agents will be evaluated based on factors such as win rate, efficiency, and adaptability to different game scenarios. Overall, this project seeks to showcase the capabilities of artificial intelligence in playing classic board games and provide an engaging experience for players.

How-to:
-   71  docker images
-   72  docker login -u danbowvalleycollege
-    73  ocker build -t imagetictactoe:1 .
-   74  docker tag 9c7aec248896 danbowvalleycollege/genai-tictactoe:dev-9c7aec248896
-   75  docker images
-   76  docker push danbowvalleycollege/genai-tictactoe:dev-9c7aec248896
-   77  docker run -it --rm imagetictactoe:1


