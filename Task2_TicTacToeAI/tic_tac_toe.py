import math

# Initialize the board
board = [" " for _ in range(9)]


def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()


def print_positions():
    print("Board Positions:")
    print(" 1 | 2 | 3")
    print("---+---+---")
    print(" 4 | 5 | 6")
    print("---+---+---")
    print(" 7 | 8 | 9")
    print()


def check_winner(player):
    win_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False


def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Choose a number between 1 and 9.")
            elif board[move - 1] != " ":
                print("That position is already taken.")
            else:
                board[move - 1] = "X"
                break

        except ValueError:
            print("Please enter a valid number.")


print("=" * 35)
print("      TIC-TAC-TOE AI")
print("=" * 35)

print_positions()

while True:

    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 Congratulations! You Win!")
        break

    if board_full():
        print_board()
        print("🤝 It's a Draw!")
        break

    print("\nAI is thinking...\n")

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if board_full():
        print_board()
        print("🤝 It's a Draw!")
        break
