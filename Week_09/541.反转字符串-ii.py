#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#


# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        if k <= 1: return s
        ls = list(s)
        for i in range(0, len(ls) - 1, 2 * k):
            ls[i:i + k] = reversed(ls[i:i + k])
            #ls[i:i + k] = ls[i:i + k][::-1]
        return ''.join(ls)


# @lc code=end
