#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#


# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1]) if len(s.split()) != 0 else 0


# @lc code=end
