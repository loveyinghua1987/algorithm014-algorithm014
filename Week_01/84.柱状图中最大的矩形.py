#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #方法2：
        n = len(heights)
        stack = []
        left = [0] * n
        right = [n] * n
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                right[stack[-1]] = i
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        #max_area = max((right[i] - left[i] - 1) * heights[i]
        #               for i in range(n)) if n > 0 else 0
        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right[i] - left[i] - 1) * heights[i])
        return max_area
        '''
        #利用栈 方法1
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
        '''


# @lc code=end
