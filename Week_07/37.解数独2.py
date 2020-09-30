#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#


# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        self.solve(board)

    def solve(self, board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for c in [str(i) for i in range(1, 10)]:
                        if self.isValid(board, i, j, c):
                            board[i][j] = c
                            if self.solve(board):
                                return True
                            board[i][j] = '.'
                    return False
        return True

    def isValid(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c: return False
            if board[i][col] == c: return False
            if board[(row // 3) * 3 +
                     i // 3][(col // 3) * 3 + i % 3] != '.' and board[
                         (row // 3) * 3 + i // 3][(col // 3) * 3 + i % 3] == c:
                return False
        return True


# @lc code=end
