class Solution(object):
    def isValidSudoku(self, board):

        # Row Check
        for i in range(len(board)):
            seen = set()

            for j in range(len(board[0])):
                if board[i][j] != ".":

                    if board[i][j] in seen:
                        return False

                    seen.add(board[i][j])

        # Column Check
        for i in range(len(board[0])):
            seen = set()

            for j in range(len(board)):
                if board[j][i] != ".":

                    if board[j][i] in seen:
                        return False

                    seen.add(board[j][i])

        # Box Check
        for i in range(0, 9, 3):

            iterator = 0
            seen = set()

            while True:

                for r in range(i, i + 3):

                    if board[r][iterator] != ".":

                        if board[r][iterator] in seen:
                            return False

                        seen.add(board[r][iterator])

                iterator += 1

                # End of current box
                if iterator == 3 or iterator == 6:
                    seen.clear()

                if iterator == 9:
                    break

        return True