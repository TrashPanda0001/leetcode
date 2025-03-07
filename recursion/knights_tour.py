import copy

# Define the possible knight moves
moves = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-1, -2), (-2, 1), (-2, -1), (-1, -2)]
boardConfigs = []


# Recursive function to find all knight's paths
def getKnightPaths(board, boardSize, row, column, cur_move):
    # If the position is out of bounds or already visited, return
    if row < 0 or column < 0 or row >= boardSize or column >= boardSize or board[row][column] != 0:
        return

    # If we've filled all positions, store the configuration
    if cur_move == boardSize * boardSize :
        board[row][column] = cur_move
        print(board)  # Store the current valid configuration
        board[row][column] = 0  # Backtrack (reset the position)
        return

    # Mark the current position with the current move number
    board[row][column] = cur_move

    # Explore all possible knight moves
    for move in moves:
        x_move = move[0]
        y_move = move[1]
        getKnightPaths(board, boardSize, row + x_move, column + y_move, cur_move + 1)

    # Backtrack: Reset the current position to 0 after recursion
    board[row][column] = 0


# Input for the board size and starting position
boardSize = int(input("Enter board size: "))
start_row = int(input("Enter start row: "))
start_column = int(input("Enter start column: "))

# Initialize the board with 0s
board = [[0] * boardSize for _ in range(boardSize)]

# Call the function to find all knight paths
getKnightPaths(board, boardSize, start_row, start_column, 1)


