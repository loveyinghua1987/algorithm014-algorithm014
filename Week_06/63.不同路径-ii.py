#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #方法2：动态规划+空间优化
        #时间复杂度：O(m*n)
        #空间复杂度：O(n)
        m = len(obstacleGrid)
        if not m: return 0
        n = len(obstacleGrid[0])
        if not n: return 1

        dp = [0] * n
        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            dp[j] = 1

        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                dp[0] = 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                else:
                    dp[j] += dp[j - 1]

        return dp[-1]
        '''
        #方法1：动态规划
        #时间复杂度：O(m*n)
        #空间复杂度：O(m*n)
        m = len(obstacleGrid)
        if not m: return 0
        n = len(obstacleGrid[0])
        if not n: return 1

        dp = [[0] * n for _ in range(m)]

        #dp数组初始值
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
        '''

        # @lc code=end
