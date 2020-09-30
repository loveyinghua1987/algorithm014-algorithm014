#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import string


class Solution:
    def ladderLength(self, beginWord: str, endWord: str,
                     wordList: List[str]) -> int:
        #写法1
        if not wordList or endWord not in wordList: return 0
        wordSet = set(wordList)
        beginSet, endSet = {beginWord}, {endWord}
        word_len = len(beginWord)
        dis = 1

        while beginSet:
            dis += 1
            nxt_beginSet = set()
            for word in beginSet:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            nxt = word[:i] + c + word[i + 1:]
                            if nxt in endSet:
                                return dis
                            if nxt in wordSet:
                                nxt_beginSet.add(nxt)
                                wordSet.remove(nxt)
            beginSet = nxt_beginSet
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
        return 0
        '''
        #写法2
        if not wordList or endWord not in wordList: return 0
        wordSet = set(wordList)
        beginSet, endSet = {beginWord}, {endWord}
        visited = set()
        word_len = len(beginWord)
        dis = 1

        while beginSet:
            dis += 1
            nxt_beginSet = set()
            for word in beginSet:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            nxt = word[:i] + c + word[i + 1:]
                            if nxt in endSet:
                                return dis
                            if nxt in wordSet and nxt not in visited:
                                nxt_beginSet.add(nxt)
                                visited.add(nxt)
            beginSet = nxt_beginSet
        return 0
        '''
# @lc code=end
