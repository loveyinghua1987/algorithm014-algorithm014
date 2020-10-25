#
# @lc app=leetcode.cn id=709 lang=python3
#
# [709] 转换成小写字母
#


# @lc code=start
class Solution:
    def toLowerCase(self, str: str) -> str:
        #写法3：
        return str.lower()
        '''
        #写法2：
        s = []
        for c in str:
            s.append(chr(ord(c) | 32) if 'A' <= c <= 'Z' else c)
        return ''.join(s)
        
        #写法1
        s = ''
        for c in str:
            s += chr(ord(c) + 32) if 'A' <= c <= 'Z' else c
        return s
        '''


# @lc code=end
