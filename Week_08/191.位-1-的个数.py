#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:     
        #方法1：位运算
        #写法1：推荐
        cnt = 0
        while n != 0:
            cnt += 1
            n &= n - 1
        return cnt
        '''    
        #写法2：
        cnt = 0
        while n != 0:
            cnt += n & 1  # 等价于cnt += n % 2
            n >>= 1  #等价于 n = n // 2
        return cnt
        
        #方法2：利用bin函数
        return bin(n).count('1')
        
        #方法3：递归
        if n == 0:
            return 0
        return self.hammingWeight(n & (n - 1)) + 1
        '''

# @lc code=end
