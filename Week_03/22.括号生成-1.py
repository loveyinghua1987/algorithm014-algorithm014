#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def generate(self, left: int, right: int, n: int, s: str):
        if right == n:
            self.res.append(s)
            return
        if left < n:
            self.generate(left + 1, right, n, s + '(')
        if right < left:
            self.generate(left, right + 1, n, s + ')')

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generate(0, 0, n, '')
        return self.res
        #return len(self.res)  
        #generateParenthesis(n) 中有多少个元素，其实是第n个卡特兰数
        #[1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862]


if __name__ == "__main__":
    solution = Solution()
    for i in range(5):
        print(solution.generateParenthesis(i))
# @lc code=end
