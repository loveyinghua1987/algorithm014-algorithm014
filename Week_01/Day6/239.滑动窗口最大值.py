#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#


# @lc code=start
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
# @lc code=end
