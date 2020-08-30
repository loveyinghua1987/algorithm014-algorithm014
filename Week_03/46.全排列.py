#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#


# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        #回溯
        def helper(nums, per):
            if len(per) == len(nums):
                res.append(per.copy())
                return
            for num in nums:
                if num not in per:
                    per.append(num)
                    helper(nums, per)
                    per.pop()

        res = []
        helper(nums, [])
        return res
        '''

        def helper(nums, path):
            if not nums:
                res.append(path[:])
            for i in range(len(nums)):
                helper(nums[:i] + nums[i + 1:], path + [nums[i]])

        res = []
        helper(nums, [])
        return res
		'''
# @lc code=end
