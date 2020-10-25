#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#


# @lc code=start
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        #枚举中心，向两边拓展
        #时间复杂度：O(n^2)
        #空间复杂度：O(1)
        
        self.maxlen, self.lo = 0, 0
        if len(s) < 2: return s
        for i in range(len(s)):
            self.extendPalindrome(s, i, i)  #odd length
            self.extendPalindrome(s, i, i + 1)  #even length
        return s[self.lo:self.lo + self.maxlen]

    def extendPalindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        if self.maxlen < j - i - 1:
            self.lo = i + 1
            self.maxlen = j - i - 1
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:    
        res = ""
        for i in range(len(s)):
            res = max(self.helper(s,i,i), self.helper(s,i,i+1), res, key=len)
        return res
           
    def helper(self,s,l,r):     
        while 0<=l and r < len(s) and s[l]==s[r]:
                l-=1; r+=1
        return s[l+1:r]


# @lc code=end
