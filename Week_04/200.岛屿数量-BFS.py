#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    grid[i][j] = '0'
                    q = collections.deque()
                    q.append((i, j))
                    while q:
                        r, c = q.popleft()
                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1),
                                     (r, c + 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '0'
                                q.append((x, y))

        return count


# @lc code=end
