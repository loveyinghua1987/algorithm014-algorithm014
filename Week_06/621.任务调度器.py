#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#

# @lc code=start
import collections


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #时间复杂度：O(m)  m:为任务的总数
        #空间复杂度：O(1)
        length = len(tasks)
        if length <= 1:
            return length

        counter = collections.Counter(tasks)
        task_sorted = sorted(counter.items(),
                             key=lambda x: x[1],
                             reverse=True)
        max_cnt = task_sorted[0][1]
        res = (max_cnt - 1) * (n + 1)
        for task in task_sorted:
            if task[1] == max_cnt:
                res += 1
        return res if res >= length else length


# @lc code=end
