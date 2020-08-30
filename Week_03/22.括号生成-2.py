#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#


# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def generate(left, right, n, s):
            if right == n:
                res.append(s)
                return
            if left < n:
                generate(left + 1, right, n, s + '(')
            if right < left:
                generate(left, right + 1, n, s + ')')

        generate(0, 0, n, '')
        return res


# @lc code=end
