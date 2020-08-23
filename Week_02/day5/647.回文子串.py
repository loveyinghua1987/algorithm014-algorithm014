#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        #中心拓展   
        n = len(s)
        res = 0
        #l= i/2  r=i/2+i%2   i:0~2n-1
        for i in range(2 * n - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
   
# @lc code=end
