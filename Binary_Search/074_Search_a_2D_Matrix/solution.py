class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        ROWS, COLS = len(matrix), len(matrix[0])

        top = 0
        bot = ROWS - 1

        while top <= bot:

            midrow = (top + bot) // 2

            if target > matrix[midrow][-1]:
                top = midrow + 1

            elif target < matrix[midrow][0]:
                bot = midrow - 1

            else:
                break

        if not (top <= bot):
            return False

        mid = (top + bot) // 2

        l = 0
        r = COLS - 1

        while l <= r:

            m = (l + r) // 2

            if target > matrix[mid][m]:
                l = m + 1

            elif target < matrix[mid][m]:
                r = m - 1

            else:
                return True

        return False