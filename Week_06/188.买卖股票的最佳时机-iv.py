#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(nk)
        #空间复杂度：O(k)
        def maxProfit(prices):
            n = len(prices)
            if not n: return 0
            nothold, hold = 0, float('-inf')
            for i in range(n):
                nothold, hold = max(nothold, hold + prices[i]), max(
                    hold, nothold - prices[i])
            return nothold

        n = len(prices)
        if not n: return 0
        if k >= n / 2:  #买卖是成对的，最多只能买n/2次， 如果大于这个数的话，就变成不限制交易次数leetcode122
            return maxProfit(prices)
        #写法2
        dp = [[0] * 2 for _ in range(k + 1)]
        for i in range(k + 1):
            dp[i][1] = float('-inf')

        for i in range(n):
            for j in range(1, k + 1):
                dp[j][0], dp[j][1] = max(dp[j][0], dp[j][1] + prices[i]), max(
                    dp[j][1], dp[j - 1][0] - prices[i])
        return dp[-1][0]
        '''
        #方法1.动态规划
        #时间复杂度：O(nk）
        #空间复杂度：O(nk）
        #1. 重复性（分治）
        #   sub(i, k, 0) = max(sub(i-1, k, 0), sub(i-1, k, 1) + prices(i))
        #   sub(i, k, 1) = max(sub(i-1, k, 1), sub(i-1, k-1, 0) - prices(i))
        #2. 定义状态数组
        #   dp[i][k][0] : 最多进行k交易时，第i天没有持有股票的最大获利
        #   dp[i][k][1] : 最多进行k交易时，第i天持有股票的最大获利
        #3. dp方程
        #   dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i-1])
        #   dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i-1])

        def maxProfit(prices):
            n = len(prices)
            if not n: return 0
            nothold, hold = 0, float('-inf')
            for i in range(n):
                nothold, hold = max(nothold, hold + prices[i]), max(
                    hold, nothold - prices[i])
            return nothold

        n = len(prices)
        if not n: return 0
        if k >= n / 2:   #买卖是成对的，最多只能买n/2次， 如果大于这个数的话，就变成不限制交易次数leetcode122
            return maxProfit(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = float('-inf')
        for i in range(1, n + 1):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0],
                                  dp[i - 1][j][1] + prices[i - 1])
                dp[i][j][1] = max(dp[i - 1][j][1],
                                  dp[i - 1][j - 1][0] - prices[i - 1])
        return dp[-1][-1][0]
        '''


# @lc code=end
