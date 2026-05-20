class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O (m+n)
        # r = 0
        # c = len(matrix[0]) - 1
        # while r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0]):
        #     if matrix[r][c] == target:
        #         return True
        #     elif matrix[r][c] < target:
        #         r+=1
        #     else:
        #         c-=1
        # return False

        #O(log(M*N))
        rows = len(matrix)
        cols = len(matrix[0])
        top = 0
        bottom = rows-1
        while top<=bottom:
            #get to the correct row first
            currRow = (top + bottom) // 2
            if target > matrix[currRow][-1]:
                top = currRow + 1
            elif target < matrix[currRow][0]:
                bottom  = currRow - 1
            else:
                break
        
        if not (top <= bottom):
            #faulty
            return False
        
        corrRow = (top + bottom) // 2
        l = 0
        r = cols-1
        while l <= r:
            mid = (l + ((r-l)//2))
            if target > matrix[corrRow][mid]:
                l = mid + 1
            elif target < matrix[corrRow][mid]:
                r = mid -1
            else:
                return True
        return False
