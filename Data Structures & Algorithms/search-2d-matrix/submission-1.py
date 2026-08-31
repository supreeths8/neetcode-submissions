class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            high = len(row) - 1
            low = 0

            while low <= high:
                mid = (low + high) // 2
                if target < row[mid]:
                    high = mid - 1
                elif row[mid] < target:
                    low = mid + 1
                else:
                    return True
        
        return False

