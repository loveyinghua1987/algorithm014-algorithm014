#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank:
            return -1
        visited ={start}
        mutation = {'A', 'C', 'G', 'T'}
        def oneMutation(s):
            for i, val in enumerate(s):
                for t in mutation - {val}:
                    tmp = s[:i] + t + s[i+1:]
                    if tmp in bank:
                        yield tmp
        def dfs(s):
            if s == end:
                return 0
            res = float('inf')
            for nxt in oneMutation(s):
                if nxt not in visited:
                    visited.add(nxt)
                    res = min(res, dfs(nxt)+1)
                    visited.remove(nxt)
            return res
        res = dfs(start)
        return res if res != float('inf') else -1

        
# @lc code=end

