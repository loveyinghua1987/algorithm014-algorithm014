#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        n = len(nums)
        if not n: return 0
        if n == 1: return nums[0]
        pre, cur = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            cur, pre = max(cur, pre + nums[i]), cur
        return cur
        
        '''
        #方法1： 动态规划 
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治）  sub(n) = max(sub(n-1), sub(n-2) + nums[n])
        #                  可以拆分成第n个房间不偷（sub(n-1)）和
        #                  偷（这个时候n-1房子不能偷，
        #                  所以是sub(n-2) + nums[n]）两个个子问题
        #2. 定义状态数组    dp[n] : 小偷偷前n个房屋的最大金额
        #3. dp方程         dp[n] = max(dp[n-1], dp[n-2]+nums[n]
        n = len(nums)
        if not n: return 0
        if n == 1: return nums[0]
        dp = [0] * n
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]
        '''


# @lc code=end
