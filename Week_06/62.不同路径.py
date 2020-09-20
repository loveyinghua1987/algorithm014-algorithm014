#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #动态规划（动态递推）
        #1. 重复性（分治） sub(i, j) = sub(i+1, j) + sub(i, j+1)
        #2. 定义状态转移   dp(i, j) i,j 到 Finish(m-1, n-1)的不同路径的总数
        #3. dp函数  dp[i][j] = dp[i+1][j] + dp[i][j+1]
        '''
        #方法1：记忆化搜索递归（自顶向下）
        #时间复杂度: O(m*n)
        #空间复杂度：O(m+n)  递归栈的深度
        memo = [[0] * n for _ in range(m)]

        def dp(i, j):
            if i == m - 1 or j == n - 1:
                return 1
            if memo[i][j] == 0:
                memo[i][j] = dp(i + 1, j) + dp(i, j + 1)
            return memo[i][j]

        return dp(0, 0)
        
        #方法2：动态规划（递推）（自底向上）
        #时间复杂度：O(m*n)
        #空间复杂度：O(m*n)
        dp = [[1] * n for _ in range(m)]
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]
        
        #方法2的另一种写法：
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
        
        #方法3：动态规划，优化空间
        #时间复杂度：O(m*n)
        #空间复杂度：O(n)
        dp = [1] * n
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[j] += dp[j + 1]
        return dp[0]
         '''
        #方法3的另一种写法：
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]
        '''
        #方法4：数学的方法
        # 从起点到终点，总共需要走 m + n + 2 步，
        # 在这么多步中，我们选择其中的m-1步向下走的组合数C(m+n-2,m-1)就是不同路径的总数
        if not m or not n:
            return 0
        import math
        return int(
            math.factorial(m + n - 2) /
            (math.factorial(m - 1) * math.factorial(n - 1)))
        '''


# @lc code=end
