#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
import collections


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        #方法1：
        #时间复杂度：O(n1logn1 + n2)
        #空间复杂度：O(n2)
        b = {v: k for k, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: b.get(x, 1000 + x))
        '''
        #方法2：
        #时间复杂度：O(n1(n1+n2)logn1)
        #空间复杂度：O(n1+n2) 
        return sorted(arr1, key=(arr2 + sorted(arr1)).index)
        
        #方法3：
        #时间复杂度：O(max(n2, N))
        #空间复杂度：O(n1)
        res, cnt = [], collections.Counter(arr1)
        for i in arr2:
            if cnt[i]:
                res.extend([i] * cnt.pop(i))
        # for i in range(1001):
        #     if cnt[i]:
        #         res.extend([i] * cnt.pop(i))
        res.extend(sorted(cnt.elements()))
        return res
        '''


# @lc code=end
