#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#


# @lc code=start
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        #哈希集合
        #时间复杂度：O(m+n)  m：len(J)  n: len(S)
        #空间复杂度：O(m)
        J_set = set(J)
        return sum(c in J_set for c in S)


# @lc code=end
