#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #桶排序
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        counter = collections.Counter(nums)
        for num, count in counter.items():
            bucket[count].append(num)
        for i in range(len(nums), -1, -1):
            if len(res) > k:
                break
            res.extend(bucket[i])
        return res[:k]
        '''
        #最小堆
        res = []
        counter = collections.Counter(nums)
        hp = []
        for num, count in counter.items():
            heapq.heappush(hp, (count, num))
            if len(hp) > k:
                heapq.heappop(hp)
        #res = [hp[i][1] for i in range(len(hp))]   #无序
        #频率由高到低排列
        res = [
            x[1] for x in reversed([heapq.heappop(hp) for _ in range(len(hp))])
        ]
        return res
        '''

    # @lc code=end
