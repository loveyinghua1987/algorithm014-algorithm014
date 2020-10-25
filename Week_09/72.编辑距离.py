#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #动态规划
        #时间复杂度：O(mn)
        #空间复杂度：O(mn)
        #重复性（分治）
        # if word1[i-1] == word2[j-1]: sub(i, j) = sub(i-1, j-1)
        # if word1[i-1] != word2[j-1]:
        #     sub(i, j) = min(sub(i-1, j-1)[+替换], sub(i-1, j)(+删除), sub(i, j-1)[+插入]) + 1
        #定义状态数组   dp[i][j]: word1[: i+1] 到 word2[: j+1]的最小操作数
        #dp方程  dp[i][j] = dp[i-1][j-1]  if word1[i-1] == word2[j-1]
        #   dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + 1  #插入
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + 1  #删除
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j],
                                   dp[i][j - 1]) + 1
        return dp[-1][-1]


# @lc code=end
