#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        #方法2：双指针
        i, j = 0, len(height)-1
        max_left, max_right = 0, 0
        water = 0
        while i < j:
            if height[i] < height[j]:  #height[i] < height[j] <= max_right
                if height[i] >= max_left: # max_left <= height[i] < height[j] <= max_right
                    max_left = height[i]
                else: #height[i] < max_left  
                    water += max_left - height[i]
                i += 1
            else:# height[i] >= height[j]
                if height[j] >= max_right:#max_left >= height[i] >= height[j] >= max_right
                    max_right = height[j]
                else:
                    water +=max_right - height[j]
                j -= 1
        return water

        '''
        #方法1：栈
        stack = []
        water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                j = stack.pop()
                if not stack:
                    continue
                water +=( min(height[stack[-1]], height[i]) - height[j])*(i - stack[-1]-1)
            stack.append(i)
        return water
        '''

# @lc code=end
