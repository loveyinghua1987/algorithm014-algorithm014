#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #方法2：动态规划 + 空间优化
        a = b = 1
        for i in range(n):
            b, a = a + b, b
        return a
        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治） sub(n) = sub(n-1) + sub(n-2)
        #2. 定义状态数组   dp[n] 到n阶台阶的方法数
        #3. dp方程 dp[n] = dp[n-1] + dp[n-2]
        dp = [1, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
        '''


# @lc code=end
