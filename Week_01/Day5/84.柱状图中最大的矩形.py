#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #利用栈
        max_area = 0
        stack = []
        for k in range(len(heights)):
            while stack and heights[k] < heights[stack[-1]]:
                ind = stack.pop()
                l = stack[-1] if stack else -1
                r = k
                max_area = max(max_area, heights[ind] * (r - l - 1))
            stack.append(k)
            
        while stack:
            ind = stack.pop()
            l = stack[-1] if stack else -1
            r = len(heights)
            max_area = max(max_area, heights[ind] * (r - l - 1))
        return max_area


# @lc code=end
