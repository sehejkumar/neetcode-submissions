class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1 is land and 0 is water
        # an island is a group of connected 1s

        possibleDirections = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        numRows = len(grid)
        numCols = len(grid[0])
        numIslands = 0

        # DFS to sink the island
        def dfs(row, col):
            if (
                row < 0
                or row >= numRows
                or col < 0
                or col >= numCols
                or grid[row][col] == '0'
            ):
                return

            # mark current cell as water
            grid[row][col] = '0'

            for dx, dy in possibleDirections:
                dfs(row + dx, col + dy)

        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    numIslands += 1

        return numIslands
