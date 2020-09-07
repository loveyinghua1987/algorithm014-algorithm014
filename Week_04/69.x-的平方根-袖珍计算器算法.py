#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
import math as m


class Solution:
    def mySqrt(self, x: int) -> int:
        #袖珍计算器
        if x == 0:
            return 0
        res = int(m.exp(0.5 * m.log(x)))
        return res + 1 if (res + 1)**2 <= x else res


# @lc code=end
