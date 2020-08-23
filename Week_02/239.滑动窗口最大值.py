#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:      
        #方法2：堆
        #最大值，想到用最大堆
        #但是python里面heapq是最小堆，求topk大
        #可以对nums的数前面取负，求最小值，在取负即最大值
        #时间复杂度 O(nlogk)
        #空间复杂度 O(n)   堆：O(k)  res：O(n-k+1)
        if k == 0 or len(nums) == 1:
            return nums
        res = []
        hp = [(-nums[i], i) for i in range(k)]
        heapq.heapify(hp)
        res.append(-hp[0][0])
        for i in range(k, len(nums)):
            while hp and hp[0][1] < i - k + 1:
                heapq.heappop(hp)
            heapq.heappush(hp, (-nums[i], i))
            res.append(-hp[0][0])
        return res    

        """
        
        #方法1：双端队列
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
        """


# @lc code=end
