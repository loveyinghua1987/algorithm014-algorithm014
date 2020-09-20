#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        n = len(prices)
        if not n: return 0
        nothold2, hold2, nothold1, hold1 = 0, float('-inf'), 0, float('-inf')
        for i in range(n):
            nothold2 = max(nothold2, hold2 + prices[i])
            hold2 = max(hold2, nothold1 - prices[i])
            nothold1 = max(nothold1, hold1 + prices[i])
            hold1 = max(hold1, -prices[i])
        return nothold2

        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1.重复性（分治）  sub(i, 2, 0) = max(sub(i-1, 2, 0), sub(i-1, 2, 1) + prices(i))
        #                 sub(i, 2, 1) = max(sub(i-1, 2, 1), sub(i-1, 1, 0) - prices(i))
        #                 sub(i, 1, 0) = max(sub(i-1, 1, 0), sub(i-1, 1, 1) + prices(i))
        #                 sub(i, 1, 1) = max(sub(i-1, 1, 1), sub(i-1, 0, 0) - prices(i))
        #2. 定义状态数组   dp[i][2][0] : 在最大交易次数为两次时， 第i天没有持有股票的最大获利
        #                 dp[i][2][1] : 在最大交易次数为两次时， 第i天持有股票的最大获利
        #                 dp[i][1][0] : 在最大交易次数为一次时， 第i天没有持有股票的最大获利
        #                 dp[i][1][1] : 在最大交易次数为一次时， 第i天持有股票的最大获利
        #                 prices(i): 第i天的价格
        #3. dp方程   dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i-1])
        #            dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i-1])
        #            dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i-1])
        #            dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i-1])
        #                        = max(dp[i-1][1][1],  - prices[i-1])
        #
        #  初始条件：dp[0][2][0] = 0
        #           dp[0][2][1] = float('-inf')
        #           dp[0][1][0] = 0
        #           dp[0][1][1] = float('-inf')

        n = len(prices)
        if not n: return 0
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]
        dp[0][2][1] = dp[0][1][1] = float('-inf')

        for i in range(1, n + 1):
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i - 1])
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i - 1])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i - 1])
            dp[i][1][1] = max(dp[i - 1][1][1], -prices[i - 1])

        return dp[-1][2][0]
        '''


# @lc code=end
