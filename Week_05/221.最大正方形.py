#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#


# @lc code=start
from typing import List
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #方法2：动态规划 + 空间优化
        #时间复杂度：O(mn)
        #空间复杂度：O(n)
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n
        prepre = 0
        for i in range(m):
            for j in range(n):
                temp = dp[j]
                #if matrix[i][j] == '1':
                #    if i== 0 or j == 0:
                #        dp[j] = 1
                #    else:    
                #        dp[j] = min(dp[j], dp[j-1], prepre ) + 1
                #else:  # matrix[i][j] == '0'
                #    dp[j] = 0
                if i == 0 or j == 0 or matrix[i][j] == '0':
                    dp[j] = int(matrix[i][j])
                else:
                    dp[j] = min(dp[j], dp[j-1], prepre) + 1
                
                res = max(res, dp[j])
                prepre = temp
            #print(i, dp)
        return res * res
        '''
        #方法1：动态规划
        #时间复杂度：O(mn)
        #空间复杂度：O(mn)
        #1. 重复性(分治)  sub(i, j) = min(sub(i-1, j), sub(i, j-1), sub(i-1, j-1) + 1
        #2. 定义状态数组  dp[i][j] : 以(i, j)为右下角的最大正方形的边长 (matrix[i][j] == '0'时最大边长为零)
        #                dp[i][j]的max就为问题所求的最大正方形的边长，平方即是面积
        #3. dp方程   dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1]) + 1
                    res = max(res, dp[i][j])
        return res * res
        '''
if __name__ == "__main__":
    solution = Solution()
    print(solution.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
# @lc code=end