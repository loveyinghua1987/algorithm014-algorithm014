#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#


# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:
            return nums[left]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] >= nums[left]:  #左边有序
                left = mid + 1
            else:  #右边有序
                right = mid - 1


# @lc code=end
