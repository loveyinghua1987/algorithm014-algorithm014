#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#

# @lc code=start
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(n)
        #空间复杂度：O(1)
        n = len(nums)
        ma = mi = res = nums[0]

        for i in range(1, n):
            n = nums[i]
            ma, mi = max(ma * n, mi * n, n), min(ma * n, mi * n, n)
            res = max(res, ma, mi)
        return res
        '''
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性（分治） sub(0, i) = max(sub(0, i-1)*nums[i], sub(1, i-1)*nums[i], nums[i])
        #                 sub(1, i) = min(sub(0, i-1)*nums[i], sub(1, i-1)*nums[i], nums[i])
        #2. 定义状态数组   dp[0][i]：nums[i]结尾的连续子数组的最大乘积
        #                  dp[1][i]: nums[i]结尾的连续子数组的最小乘积
        #3. dp方程        dp[0][i] = max(dp[0][i-1]*nums[i], dp[1][i-1]*nums[i], nums[i])
        #                 dp[1][i] = min(dp[0][i-1]*nums[i], dp[1][i-1]*nums[i], nums[i])

        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = dp[1][0] = nums[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i],
                           nums[i])
            dp[1][i] = min(dp[0][i - 1] * nums[i], dp[1][i - 1] * nums[i],
                           nums[i])
        return max(dp[0])
        '''


if __name__ == "__main__":
    s = Solution()
    print(s.maxProduct([2, 3, -2, 4]))
# @lc code=end
