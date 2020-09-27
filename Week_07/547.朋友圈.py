#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 朋友圈
#


# @lc code=start
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        #方法1： DFS/BFS（类似岛屿数量问题）
        #DFS
        # 时间复杂度：O(n^2)
        # 空间复杂度：O(n)
        if not M: return 0
        count = 0
        visited = set()
        for i in range(len(M)):
            if i not in visited:
                self._dfs(M, visited, i)
                count += 1
        return count

    def _dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and j not in visited:
                visited.add(j)
                self._dfs(M, visited, j)
        '''
        #方法2：并查集
        #时间复杂度：O(n^3)
        #空间复杂度：O(n)
        if not M: return 0
        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    self._union(p, i, j)
        return len(set(self._parent(p, i) for i in range(n)))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p2] = p1

    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            p[i], i = root, p[i]
        return root


# @lc code=end
