#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #方法2：
        sgood = ''.join(c.lower() for c in s if c.isalnum())
        return sgood == sgood[::-1]
        '''
        #方法1：
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[j].isalnum():
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
        '''

# @lc code=end
