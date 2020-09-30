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
        rows = [set(range(1, 10)) for _ in range(9)]  #行剩余可用数字
        cols = [set(range(1, 10)) for _ in range(9)]  #列剩余可用数字
        blocks = [set(range(1, 10)) for _ in range(9)]  #块剩余可用数字
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':  #更新可用数字
                    b = (i // 3) * 3 + j // 3
                    val = int(board[i][j])
                    rows[i].remove(val)
                    cols[j].remove(val)
                    blocks[b].remove(val)
                else:
                    empty.append((i, j))

        def backtrace(iter=0):
            if iter == len(empty):  #处理完empty代表找到答案
                return True
            i, j = empty[iter]
            b = (i // 3) * 3 + j // 3
            for val in rows[i] & cols[j] & blocks[b]:
                rows[i].remove(val)
                cols[j].remove(val)
                blocks[b].remove(val)
                board[i][j] = str(val)
                if backtrace(iter + 1):  #回溯
                    return True
                rows[i].add(val)
                cols[j].add(val)
                blocks[b].add(val)
            return False

        backtrace()


# @lc code=end
