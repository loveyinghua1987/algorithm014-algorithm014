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
        #双向BFS
        wordList = set(wordList)
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        n = len(beginWord)
        all_combo_dict = collections.defaultdict(list)

        for word in wordList:
            for i in range(n):
                all_combo_dict[word[:i] + '*' + word[i + 1:]].append(word)

        def bfs(q, visited, other_visited):
            word, level = q.popleft()
            for i in range(n):
                for nxt in all_combo_dict[word[:i] + '*' + word[i + 1:]]:
                    if nxt in other_visited:
                        return level + other_visited[nxt]
                    if nxt not in visited:
                        if nxt == endWord:
                            return level + 1
                        visited[nxt] = level + 1
                        q.append((nxt, level + 1))
            return 0

        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        q_begin = collections.deque([(beginWord, 1)])
        q_end = collections.deque([(endWord, 1)])
        while q_begin and q_end:
            res = bfs(q_begin, visited_begin, visited_end)
            if res:
                return res
            res = bfs(q_end, visited_end, visited_begin)
            if res:
                return res
        return 0


# @lc code=end
