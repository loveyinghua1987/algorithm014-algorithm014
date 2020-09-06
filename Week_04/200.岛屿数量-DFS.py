#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#


# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        def dfs(grid, r, c):
            grid[r][c] = '0'
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    dfs(grid, x, y)

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(grid, i, j)
        return cnt


# @lc code=end
