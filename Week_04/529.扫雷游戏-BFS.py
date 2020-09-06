#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#


# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]],
                    click: List[int]) -> List[List[str]]:
        #BFS
        m = len(board)
        if not m:
            return []
        n = len(board[0])
        d = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),
             (1, -1)]
        i, j = click[0], click[1]
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        visited = set()
        visited.add((i, j))
        q = collections.deque()
        q.append((i, j))
        while q:
            r, c = q.popleft()
            cnt = 0
            for dx, dy in d:
                x, y = r + dx, c + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'M':
                    cnt += 1
            if cnt > 0:
                board[r][c] = str(cnt)
            else:
                board[r][c] = 'B'
                for dx, dy in d:
                    x, y = r + dx, c + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 'E':
                        if (x, y) not in visited:
                            visited.add((x, y))
                            q.append((x, y))
        return board


# @lc code=end
