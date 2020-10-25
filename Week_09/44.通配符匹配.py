#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #动态规划
        #dp[i][j]: s的前i个字符与p的前j个字符是否匹配
        #matchs = lambda i, j: i > 0 and p[j-1] in {s[i-1], '?'}
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                else:
                    #if matchs(i, j):
                    if i > 0 and p[j - 1] in {s[i - 1], '?'}:
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]


# @lc code=end
