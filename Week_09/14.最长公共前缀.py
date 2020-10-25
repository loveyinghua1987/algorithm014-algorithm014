#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #纵向扫描
        #时间复杂度：O(mn)，m:字符串数组中的字符串的平均长度，n :字符串的数量
        #空间负责度：O(1)
        if not strs: return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if len(strs[j]) == i or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]


# @lc code=end
