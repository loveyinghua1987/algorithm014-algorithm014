#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        n = len(prices)
        if not n: return 0
        nothold = 0
        prenothold = 0
        hold = float('-inf')
        for i in range(n):
            nothold, hold, prenothold = max(nothold, hold + prices[i]), max(
                hold, (prenothold if i >= 1 else 0) - prices[i]), nothold
        return nothold
        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治） sub(i,0) = max(sub(i-1, 0), sub(i-1, 1) + prices(i))
        #                 sub(i,1) = max(sub(i-1, 1), sub(i-2, 0) - prices(i))
        #         卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天),对卖出有限制
        #2. 定义状态数组   dp[i][0] : 不限交易次数时，第i天没有持有股票的最大获利
        #                 dp[i][1] : 不限交易次数时，第i天持有股票的最大获利
        #3. dp方程   dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i-1])
        #            dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i-1])

        n = len(prices)
        if not n: return 0
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0][1] = float('-inf')

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1],
                           (dp[i - 2][0] if i >= 2 else 0) - prices[i - 1])

        return dp[-1][0]
        '''


# @lc code=end
