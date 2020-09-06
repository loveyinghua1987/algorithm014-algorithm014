#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        #DFS会超时，用BFS
        #方法1：BFS
        wordList = set(wordList)
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        n = len(beginWord)
        all_combo_word = collections.defaultdict(list)
        for word in wordList:
            for i in range(n):
                all_combo_word[word[:i] + '*' + word[i + 1:]].append(word)
        q = collections.deque()
        q.append((beginWord, 1))
        visited = {beginWord: True}
        while q:
            word, level = q.popleft()
            for i in range(n):
                for nxt in all_combo_word[word[:i] + '*' + word[i + 1:]]:
                    if nxt not in visited:
                        if nxt == endWord:
                            return level + 1
                        visited[nxt] = True
                        q.append((nxt, level + 1))
        return 0


# @lc code=end
