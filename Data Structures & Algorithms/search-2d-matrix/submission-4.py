class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                break

        if not (l <= r):
            return False

        m = (l + r) // 2
        l2 = 0
        r2 = len(matrix[0]) - 1
        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if target > matrix[m][m2]:
                l2 = m2 + 1
            elif target < matrix[m][m2]:
                r2 = m2 - 1
            else:
                return True
        return False