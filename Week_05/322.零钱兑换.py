#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #方法1：动态规划
        #时间复杂度：O(amount*len(coins))
        #空间复杂度：O(amount)
        #1. 重复性（分治） sub(n) = min(sub(n-coin)+1 for coin in coins)
        #2. 定义状态数组   dp[n]: 凑成n所需的最少硬币个数
        #3. dp方程        dp[n] = min(dp[n-coin]+1 for coin in coins)
        #这个有个问题，有可能出现没有任何一种硬币组合能组成的金额，
        #所以，最终需要判定 dp[n] 是否为初始的float('inf')’, 即没找到，返回-1
        
        #写法1
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i < coin: continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1
        
        #写法2
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
        '''
        #方法2： 记忆化搜索递归
        memo = {}

        def helper(n):
            #terminator
            if n < 0: return -1
            if n == 0: return 0
            if n in memo:
                return memo[n]
            res = float('inf')
            for coin in coins:
                sub = helper(n - coin)
                if sub == -1: continue
                res = min(res, sub + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]

        return helper(amount)
        
        '''
# @lc code=end
