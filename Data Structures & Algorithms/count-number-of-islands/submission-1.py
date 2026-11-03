class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def recurse(row: int, col: int):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != "1":
                return
            
            grid[row][col] = "0"

            newIndicies = [[1,0], [-1,0], [0,1], [0,-1]]
            for newR, newC in newIndicies:
                recurse(row+newR, col+newC)

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    res+=1
                    recurse(r,c)

        return res
