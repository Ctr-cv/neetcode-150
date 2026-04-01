class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix) - 1
        while (lrow < rrow):
            row = lrow + (rrow - lrow) // 2
            if matrix[row][-1] < target:
                lrow = row + 1
            elif matrix[row][0] > target:
                rrow = row - 1
            else:
                lrow = row
                break
        l, r = 0, len(matrix[0]) - 1
        while (l < r):
            mid = l + (r - l) // 2
            if matrix[lrow][mid] < target:
                l = mid + 1
            elif matrix[lrow][mid] > target:
                r = mid - 1
            else:
                return True
        return matrix[lrow][l] == target
        
