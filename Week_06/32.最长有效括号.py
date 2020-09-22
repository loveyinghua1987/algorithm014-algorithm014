#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#


# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #方法3：计数器
        #时间复杂度： O(n)
        #空间复杂度： O(1)
        res = 0
        left = right = 0
        for i in range(len(s)):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0
        return res
        '''
        #方法2：栈
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」
        #需要注意的是，如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，
        #这样就不满足提及的「最后一个没有被匹配的右括号的下标」，
        #为了保持统一，我们在一开始的时候往栈中放入一个值为 −1 的元素
        stack = [-1]
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1]) 
        return res   

        
        #方法1：动态规划
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        #1. 重复性：
        #   有效括号的子串一定以')'结束，
        #   随着字符串长度的增大， 有效括号的子串的最大长度一定是增大或不变的
        #   我们计算以s每个字符结尾的有效子串的长度(重复性)，再取最大，即为所求
        #2. 定义状态数组：
        #   dp[i]:下标 i 字符结尾的最长有效括号的长度
        #   i下标对应的字符为'('的话，dp[i] = 0
        #   所以只需考虑i为')'的情况
        #   如果s[i-1]为'(':  dp[i] = dp[i-2] + 2
        #   如果s[i-1]为'):  s[i- dp[i]-1]有两种情况，为('(如下) 或')'(为零)
        #       dp[i] = dp[i-1] + dp[i - dp[i-1]-2] + 2
        #3. dp方程:
        #    if s[i] == ')'
        #         dp[i] = dp[i-2] + 2  if s[i-1] == '('
        #    elif i- dp[i-1] > 0 and s[i - dp[i-1]-1] == '(':
        #         dp[i] = dp[i-1] + dp[i - dp[i-1]-2] + 2
        n = len(s)
        if n <= 1: return 0
        dp = [0] * n
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
        for i in range(2, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp)
        '''


# @lc code=end
