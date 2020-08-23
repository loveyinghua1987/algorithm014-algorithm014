#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#


# @lc code=start
import heapq
class Ugly:
    def __init__(self):
        #方法1：
        #self.nums = sorted(2**i2*3**i3*5**i5 for i2 in range(32) for i3 in range(20) for i5 in range(14))
        '''
        #方法2：
        self.nums = nums = [1]
        i2 = i3 = i5 = 0
        for _ in range(1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)
            if ugly == nums[i2] * 2:
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
        '''
        #方法3：堆
        self.nums = nums = []
        seen = {1}
        hp = [1]
        heapq.heapify(hp)
        for _ in range(1690):
            ugly = heapq.heappop(hp)
            nums.append(ugly)
            for i in [2, 3, 5]:
                new_ugly = ugly*i
                if new_ugly not in seen:
                    heapq.heappush(hp, new_ugly)
                    seen.add(new_ugly)
            
class Solution:
    u = Ugly()

    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n - 1]


# @lc code=end
