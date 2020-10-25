#
# @lc app=leetcode.cn id=151 lang=python3
#
# [151] 翻转字符串里的单词
#


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:       
        #方法1：分割+倒序
        return ' '.join(reversed(s.split()))
        '''
        #方法2：双指针(先翻转整个数组,再翻转单个单词,清除多余空格)
        s, n = list(s), len(s)

        #翻转数组
        def reverse(s, i, j):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        #翻转单个单词
        def word_reverse(s):
            #用双指针找到第一个单词
            i, j = 0, 0
            while i < n:
                #找到第一个单词首字母位置
                while i < n and s[i] == ' ':
                    i += 1
                j = i
                #找到第一个第一个单词末尾字母位置
                while j < n and s[j] != ' ':
                    j += 1
                #单词从i开始，到j-1
                reverse(s, i, j - 1)
                i = j

        #清除多余空格
        def clear_space(s):
            i, j = 0, 0
            while j < n:
                # 找到一个单词
                while j < n and s[j] == ' ':
                    j += 1
                # 单词朝前移    
                while j < n and s[j] != ' ':
                    s[i] = s[j]
                    i += 1
                    j += 1
                # 移动到下一个单词
                while j < n and s[j] == ' ':
                    j += 1
                if j < n:
                    s[i] = ' '
                    i += 1
            return ''.join(s[:i])

        reverse(s, 0, n - 1)
        word_reverse(s)
        return clear_space(s)
        '''

# @lc code=end
