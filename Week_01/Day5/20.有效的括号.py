#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        #栈
        #方法3：
        if len(s) % 2 != 0: #奇数
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''

        """
        #方法2：
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in d.values():
                stack.append(c)
            elif c in d.keys():
                if not stack or d[c] != stack.pop():
                    return False
        return stack == []
        
        #方法1：
        stack = []
        for c in s:
            if c is '(':
                stack.append(')')
            elif c is '[':
                stack.append(']')
            elif c is '{':
                stack.append('}')
            elif not stack or c != stack.pop():
                return False
        return stack == []
        """


# @lc code=end
