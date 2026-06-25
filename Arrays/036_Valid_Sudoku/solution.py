class Solution(object):
    def isValidSudoku(self, board):
        for i in range(len(board)):
            seen=set()
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    else:
                        seen.add(board[i][j])
        for i in range(len(board[0])):
            seen=set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in seen:
                        return False
                    else:
                        seen.add(board[j][i])
        for i in range(0,9,3):
            iterator=0
            seen=set()
            while True:
                if board[i][iterator] in seen:
                    return False
                if board[i][iterator]!=".":
                    seen.add(board[i][iterator])
                if board[i+1][iterator] in seen:
                    return False
                if board[i+1][iterator]!=".":
                    seen.add(board[i+1][iterator])
                if board[i+2][iterator] in seen:
                    return False
                if board[i+2][iterator]!=".":
                    seen.add(board[i+2][iterator])

                iterator+=1
                if iterator==3 or iterator==6:
                    seen.clear()
                if iterator==9:
                    break

        return True
                
                
                