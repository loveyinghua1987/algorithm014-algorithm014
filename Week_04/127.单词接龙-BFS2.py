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
        #BFS2
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        q.append((next_word, length + 1))
        return 0

        '''
        #BFS2
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        visited = {beginWord}

        def combo_words(w):
            for i in range(len(w)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    temp = w[:i] + c + w[i + 1:]
                    if temp in wordList:
                        yield temp

        q = collections.deque()
        q.append((beginWord, 1))
        while q:
            w, l = q.popleft()
            for x in combo_words(w):
                if x not in visited:
                    if x == endWord:
                        return l + 1
                    visited.add(x)
                    q.append((x, l + 1))
        return 0
        '''


# @lc code=end
