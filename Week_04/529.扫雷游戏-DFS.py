#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        #DFS
        def dfs(board, i, j):
            #terminator
            cnt = 0
            for dx, dy in d:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                    cnt += 1
            if cnt > 0:
                board[i][j] = str(cnt)
                return
            #process current logic
            board[i][j] = 'B'
            for dx, dy in d:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'E':
                    #drill down
                    dfs(board, x, y)
            #reverse

        m = len(board)
        if not m:
            return []
        n = len(board[0])
        d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
             (1, -1)]
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
        else:
            dfs(board, i, j)
        return board


# @lc code=end
