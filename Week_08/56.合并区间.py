#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#


# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 排序+一次扫描
        # 时间复杂度：O(nlogn) 排序的时间复杂度，快速排序
        # 空间复杂度：O(logn), 排序所需要的空间复杂度
        res = []
        #intervals.sort()
        intervals.sort(key=lambda x: x[0])
        for i in intervals:
            if res and i[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], i[1])
            else:
                res.append(i)
                #res += i,
        return res


# @lc code=end
