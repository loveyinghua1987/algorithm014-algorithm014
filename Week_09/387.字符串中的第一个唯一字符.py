#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = dict(collections.Counter(s))
        for i, val in enumerate(s):
            if d[val] == 1:
                return i
        return -1


# @lc code=end
