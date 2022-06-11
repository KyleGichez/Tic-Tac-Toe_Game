"""
Before building a tic tac toe game, we need to know the features that we should include;
1. Print the tic tac toe game board
2. Get player's input
3. Check for winner 
4. Check for tie
4. Switch players
5. Check winner 
6. Check tie
7. Player can win either horizontally, vertically or diagonally.
"""
import random

board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

player_one = "X"
winner = None
game_running = True

"""Print the game board"""
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 10)
    print(board[6] + " | " + board[7] + " | " + board[8])
print_board(board)

def player_input(board):
    """Choose player one spot"""
    player_one_input = int(input("Please enter a number between 1 and 9: "))
    if player_one_input >= 1 and player_one_input <= 9 and board[player_one_input - 1] == "-":
        board[player_one_input - 1] = player_one
    else:
        print("Oops!! the current spot is already taken.")

"""Check if player wins horizontally"""
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    else: return False

"""Check if player wins vertically"""
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    else: return False

"""Check if player wins diagonally"""
def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    else: return False

""""Check for tie game"""
def check_tie(board):
    global game_running
    if "-" not in board:
        print_board(board)
        print("Hey, The game is a tie!")
        game_running = False

"""Check for the winner"""
def check_win():
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print(f"Hey, The winner is {winner}!")
    else:
        pass

"""Switch player"""
def switch_player():
    global player_one
    if player_one == "X":
        player_one = "O"
    else:
        player_one = "X" 

"""Computer player"""
def computer_play(board):
    while player_one == "O":
        player_position = random.randint(0, 8)

        if board[player_position] == "-":
            board[player_position] = "O"
            switch_player()
        else:
            pass

while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch_player()
    computer_play(board)
    check_win()
    check_tie(board)