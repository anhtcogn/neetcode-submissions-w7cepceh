class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        l, h = 0, (row * col) - 1

        while l <= h:
            mid = l + (h - l) // 2
            r = mid // col
            c = mid % col

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = mid - 1
            else:
                l = mid + 1

        return False