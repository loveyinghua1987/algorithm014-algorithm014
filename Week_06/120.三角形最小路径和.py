#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#


# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        '''
        #方法2：动态规划+空间优化
        #时间复杂度：O(m^2)
        #空间复杂度：O(m)
        #写法1：
        m = len(triangle)
        dp = triangle[-1]

        for i in range(m - 2, -1, -1):
            prev = dp[i + 1]
            for j in range(i, -1, -1):
                cur = dp[j]
                dp[j] = min(dp[j], prev) + triangle[i][j]
                prev = cur
                
        return dp[0]
        '''
        #写法2：
        m = len(triangle)
        dp = triangle[-1]

        for i in range(m - 2, -1, -1):
            #for j in range(i + 1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]
        '''
        #方法1：动态规划
        #时间复杂度：O(m^2)
        #空间复杂度：O(m^2)
        #1：重复性（分治） sub(i,j) = min(sub(i+1，j), sub(i+1, j+1)) + a(i,j)
        #2：定义状态数组   dp[i][j]：从（i，j）结点到最底层结点的最小路径和
        #3：dp方程         dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + a[i][j]
        
        m = len(triangle)
        dp = [[0] * m for _ in range(m)]

        dp[-1] = triangle[-1]

        for i in range(m - 2, -1, -1):
            for j in range(i, -1, -1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
        '''


# @lc code=end
