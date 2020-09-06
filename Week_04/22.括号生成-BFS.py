#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
import collections


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = [('', 0, 0)]
        while stack:
            s, l, r = stack.pop()
            if r == n:
                res.append(s)
            if r < l:
                stack.append((s + ')', l, r + 1))
            if l < n:
                stack.append((s + '(', l + 1, r))
        return res
        '''
        #BFS
        res = []
        stack = [('', 0, 0)]
        while stack:
            s, l, r = stack.pop()
            if l < r or l > n or r > n:
                continue
            if l == r == n:
                res.append(s)
            stack.append((s + '(', l + 1, r))
            stack.append((s + ')', l, r + 1))
        return res
        '''


# @lc code=end
