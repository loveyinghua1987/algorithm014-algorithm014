#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        #1.递归 f(n)=f(n-1)+f(n-2) f(n):到达n阶的不同方法数
        #2.dp动态规划  迭代
        #3.优化dp  时间复杂度O(n),空间复杂度O(1)
        """
        #1.递归:时间复杂度:O(2**n)   超时 ,空间复杂度：O(n)
        #recursion terminator
        if n == 0 or n == 1:
            return 1
        #process logic in current layer
        #drill down

        return self.climbStairs(n-1)+self.climbStairs(n-2)

        #reverse the current level status if needed
        """
        """
        #2. dp动态规划:时间复杂度O(n),空间复杂度O(n)
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        """
        """
        #3.优化dp  时间复杂度O(n),空间复杂度O(1)
        cur, pre = 1, 1
        for i in range(2, n+1):#n-1次
            pre, cur = cur, (cur + pre)
        return cur
        """
        a, b = 1, 1
        for i in range(n):
            a, b = b, a + b
        return a

# @lc code=end
