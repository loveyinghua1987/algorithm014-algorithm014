#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
import string
import collections
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #方法1：计数
        #return all(s.count(c) == t.count(c) for c in string.ascii_lowercase)
        #return not any(s.count(c) != t.count(c) for c in string.ascii_lowercase)
        return collections.Counter(s) == collections.Counter(t)
        
        '''
        #方法2：快速排序
        return sorted(s) == sorted(t)
        
        #方法3：计数排序
        arr1, arr2 = [0]*26, [0]*26
        for c in s:
            arr1[ord(c) - ord('a')] += 1
        for c in t:
            arr2[ord(c) - ord('a')] += 1
        return arr1 == arr2

        '''

# @lc code=end

