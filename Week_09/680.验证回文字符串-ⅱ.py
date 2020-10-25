#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#


# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def isPalindrome(s):
        #     i, j = 0, len(s) - 1
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True
        isPalindrome = lambda x: x == x[::-1]

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return isPalindrome(s[i + 1:j + 1]) or isPalindrome(s[i:j])
            i += 1
            j -= 1
        return True


# @lc code=end
