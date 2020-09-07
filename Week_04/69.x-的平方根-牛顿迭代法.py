#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        #牛顿迭代法
        #f(x) = x**2 - C(C为输入x)
        #一阶泰勒展开式 f(x)= f(x0) + f'(x0)(x-x0)
        #                  = x0**2 - C + 2*x0*(x-x0)
        #                  = 2*x0*x - x0**2 - C
        #我们要求解f(x) = 0, 即 2*x0*x - x0**2 - C = 0
        #求得迭代公式： x = 1/2(x0 + C/x0)
        if x == 0:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = 1 / 2 * (x0 + C / x0)
            if abs(xi - x0) < 1e-7:
                break
            x0 = xi
        return int(xi)


# @lc code=end
