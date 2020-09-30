#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #写法2：
        if n < 1: return []
        self.res = []
        self.cols, self.pie, self.na = set(), set(), set()
        self.dfs(n, 0, [])
        return self._generate_result(n)

    def dfs(self, n, row, cur_state):
        #recursion terminator
        if row >= n:
            self.res.append(cur_state)
            return
        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)
            self.dfs(n, row + 1, cur_state + [col])
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def _generate_result(self, n):
        return [['.' * c + 'Q' + '.' * (n - c - 1) for c in cols]
                for cols in self.res]
        '''
        #写法1
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
        '''


# @lc code=end
