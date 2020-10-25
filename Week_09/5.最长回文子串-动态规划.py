#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #动态规划
        # dp[i][j]:s的下标i到下标j之间的子串是否是回文子串
        # dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i+1][j-1])
        #时间复杂度：O(n^2)
        #空间复杂度：O(n^2)
        res = ''
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i < 2 or dp[i + 1][j - 1])
                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res


# @lc code=end
