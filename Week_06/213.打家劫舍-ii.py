#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        #动态规划
        #198.打家劫舍 求解了偷n个房子能偷到的最高金额
        #此题，第一个房子和最后一个房子只能偷其中一个
        #此时有三种情况：
        # case1： 第一个房子偷，最后一个房子不可偷
        # case2： 第一个房子不偷，最后一个房子可偷
        # case3： 第一个房子不偷， 最后一个房子不偷
        #明显，case3是包含在case2中的，所以只需要考虑case1和case2即可
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        if not nums:
            return 0
        n = len(nums)
        if n == 1: return nums[0]

        def helper(nums):
            pre, cur = 0, 0
            for num in nums:
                cur, pre = max(cur, pre + num), cur
            return cur

        return max(helper(nums[:n - 1]), helper(nums[1:]))


# @lc code=end