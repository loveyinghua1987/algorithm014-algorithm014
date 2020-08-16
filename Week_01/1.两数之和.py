#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#


# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #hashtable  时间复杂度：O(n)
        hash = dict()
        for i, num in enumerate(nums):
            num1 = target - num
            if num1 in hash:
                return [hash[num1], i]
            hash[num] = i
        return []


# @lc code=end
