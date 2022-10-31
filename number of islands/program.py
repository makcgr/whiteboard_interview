class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        numRows, numCols = len(grid), len(grid[0])
        count = 0
        for i in range(numRows):
            for j in range(numCols):
                if(grid[i][j]==1):
                    self.dfs(grid, i, j)
                    count += 1
        return count
        # Fill this in.

    def inRange(self, grid, r, c):
        numRows, numCols = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRows or c >= numCols:
            return False
        return True

    def dfs(self, grid, r, c):
        # mark as visited
        grid[r][c] = 2
        directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for dir in directions:
            nr, nc = r + dir[0], c + dir[1]
            if self.inRange(grid, nr, nc) and grid[nr][nc] == 1:
                self.dfs(grid, nr, nc)


grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]

res = Solution().numIslands(grid)
assert res == 3
print(res)