#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#


# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #(dx, dy):方向 北-东-南-西
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0  #di表示dx和dy的下标, 当di=0时，(dx[di], dy[di]) = (0, 1) :初始的方向
        res = 0
        obstacles = set(map(tuple, obstacles))
        for cmd in commands:
            if cmd == -2:  #向左
                di = (di + 3) % 4
            elif cmd == -1:  #向右
                di = (di + 1) % 4
            else:  # 1 <= x <= 9
                for _ in range(cmd):
                    if (x + dx[di], y + dy[di]) not in obstacles:
                        x += dx[di]
                        y += dy[di]
                        res = max(res, x * x + y * y)
        return res


# @lc code=end
