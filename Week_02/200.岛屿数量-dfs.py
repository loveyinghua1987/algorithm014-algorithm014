#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
import collections

class Solution:
    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        grid[r][c] = '0'
        for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= i < nr and 0 <= j < nc and grid[i][j] == '1':
                self.dfs(grid, i, j)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        #dfs深度优先搜索
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num += 1
                    self.dfs(grid, i, j)
        return num


# @lc code=end

