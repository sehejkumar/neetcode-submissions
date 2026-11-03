from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque([])
        numFresh = 0
        numMins = 0
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    numFresh+=1

        numMins = 0
        dir = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and numFresh > 0:
            numOranges = len(queue)
            for _ in range(numOranges):
                currRow, currCol = queue.popleft()
                for r,c in dir:
                    newRow = currRow + r
                    newCol = currCol + c
                    if (newRow >= 0 and newRow < len(grid) and newCol >= 0 and newCol < len(grid[0]) and grid[newRow][newCol] == 1):
                        grid[newRow][newCol] = 2
                        queue.append((newRow, newCol))
                        numFresh -=1

                
            numMins +=1

        if numFresh > 0:
            return -1

        return numMins
            


        

