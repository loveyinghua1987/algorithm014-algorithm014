#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#


# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        #当n>=4时， sqrt(n) <= n/2
        #当n为2,3时，不为完全平方数，所以下面right从num//2开始
        if num < 2:
            return True
        left, right = 0, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:  # mid*mid > num
                right = mid - 1
        return False


# @lc code=end
