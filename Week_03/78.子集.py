#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#


# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #方法1：回溯
        def helper(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i + 1, path)
                path.pop()

        res = []
        helper(0, [])
        return res

        '''
        #方法2：递归
        res = [[]]
        for num in nums:
            res += [item + [num] for item in res]
        return res

        #方法3：
        def helper(n, k, start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n - k + len(path) + 1):
                path.append(nums[i])
                helper(n, k, i + 1, path)
                path.pop()
        n = len(nums)
        res = []
        for k in range(n + 1):
            helper(n, k, 0, [])
        return res
        '''


# @lc code=end
