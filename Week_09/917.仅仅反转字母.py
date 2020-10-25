#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#


# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        #双指针
        '''
        #写法1
        s = list(S)
        i, j = 0, len(s) - 1
        while i < j:
            #if s[i] < 'A' or  'Z' < s[i] < 'a'  or s[i] > 'z':
            if not s[i].isalpha():
                i += 1
                continue
            #if s[j] < 'A' or  'Z' < s[j] < 'a'  or s[j] > 'z':
            if not s[j].isalpha():
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return ''.join(s)
        '''
        #写法2：
        s = list(S)
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalpha():
                i += 1
            while i < j and not s[j].isalpha():
                j -= 1
            if s[i].isalpha() and s[j].isalpha():
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return ''.join(s)


# @lc code=end
