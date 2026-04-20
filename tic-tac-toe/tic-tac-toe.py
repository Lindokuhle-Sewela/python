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
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
