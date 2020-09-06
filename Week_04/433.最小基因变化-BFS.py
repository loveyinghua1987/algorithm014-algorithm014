#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
import collections


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        bank = set(bank)
        if end not in bank:
            return -1
        visited = {start}
        mutation = {'A', 'C', 'G', 'T'}

        def oneMutation(s):
            for i, val in enumerate(s):
                for t in mutation - {val}:
                    temp = s[:i] + t + s[i + 1:]
                    if temp in bank:
                        yield temp

        #BFS
        q = collections.deque()
        q.append((start, 0))
        while q:
            s, res = q.popleft()
            if s == end:
                return res
            for nxt in oneMutation(s):
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, res + 1))
        return -1


# @lc code=end
