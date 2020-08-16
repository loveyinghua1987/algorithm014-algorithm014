#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#


# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #栈
        max_area = 0
        stack = []
        for k in range(len(heights)):
            if not stack:
                stack.append(k)
            else:
                if heights[k] > heights[stack[-1]]:  # k位置的左边界找到，接着k入栈
                    stack.append(k)
                else:  #heights[k] <= stack[-1]
                    #stack[-1]找到左（stack[-2]）右(k)边界，pop出来计算
                    while stack and heights[k] < heights[stack[-1]]:
                        ind = stack.pop()
                        l = stack[-1] if stack else -1
                        r = k
                        max_area = max(max_area, heights[ind] * (r - l - 1))
                        #print(ind, l, r, max_area)
                    stack.append(k)

        #stack可能最终还有剩，他们的右边界都为len(heights),前面一个数是左边界
        while stack:
            ind = stack.pop()
            if stack:
                l = stack[-1]
            else:
                l = -1
            r = len(heights)
            max_area = max(max_area, heights[ind] * (r - l - 1))
            #print(ind, l, r, max_area, heights[ind], r-l-1)
        return max_area
        '''
        #双指针  超时
        max_area =0
        for k in range(len(heights)):
            l = r = k
            while l >=0 and heights[l] >= heights[k]:
                l -= 1
            while r < len(heights) and heights[r] >= heights[k]:
                r += 1

            max_area = max(max_area, heights[k]*(r-l-1))
        return max_area

        
        #暴力穷举 超时
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                max_area = max(max_area, min(heights[i:j+1])*(j-i+1))
        return max_area   
        '''


# @lc code=end
