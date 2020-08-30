#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#


# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #方法2:迭代
        #时间复杂度：O(logn)
        #空间复杂度: O(1)
        if not n:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        res = 1
        while n:
            if n & 1:  #等价于n%2
                res *= x
            n >>= 1  #等价于n//2
            x *= x
        return res
        '''
        #方法1:递归
        #时间复杂度：O(logn)
        #空间复杂度：O(logn)
        if not n:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        p = self.myPow(x * x, n // 2)
        return x * p if n % 2 else p
        '''


# @lc code=end
