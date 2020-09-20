#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        #方法2： 动态规划 + 空间优化
        #时间复杂度： O(n)
        #空间复杂度： O(1)
        n = len(s)
        if not n: return 0
        pre, cur = 1, 1 * (s[0] > '0')
        for i in range(1, n):
            cur, pre = cur * (s[i] > '0') + pre * ('10' <= s[i - 1:i + 1] <='26'), cur
        return cur

        #方法1：动态规划
        #时间复杂度： O(n)
        #空间复杂度： O(n)
        #1. 重复性（分治）：
        #   sub(s) = sub(s[:n-1]) if s[n-1] > '0' else 0 + sub(s[:n-2]) if '10' <= s[n-1: n] <= '26' else 0
        #2. 定义动态数组：
        #   dp[i] : 前i个字符的解码总数
        #3. dp方程
        '''
        n = len(s)
        if not n: return 0
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1 * (s[0] > '0')
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] * (s[i - 1] > '0') + dp[i - 2] * (
                '10' <= s[i - 2:i] <= '26')
        return dp[-1]
        '''

# @lc code=end
