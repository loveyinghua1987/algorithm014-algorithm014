#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#


# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        方法1：利用bin函数和zfill函数
        return int(bin(n)[2:].zfill(32)[::-1], 2)
        '''
        #方法2：位运算
        #关键思想:对于位于索引 i 处的位，在反转之后，
        #        其位置应为 31-i（注：索引从零开始）
        #写法1：
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res
        '''
        #写法2：
        #从最低位到最高位逐位检查n的第i位是不是为1. 
        #如果是, 就把（31-i）位设为1
        res, mark = 0, 1
        for i in range(32):
            if n & mark:
                res |= 1 << (31 - i)
            mark <<= 1
        return res
        '''

# @lc code=end
