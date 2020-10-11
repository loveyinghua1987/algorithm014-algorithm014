#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #位运算
        if n < 1: return [[]]
        self.res = []
        self.DFS(n, [], 0, 0, 0, 0)
        return [['.' * col + 'Q' + '.' * (n - col - 1) for col in cols]
                for cols in self.res]

    def DFS(self, n, qeens, row, cols, pie, na):
        if row == n:
            self.res.append(qeens[:])
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)  #得到当前所有的空位
        while bits:
            p = bits & -bits  #获取最后一个1的位置
            col = bin(p - 1).count('1')
            qeens.append(col)
            bits &= bits - 1  #删除最后一个1，即表示p位置放入皇后
            self.DFS(n, qeens, row + 1, cols | p, (pie | p) << 1,
                     (na | p) >> 1)
            qeens.pop()


if __name__ == "__main__":
    s = Solution()
    print(s.solveNQueens(4))

# @lc code=end
