#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#


# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:    
        #方法2：基于位运算的回溯 (终极解法)
        self.cnt = 0
        self.backtrace(n, 0, 0, 0, 0)
        return self.cnt

    def backtrace(self, n, row, cols, pie, na):
        while row == n:
            self.cnt += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits  #获取最后一个1的位置
            bits &= bits - 1  #删除最后一个1，即表示p位置放皇后
            self.backtrace(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
    '''
        #方法1：基于列表的回溯
        self.cnt = 0
        self.backtrace(n, [], [], [])
        return self.cnt

    def backtrace(self, n, cols, xy_sum, xy_diff):
        row = len(cols)
        if row == n:
            self.cnt += 1
            return
        for col in range(n):
            if col in cols or row + col in xy_sum or row - col in xy_diff:
                continue
            self.backtrace(n, cols + [col], xy_sum + [row + col],
                           xy_diff + [row - col])
    '''

# @lc code=end
