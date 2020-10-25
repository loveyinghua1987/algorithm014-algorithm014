#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#


# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        m, n = len(s), len(p)

        scnt = collections.Counter(s[:n - 1])
        pcnt = collections.Counter(p)

        for i in range(n - 1, m):
            scnt[s[i]] += 1
            if scnt == pcnt:
                res.append(i - n + 1)
            scnt[s[i - n + 1]] -= 1
            if scnt[s[i - n + 1]] == 0:
                #del scnt[s[i - n + 1]]
                scnt.pop(s[i - n + 1])
        return res


# @lc code=end
