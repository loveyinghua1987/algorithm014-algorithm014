#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #矩阵快速幂
        def multiply(a, b):  #矩阵乘法
            return [[
                a[0][0] * b[0][0] + a[0][1] * b[1][0],
                a[0][0] * b[0][1] + a[0][1] * b[1][1]
            ],
                    [
                        a[1][0] * b[0][0] + a[1][1] * b[1][0],
                        a[1][0] * b[0][1] + a[1][1] * b[1][1]
                    ]]

        def pow(a, n):
            if n == 0:
                return [[1, 0], [0, 1]]
            res = [[1, 0], [0, 1]]

            while n:
                if n % 2:
                    res = multiply(res, a)
                a = multiply(a, a)
                n >>= 1
            return res

            #p = pow(multiply(a, a), n // 2)
            #return multiply(p, a) if n % 2 else p

        x = [[1, 1], [1, 0]]
        return sum(pow(x, n)[1])

        # @lc code=end
