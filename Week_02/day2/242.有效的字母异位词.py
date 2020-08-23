#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #mehthod 7
        return collections.Counter(s) == collections.Counter(t)

        """
        #method 6
        if len(s) != len(t):
            return False
        dict = [0]*26
        for c in s:
            dict[ord(c) - ord('a')] += 1
        for c in t:
            dict[ord(c) - ord('a')] -= 1
            if dict[ord(c) - ord('a')] < 0:
                return False
        return True
        
        #method 5:
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
        for c in t:
            count[c] -= 1
            if count[c] < 0:
                return False
        return True

        
        #method 4：
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])
        
        #method 3: 用数组构造hashtable，字母‘a~z’对应的ASCII码作为key，再比较
        arr1, arr2 = [0]*26, [0]*26
        for c in s:
            arr1[ord(c) - ord('a')] += 1
        for c in t:
            arr2[ord(c) - ord('a')] += 1
        return arr1 == arr2
        
        #method 2: map计数后再比较
        dict1, dict2 = {}, {}
        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        for c in t:
            dict2[c] = dict2.get(c, 0) + 1
        return dict1 == dict2
        
        #method 1：排序后再比较
        return sorted(s) == sorted(t)
        """


# @lc code=end
