#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        box_indexs =[{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_index = (i // 3) * 3 + j //3
                    num = int(board[i][j])
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    box_indexs[box_index][num] = box_indexs[box_index].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or box_indexs[box_index][num] > 1:
                        return False
        return True
# @lc code=end

