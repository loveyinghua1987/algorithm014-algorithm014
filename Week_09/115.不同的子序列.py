#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#


# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #动态规划
        #dp[i][j] :t的前i个字符在s的前j个字符的子序列出现的个数
        #dp[i][j] = dp[i-1][j-1] + dp[i][j-1] if t[i-1] == s[j-1]
        #dp[i][j] = dp[i][j-1]                if t[i-1] != s[j-1]
        m, n = len(t), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = [1 for i in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]


# @lc code=end
