class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #sounds like a recursive backtracking problem
        #start at an arbitrary index, make sure it is less than length of target
        numRows = len(board)
        numCols = len(board[0])
        seenCells = set()

        def dfs(currRow, currCol, currIndex):
            if currIndex == len(word):
                return True
            if currRow < 0 or currCol < 0 or currRow >= numRows or currCol >= numCols or word[currIndex] != board[currRow][currCol] or (currRow, currCol) in seenCells:
                return False
            #mark curr cell as seen
            seenCells.add((currRow,currCol))
            res = dfs(currRow +1, currCol, currIndex +1) or dfs(currRow - 1, currCol, currIndex +1) or dfs(currRow , currCol + 1, currIndex +1) or dfs(currRow , currCol-1, currIndex +1)
            #backtrack and mark coordinates as not seen
            seenCells.remove((currRow, currCol))
            return res
        
        for r in range(numRows):
            for c in range(numCols):
                if dfs(r,c,0): return True

        return False    