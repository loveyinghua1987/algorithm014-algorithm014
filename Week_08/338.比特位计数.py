#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#


# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        #位运算 + DP
        #方法1：
        #状态转移方程：dp[n] = dp[n & n - 1] + 1
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i & i - 1] + 1
        return dp
        '''
        #方法2：
        #状态转移方程：dp[n] = dp[n >> 1] + (n & 1)
        dp = [0] * (num + 1)
        for i in range(1, num + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
        '''

# @lc code=end
