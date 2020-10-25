#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        #方法1：排序后的字符串作为dict的key，原字符串为value
        d = collections.defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
            #d[''.join(sorted(s))].append(s)
        return list(d.values())
        '''
        #方法2：计数作为key
        d = collections.defaultdict(list)
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(s)
        return list(d.values())


# @lc code=end
