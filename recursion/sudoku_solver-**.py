import copy


class Solution(object):
    def __init__(self):
        self.final_board = None

    def isValid(self, i, row, col, board):
        # Check if number 'i' can be placed in the current position
        for y in range(0, len(board[0])):
            if board[row][y] == str(i):  # Compare as strings
                return False
        for y in range(0, len(board)):
            if board[y][col] == str(i):  # Compare as strings
                return False
        top_row = row // 3 * 3
        top_column = col // 3 * 3
        for k in range(0, 3):
            for l in range(0, 3):
                if board[top_row + k][top_column + l] == str(i):  # Compare as strings
                    return False
        return True

    def solve(self, board, x, y):
        if x == len(board):
            self.final_board = copy.deepcopy(board)  # Save a deep copy when solved
            return

        if y == len(board[0]) - 1:  # If we reach the end of a row, move to the next row
            new_x = x + 1
            new_y = 0
        else:  # Move to the next column
            new_x = x
            new_y = y + 1

        if board[x][y] != ".":
            self.solve(board, new_x, new_y)  # Skip filled cells
        else:
            for i in range(1, 10):  # Try numbers 1-9
                if self.isValid(i, x, y, board):
                    board[x][y] = str(i)  # Place the number
                    self.solve(board, new_x, new_y)  # Recursively solve the next cell
                    if self.final_board:  # If the board has been solved, stop recursion
                        return
                    board[x][y] = "."  # Backtrack if no valid number works

    def solveSudoku(self, board):
        self.solve(board, 0, 0)  # Start solving from the top-left corner
        return self.final_board  # Return the solved board
