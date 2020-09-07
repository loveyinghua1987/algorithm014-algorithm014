#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#


# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #二分查找
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                #前面升序 或 后面是升序，且target小于右边界
                if nums[mid] >= nums[left] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:  # nums[mid] > target
                #后面是升序 或前面是升序，且target大于左边界
                if nums[mid] <= nums[right] or target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

# @lc code=end
