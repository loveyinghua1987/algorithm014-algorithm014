#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#


# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        #双向BFS
        if not bank or end not in bank: return -1

        bank = set(bank)
        front, rear = {start}, {end}
        mutation = {'A', 'C', 'G', 'T'}
        gen_len = 8
        cnt = 0
        while front:
            cnt += 1
            nxt_front = set()
            for s in front:
                for i in range(gen_len):
                    for c in mutation - {s[i]}:
                        nxt = s[:i] + c + s[i + 1:]
                        if nxt in rear:
                            return cnt
                        if nxt in bank:
                            nxt_front.add(nxt)
                            bank.remove(nxt)
            front = nxt_front
            if len(front) < len(rear):
                front, rear = rear, front
        return -1


# @lc code=end
