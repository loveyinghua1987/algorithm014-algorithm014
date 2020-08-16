#Leetcode239. Sliding Window Maximum滑动窗口最大值
#https://leetcode-cn.com/problems/sliding-window-maximum/


#思想：
#     想办法实现：当append和pop元素，始终保持window的首个元素是最大的，且里面的元素是降序排列的
#     添加元素的时候，从window的后面依次往前跟添加元素比较，如果比添加元素小，就pop出来，直到遇到比它大的停止
#     同时如果window遍历的元素个数大于k的时候开始，需要pop最前面的元素
#     从i=k-1开始记录结果，可以节省空间，前面不需要的可以不用记录输出

#时间复杂度： O(n)  每个元素被处理两次- 其索引被添加到双向队列中和被双向队列删除。
#空间复杂度： O(n)  输出数组使用了 O(N−k+1) 空间，双向队列使用了 O(k)


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = collections.deque()
        res = []
        for i, num in enumerate(nums):
            #加入每个元素之前，把它前面比它小的都pop出来
            while window and nums[window[-1]] < num:
                window.pop()
            window.append(i)
            #上面处理后，window第一个元素一定记录的是最大值的下标
            #当窗口长度超过k的时候，需要pop window第一个元素
            #因为window记录的是nums的下标值，所以可以通过window第一个元素的值（nums的下标）和当前位置i比较判断
            if window[0] == i - k:
                window.popleft()
            #res结果只需要i从k-1k开始记录
            if i >= k-1:
                res.append(nums[window[0]])
        return res
