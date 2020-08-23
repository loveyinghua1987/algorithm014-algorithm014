#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #广度优先搜索
        num = 0
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == '1':
                    num += 1
                    grid[i][j] == '0'
                    q = collections.deque([(i, j)])
                    while q:
                        r, c = q.popleft()
                        for x, y in [(r - 1, c), (r + 1, c), (r, c - 1),
                                     (r, c + 1)]:
                            if 0 <= x < nr and 0 <= y < nc and grid[x][
                                    y] == '1':
                                grid[x][y] = '0'
                                q.append((x, y))
        return num


# @lc code=end
