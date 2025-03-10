class Solution(object):

    def __init__(self):
        self.moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def getMaxGold(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        max_gold = 0
        temp_value = grid[row][col]
        grid[row][col] = 0
        for move in self.moves:
            x_move = move[0]
            y_move = move[1]
            max_gold = max(max_gold, temp_value + self.getMaxGold(grid, row + x_move, col + y_move))
        grid[row][col] = temp_value
        return max_gold

    def getMaximumGold(self, grid):
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, self.getMaxGold(grid, i, j))
        return max_gold
