#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # 方法1. dp
        # "(" + 【i=p时所有括号的排列组合】 + ")" + 【i=q时所有括号的排列组合】
        # p + q = n-1
        # dp[i] = ["(" + k1 + ")" + k2 for j in range(i) for k1 in dp[j] for k2 in dp[i-1 - j]]
        if not n: return []
        dp = [[""]] * (n + 1)
        dp[1] = ["()"]
        for i in range(2, n + 1):
            dp[i] = [
                "(" + k1 + ")" + k2 for j in range(i) for k1 in dp[j]
                for k2 in dp[i - 1 - j]
            ]
            print(dp[i])
        return dp[-1]
        '''
        #方法2：
        dp = set(["()"])
        for i in range(1, n):
            dp = set(per[:j] + "()" + per[j:] for per in dp
                     for j in range(2 * i))
        return list(dp)
        '''

# @lc code=end
