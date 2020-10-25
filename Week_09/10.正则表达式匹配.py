#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #方法2：动态规划
        # dp[i][j]: s的前i个字符与p的前j个字符是否匹配

        # def matchs(i, j):
        #     if i == 0:
        #         return False
        #     if p[j - 1] == '.':
        #         return True
        #     return s[i - 1] == p[j - 1]
        matchs = lambda i, j: i > 0 and p[j - 1] in {s[i - 1], '.'}
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    if matchs(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                    dp[i][j] |= dp[i][j - 2]
                else:
                    if matchs(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[m][n]
        '''
        #方法1：递归
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >=2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

        '''


# @lc code=end
