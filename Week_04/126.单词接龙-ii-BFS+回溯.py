#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from typing import List
import string
import collections


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        n = len(beginWord)
        #产生dict{单词：下一个符合要求的单词列表}
        def bfs(beginword, successors):
            found = False
            q = collections.deque()
            q.append(beginWord)
            visited = {beginWord}
            nxt_visited = set()
            while q:
                size = len(q)
                for _ in range(size):
                    word = q.popleft()
                    for i in range(n):
                        for c in string.ascii_lowercase:
                            nxt = word[:i] + c + word[i + 1:]
                            if nxt in wordSet:
                                if nxt not in visited:
                                    if nxt == endWord:
                                        found = True
                                    if nxt not in nxt_visited:
                                        nxt_visited.add(nxt)
                                        q.append(nxt)
                                    successors[word].add(nxt)
                if found:
                    break
                visited |= nxt_visited
                nxt_visited.clear()
            return found

        #回溯
        def dfs(beginWord, path):
            if beginWord == endWord:
                res.append(path[:])
                return
            if beginWord not in successors:
                return
            for nxt in successors[beginWord]:
                path.append(nxt)
                dfs(nxt, path)
                path.pop()

        visited = {beginWord}
        nxt_visited = set()
        res = []
        #successors = {word : nxt_level_words}
        successors = collections.defaultdict(set)
        found = bfs(beginWord, successors)
        if not found:
            return res
        path = [beginWord]
        dfs(beginWord, path)
        return res


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    solution = Solution()
    res = solution.findLadders(beginWord, endWord, wordList)
    print(res)
# @lc code=end
