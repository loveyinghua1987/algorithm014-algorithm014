#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # cols[i]记录第i行放置皇后的列下标
        # xy_diff记录行下标与列下标的差值，与(x,y)差值相等的元素在(x, y)的左对角线上
        # xy_sum记录行下标与列下标的和，与(x,y)和相等的元素在(x, y)的右对角线上
        def backtrace(cols, xy_diff, xy_sum):
            row = len(cols)
            if row == n:
                res.append(cols)
                return
            for col in range(n):
                # 下面分别判断 在垂直线上，左对角线上， 右对角线上是否有皇后Q
                # 如果都没有的话，则放置皇后Q, 再继续递归下去，不满足条件时，回溯重新做选择
                if col not in cols and row - col not in xy_diff and row + col not in xy_sum:
                    backtrace(cols + [col], xy_diff + [row - col],
                              xy_sum + [row + col])

        res = []
        backtrace([], [], [])
        # 转换为要求的格式输出
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in cols]
                for cols in res]


# @lc code=end
