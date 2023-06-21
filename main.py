game_board = [[" ", " ", " "],
              [" ", " ", " "],
              [" ", " ", " "]]


# make gameboard structure
def print_board(board):
    for i in range(len(board)):
        print(" " + " | ".join(board[i]) + " ")
        if i != len(board) - 1:
            print("-" * 11)


# check if a winner has been acheived
def check_winner(player):
    for row in game_board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [game_board[row][col] for row in range(3)].count(player) == 3:
            return True

    if game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
        return True
    if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
        return True
    return False


current_player = "X"

# Game function
while True:
    print_board(game_board)
    row = int(input("Enter a row (0-2): "))
    col = int(input("Enter a column (0-2): "))

    if row < 0 or row > 2 or col < 0 or col > 2:
        print("invalid move. Try again.")
        continue
    game_board[row][col] = current_player

    if check_winner(current_player):
        print_board(game_board)
        print("Player", current_player, "Wins!")
        break

    if all(game_board[row][col] != " " for row in range(3) for col in range(3)):
        print_board(game_board)
        print("its a draw")
        break

    current_player = "O" if current_player == "X" else "X"
