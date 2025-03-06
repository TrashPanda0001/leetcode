import copy


class Solution(object):
    def __init__(self):
        self.arr = None

    def isSafe(self, arr, n, cur_row, cur_col):
        # Check vertical column
        for row in range(cur_row):
            if arr[row][cur_col] == "Q":
                return False

        # Check horizontal row
        for col in range(cur_col):
            if arr[cur_row][col] == "Q":
                return False

        # Check main diagonal
        row, col = cur_row - 1, cur_col - 1
        while row >= 0 and col >= 0:
            if arr[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # Check anti diagonal
        row, col = cur_row - 1, cur_col + 1
        while row >= 0 and col < n:
            if arr[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True

    def getAllNQueenConfigs(self, arr, n, cur_row, boardConfigs):
        # If we have filled all rows, store the current configuration
        if cur_row == n:
            temp_arr = copy.deepcopy(arr)
            boardConfigs.append(temp_arr)
            return

        # Try placing a Queen in every column of the current row
        for col in range(n):
            if self.isSafe(arr, n, cur_row, col):
                arr[cur_row][col] = "Q"
                self.getAllNQueenConfigs(arr, n, cur_row + 1, boardConfigs)
                arr[cur_row][col] = "."  # Backtrack

    def solveNQueens(self, n):
        self.arr = [["."] * n for _ in range(n)]  # Initialize the board
        boardConfigs = []
        self.getAllNQueenConfigs(self.arr, n, 0, boardConfigs)
        # Convert each board configuration to a list of strings (for a nice display)
        return [[''.join(row) for row in board] for board in boardConfigs]
