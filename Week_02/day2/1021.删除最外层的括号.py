#
# @lc app=leetcode.cn id=1021 lang=python3
#
# [1021] 删除最外层的括号
#


# @lc code=start
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        #方法3： 栈，本质与左、括号计数相同，且还多用了空间
        res, start, stack = [], 0, []
        for i in range(len(S)):
            if S[i] == '(':
                stack.append(i)
            else:
                stack.pop()
            if not stack:
                res.append(S[start + 1:i])
                start = i + 1
        return ''.join(res)
        """
        #方法2：通过当前开着的括号数opened，来判断左、右括号是不是需要保留或是删除的
        #时间复杂度:O(n)
        #空间复杂度：O(n)
        res, opened = [], 0
        for c in S:
            if c == "(" and opened > 0: res.append(c)
            if c == ")" and opened > 1: res.append(c)
            opened += 1 if c == "(" else -1
        return ''.join(res)
        
        #方法1：通过左、右括号的计数来确定需要删除的括号位置
        res, start, cnt = [], 0, 0
        for i in range(len(S)):
            if S[i] == "(": cnt += 1
            if S[i] == ")": cnt -= 1
            if cnt == 0:
                res.append(S[start + 1:i])
                start = i + 1
        return ''.join(res)
        """


# @lc code=end
