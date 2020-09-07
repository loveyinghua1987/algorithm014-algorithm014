#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:  #前半部分为升序
                if nums[left] <= target < nums[mid]:  #target在前半部分
                    right = mid - 1
                else:
                    left = mid + 1
            else:  #后半部分为升序
                if nums[mid] < target <= nums[right]:  #target在后半部分
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


# @lc code=end
