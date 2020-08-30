#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        import numpy as np

        def pow(a, n):
            if n == 0:
                return np.array([[1, 0], [0, 1]])
            p = pow(np.dot(a, a), n // 2)
            return np.dot(p, a) if n % 2 else p

        a = np.array([[1, 1], [1, 0]])
        return int(np.sum(pow(a, n), axis=1)[1])


# @lc code=end
