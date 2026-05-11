class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        numRows = len(matrix)
        numCols = len(matrix[0])
        l = 0
        r = numRows - 1
        #do a search on the rows first
        while l <= r:
            mid = (l + r) //2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break
        if not (l <= r):
            return False

        searchRow = (l + r) // 2
        rowl, rowr, = 0, numCols-1
        while rowl <= rowr:
            midRow = (rowl + rowr) // 2
            if target == matrix[searchRow][midRow]:
                return True
            elif target > matrix[searchRow][midRow]:
                rowl  = midRow + 1
            else:
                rowr  = midRow - 1
        return False

