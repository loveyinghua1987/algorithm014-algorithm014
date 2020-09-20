#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(mn)
        #空间复杂度：O(n)
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]
        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]
        '''
        #方法1：动态规划
        #时间复杂度：O(mn)
        #空间复杂度：O(mn)
        #1. 重复性（分治） sub(i, j) = min(sub(i-1,j), sub(i, j-1)) + grid[i][j]
        #2. 定义状态数组   dp[i][j] : 左上角到第i行j列的元素路径总和的最小值
        #3. dp函数   dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]
        '''


# @lc code=end
