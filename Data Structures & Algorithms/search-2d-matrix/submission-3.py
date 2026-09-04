class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1

        while top <= bottom:
            row = (top + bottom) // 2

            if target < matrix[row][0]:
                bottom = row - 1
            elif matrix[row][-1] < target:
                top = row + 1
            else:
                break
        
        # if top > bottom:
        #     return False

        l,h = 0, cols - 1

        row = (top + bottom) // 2
        while l <= h:
            mid = (l + h) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif target < matrix[row][mid]:
                h = mid - 1
            else:
                return True

        return False
                

