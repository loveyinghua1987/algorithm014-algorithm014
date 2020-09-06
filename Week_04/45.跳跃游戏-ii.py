#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        #写法2：
        steps = max_pos = end = 0

        for i in range(len(nums)-1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                steps += 1
                end = max_pos
        return steps
        '''
        #写法1
        if len(nums) <= 1:
            return 0
        l, r = 0, nums[0]
        steps = 1
        while r < len(nums) - 1:
            steps += 1
            nxt = max([i + nums[i] for i in range(l, r + 1)])
            l, r = r, nxt
        return steps
        '''


# @lc code=end
