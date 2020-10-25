#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        #return ' '.join([''.join(reversed(c)) for c in s.split()])
        return " ".join(c[::-1] for c in s.split())
 
# @lc code=end

