#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start


# 并查集
class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.rank = [0] * N
        self.count = 0

    def _find(self, i):
        root = i
        while self.parent[root] != root:
            root = self.parent[root]
        while self.parent[i] != i:
            self.parent[i], i = root, self.parent[i]
        return root

    def _union(self, x, y):
        rootx = self._find(x)
        rooty = self._find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count

    def isConnected(self, x, y):
        return self._find(x) == self._find(y)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n + 1)
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0
                        or j == n - 1) and board[i][j] == 'O':
                    uf._union(i * n + j, m * n)
                elif board[i][j] == 'O':
                    for d in directions:
                        x, y = i + d[0], j + d[1]
                        if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                            uf._union(i * n + j, x * n + y)
        for i in range(m):
            for j in range(n):
                if not uf.isConnected(i * n + j, m * n) and board[i][j] == 'O':
                    board[i][j] = 'X'


# @lc code=end
