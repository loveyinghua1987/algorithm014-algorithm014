#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#


# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #方法2：动态规划+空间优化
        m, n = len(text1), len(text2)
        #if m < n: return self.longestCommonSubsequence(text2, text1)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            pre = 0
            for j in range(1, n + 1):
                cur = dp[j]
                dp[j] = pre + 1 if text1[i - 1] == text2[j - 1] else max(
                    dp[j - 1], cur)
                pre = cur
        return dp[-1]
        '''
        #方法1：动态规划
        #时间复杂度：O(m*n)
        #空间复杂度：O(m*n)
        #1. 重复性（分治）
        #   sub(i, j) = sub(i-1, j-1) + 1 if text1[i-1] == text2[j-1]
        #   sub(i, j) = max(sub(i-1, j), sub(i,j-1))  if text1[i=1] != text2[j=1]
        #2. 定义状态数组  dp[i][j]: text1的前i个字符串和text2的前j个字符串的最长公共子序列的长度
        #3. dp方程  dp[i][j] = dp[i-1][j-1] + 1 if text1[i-1] == text2[j-1]
        #                    = max(dp[i-1][j] , dp[i][j-1]) if text1[i-1] != text2[j-1]
        
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
        '''


# @lc code=end
