#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrace(left, right, path):
            if right == n:
                res.append(path)
                return
            if left < n:
                backtrace(left + 1, right, path + '(')
            if right < left:
                backtrace(left, right + 1, path + ')')

        res = []
        backtrace(0, 0, '')
        return res


# @lc code=end
