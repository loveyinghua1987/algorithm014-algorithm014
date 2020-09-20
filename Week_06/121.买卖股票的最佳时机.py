#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度： O(n)
        #空间复杂度：O(1)
        n = len(prices)
        if not n: return 0
        nothold, hold = 0, float('-inf')
        for i in range(n):
            nothold, hold = max(nothold,hold + prices[i]), max(hold, -prices[i])
        return max(nothold, hold)
        
        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治）：sub(i, 1, 0) = max(sub(i-1, 1, 0), sub(i-1, 1, 1) + prices(i)
        #                  sub(i, 1, 1) = max(sub(i-1, 1, 1), sub(i-1, 0, 0) - price(i)
        #2. 定义状态数组    dp[i][k][0]: 在最多允许k次交易时，第i天手上没有持有股票的最大获利
        #                  dp[i][k][1]: 在最多允许k次交易时，第i天手上持有股票的最大获利
        #                  price(i) : 第i天的价格
        #3. dp方程:   dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i -1])
        #             dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i -1])
        #                         = max(dp[i-1][1][1], - prices[i-1])
        #             dp[i][0][0] = dp[]i-1[0][0]= ... = dp[0][0][0] = 0
        #
        #         --->dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i -1])
        #             dp[i][1] = max(dp[i-1][1], - prices[i-1])
        #
        #
        #初始情况： dp[0][0] = dp[0][1][0] = 0
        #          dp[0][1] = dp[0][1][1] = float('-inf')  #股市还没开始，不允许持股，获利初始化为负无穷
        
        n = len(prices)
        if not n: return 0
        dp = [[0] * 2 for _ in range(n + 1)]  #n+1行2列
        dp[0][1] = float('-inf')

        for i in range(1, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i - 1])
            dp[i][1] = max(dp[i - 1][1], -prices[i - 1])

        return max(dp[n])
        '''


# @lc code=end
