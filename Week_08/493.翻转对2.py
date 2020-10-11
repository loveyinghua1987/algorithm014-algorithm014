#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#


# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
	#时间复杂度：O(nlogn)
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
        self.merge(nums, l, mid, r)
        return cnt

    def merge(self, nums, l, mid, r):
        cache = [0] * (r - l + 1)
        i, k = l, 0
        for j in range(mid + 1, r + 1):
            while i <= mid and nums[i] < nums[j]:
                cache[k] = nums[i]
                k, i = k + 1, i + 1
            cache[k] = nums[j]
            k += 1
        while i <= mid:
            cache[k] = nums[i]
            k, i = k + 1, i + 1
        nums[l:r + 1] = cache


# @lc code=end
