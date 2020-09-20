#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治）  sub(j) = max(sub(j-1) + nums[j], nums[j])
        #2. 定义状态数组    dp[j] nums[j]结尾的连续子数组的最大和
        #3. dp方程          dp[j] = max(dp[j-1] + nums[j], nums[j])
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
        
        #方法2：动态规划 + 空间优化
        #时间复杂度： O(n)
        #空间复杂度： O(1)
        n = len(nums)
        prev = nums[0]
        res = nums[0]
        for i in range(1, n):
            prev = max(prev + nums[i], nums[i])
            res = max(res, prev)
        return res
        '''
        #方法3：
        # 从正数开始加，加到负数后，又重新开始寻找下一个开始的正数
        # 一轮循环后，nums里面最大的数，即为子序列和的最大值
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


# @lc code=end
