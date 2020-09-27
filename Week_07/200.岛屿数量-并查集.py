#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
#并查集


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.parent = [-1] * m * n
        self.rank = [0] * m * n
        self.count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
            self.count -= 1

    def find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != i:
            self.parent[i], i = root, self.parent[i]
        return root


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        m, n = len(grid), len(grid[0])
        uf = UnionFind(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                            uf.union(i * n + j, x * n + y)
        return uf.count


# @lc code=end
