#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#


# @lc code=start
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        #方法1. 遍历word -> board search
        #   时间复杂度: O(N*m*n*4^k)
        #   N:len(words), m: len(board), n: len(board[0]), k: word的最大长度
        #方法2：Trie
        #   a. all words --> Trie 构建起prefix
        #   b. board, DFS
        #   时间复杂度： O(N*k) + O(n*4^k)
        #               n:board中含有root中元素的个数 < m*n  k: word的最大长度
        #   空间复杂度： Trie所用空间 O(N)

        if not board or not board[0]: return []
        if not words: return []
        self.res = set()
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

        #构建Trie树
        root = {}
        self.end_of_word = "#"
        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char, {})
            node[self.end_of_word] = self.end_of_word

        #DFS board
        self.m, self.n = len(board), len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.res)

    def _dfs(self, board, i, j, cur_word, cur_dict):

        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if self.end_of_word in cur_dict:
            self.res.add(cur_word)
        temp, board[i][j] = board[i][j], "@"
        for k in range(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.m and 0 <= y < self.n and board[x][
                    y] != "@" and board[x][y] in cur_dict:
                self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = temp


# @lc code=end
