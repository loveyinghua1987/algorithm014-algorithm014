#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#


# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #贪心
        g.sort()
        s.sort()
        i = j = 0
        cnt = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt


# @lc code=end
