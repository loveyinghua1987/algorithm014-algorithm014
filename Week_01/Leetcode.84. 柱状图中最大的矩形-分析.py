#84. Largest Rectangle in Histogram柱状图中最大的矩形
#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
 
#方法2：递归解法
#思想：固定高度heights[ind]，寻找每个高度对应的最大宽度(r-l-1)，分别计算area，比较取最大值 
#	   l: ind左边第一个比heights[ind]小的高度的下标
#	   r：ind右边第一个比heights[ind]小的高度的下标	

#难点：如何确定每个高度的左右边界下标？
#      利用栈解决，heights中的元素依次入栈，如果比栈顶元素大，入栈；
#	   如果比栈顶元素小，弹出栈顶元素计算它的最大宽度，计算area，跟最大值比较取最大。
#      这里有个问题，如果遇到栈为空的情况，怎么处理? 
#	   栈为空，说明它前面没有元素了，到头了，左边界应该在它前面一个位置，
#	   我们可以假想作左边有个元素小于它,为了统一计算最大宽度的方式，可以将下标index设置为-1
#      同理，最后stack可能不为空，这个时候以同样类似的方式处理右边界，设右边界index设置为len(heights)

	
#时间复杂度：O(n)  n=len(heights)   处理heights中的元素入栈、出栈各一次
#空间复杂度：O(n)  

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



