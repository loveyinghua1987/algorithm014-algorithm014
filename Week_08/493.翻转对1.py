#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#


# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        #时间复杂度：O(nlogn*logn)
        #空间复杂度：O(n)
        if not nums: return 0
        return self.mergeSort(nums, 0, len(nums) - 1)

    def mergeSort(self, nums, l, r):
        if l >= r: return 0
        mid = l + ((r - l) >> 1)
        cnt = self.mergeSort(nums, l, mid) + self.mergeSort(nums, mid + 1, r)
        i = l
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] / 2 <= nums[j]:
                i += 1
            cnt += mid - i + 1
        nums[l:r + 1] = sorted(nums[l:r + 1])  #O(nlogn)
        return cnt


# @lc code=end
