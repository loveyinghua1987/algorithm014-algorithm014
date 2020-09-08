#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
import collections
import string


class Solution:
    def findLadders(self, beginWord: str, endWord: str,
                    wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        n = len(beginWord)

        def bin_bfs(beginWord, successors):
            visited = {beginWord, endWord}
            visited_begin = {beginWord}
            visited_end = {endWord}

            found = False
            forward = True
            while visited_begin:
                if len(visited_begin) > len(visited_end):
                    visited_begin, visited_end = visited_end, visited_begin
                    forward = not forward
                nxt_visited = set()
                for word in visited_begin:
                    for i in range(n):
                        for c in string.ascii_lowercase:
                            nxt = word[:i] + c + word[i + 1:]
                            if nxt in wordSet:
                                if nxt in visited_end:
                                    found = True
                                    add_to_successors(successors, forward,
                                                      word, nxt)
                                if nxt not in visited:
                                    nxt_visited.add(nxt)
                                    add_to_successors(successors, forward,
                                                      word, nxt)
                visited_begin = nxt_visited
                visited |= nxt_visited
                if found:
                    break
            return found

        def add_to_successors(successors, forward, word, nxt):
            if forward:
                successors[word].add(nxt)
            else:
                successors[nxt].add(word)

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

        res = []
        successors = collections.defaultdict(set)
        found = bin_bfs(beginWord, successors)
        if not found:
            return res
        dfs(beginWord, [beginWord])
        return res

        # @lc code=end
