#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import string
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:

        wordSet = set(wordList)
        if not wordSet or endWord not in wordSet:
            return 0
        n = len(beginWord)

        def combo(word):
            for i in range(n):
                for c in string.ascii_lowercase:
                    tmp = word[:i] + c + word[i + 1:]
                    if tmp in wordSet:
                        yield tmp

        #BFS
        visited = {beginWord}
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            w, cnt = q.popleft()
            if w == endWord:
                return cnt
            for nxt in combo(w):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, cnt + 1))
        return 0
        '''
        #双向BFS
        def _bfs(q, visited, other_visited):
            w, cnt = q.popleft()
            for nxt in combo(w):
                if nxt in other_visited:
                    return cnt + other_visited[nxt]
                if nxt not in visited:
                    visited[nxt] = cnt + 1
                    q.append((nxt, cnt + 1))
            return 0

        begin_visited = {beginWord: 1}
        end_visited = {endWord: 1}
        q_begin = collections.deque([(beginWord, 1)])
        q_end = collections.deque([(endWord, 1)])
        while q_begin and q_end:
            res = _bfs(q_begin, begin_visited, end_visited)
            if res:
                return res
            res = _bfs(q_end, end_visited, begin_visited)
            if res:
                return res
        return 0
        '''


# @lc code=end
