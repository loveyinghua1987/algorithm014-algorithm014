#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#


# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        stack = [0]
        water = 0
        for i in range(1, len(height)):
            if stack and height[i] > height[stack[0]]:
                temp = stack[0]
                while stack:
                    left = stack.pop()
                    water = water + height[temp] - height[left]
            stack.append(i)
        right = stack.pop()
        while stack:
            if height[stack[-1]] > height[right]:
                right = stack.pop()
            else:
                water = water + height[right] - height[stack.pop()]
        return water


# @lc code=end
