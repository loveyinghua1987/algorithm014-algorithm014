#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrace(board, row):
            if row == len(board):
                temp = [''.join(erow) for erow in board]
                res.append(temp[:])
                return
            for col in range(len(board[0])):
                if not isValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrace(board, row + 1)
                board[row][col] = '.'

        def isValid(board, row, col):
            n = len(board)
            for i in range(n):
                if board[i][col] == 'Q':
                    return False
            r_row, r_col = row, col
            while r_row > 0 and r_col < n - 1:
                r_row -= 1
                r_col += 1
                if board[r_row][r_col] == 'Q':
                    return False
            l_row, l_col = row, col
            while l_row > 0 and l_col > 0:
                l_row -= 1
                l_col -= 1
                if board[l_row][l_col] == 'Q':
                    return False
            return True

        board = [['.'] * n for _ in range(n)]
        res = []
        backtrace(board, 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.solveNQueens(4))
# @lc code=end
