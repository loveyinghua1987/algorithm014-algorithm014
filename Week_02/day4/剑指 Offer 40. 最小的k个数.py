#剑指 Offer 40. 最小的k个数
from typing import List
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #堆，python里面heapq是最小堆，求topk大，需要将arr先进行处理，
        # 前面加负号，就把原问题从求topk小，变成了新问题求、取负后求topk大，再取负
        res =[]
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        for i in range(k, len(arr)):
            if -arr[i] > hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp, -arr[i])
        res = [-x for x in hp]
        return res

if __name__ == "__main__":
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    ans = Solution().getLeastNumbers(arr, k)
    print(ans)