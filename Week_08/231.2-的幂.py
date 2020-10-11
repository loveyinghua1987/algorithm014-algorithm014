#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:       
        #位运算
        #时间复杂度：O(1)
        #空间复杂度：O(1)
        #写法1：去除二进制中最右边的 1 （推荐）
        return n != 0 and n & n - 1 == 0
        '''
        #写法2：获取二进制中最右边的 1
        return n != 0 and n & -n == n
        '''

# @lc code=end
