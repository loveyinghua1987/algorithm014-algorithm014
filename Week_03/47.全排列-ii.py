#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(visited, per):
            if len(visited) == n:
                res.append(per[:])
                return 
            for i in range(n):
                if i in visited:
                    continue
                if i >0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue
                helper(visited + [i], per + [nums[i]])
                #visited.append(i)
                #per.append(nums[i])
                #helper(visited, per)
                #visited.pop()
                #per.pop()

        n = len(nums)
        nums.sort()
        res = []
        helper([], [])
        return res

# @lc code=end 

