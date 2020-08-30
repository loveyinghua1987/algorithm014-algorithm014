#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        #方法2：回溯+剪枝
        def helper(n, k, start, track):
            if len(track) == k:
                res.append(track.copy())
                return
            for i in range(start, n - k + len(track) + 2):
                track.append(i)
                helper(n, k, i + 1, track)
                track.pop()

        res = []
        if k <= 0 or n <= 0:
            return res
        helper(n, k, 1, [])
        return res
        '''
        #方法1：回溯
        def helper(n, k, start, track):
            if len(track) == k:
                #res.append(track.copy())
                res.append(track[:])
                return
            for i in range(start, n + 1):
                track.append(i)
                helper(n, k, i + 1, track)
                track.pop()
                #helper(n, k, i+1, track+[i])

        res = []
        if k <= 0 or n <= 0:
            return res
        helper(n, k, 1, [])
        return res
        '''


# @lc code=end
