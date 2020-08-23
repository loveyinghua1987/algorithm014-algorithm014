#剑指 Offer 40. 最小的k个数
from typing import List
import heapq
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        #方法1：排序
        #时间复杂度： O(nlogn)
        #空间复杂度： O(logn)  排序所需额外的空间复杂度
        arr.sort()
        return arr[:k]
        '''
        #方法2:堆
        #时间复杂度：O(nlogk)
        #空间复杂度：O(k)
        #找最小的k个数（Topk小）用最大堆
        #python自带的heapq是最小堆，此问题需要转化一下
        #可以先取负号，在利用heapq最小堆，找topk大，再取负，即Topk小
        res =[]
        #前k个元素取负后构建最小堆
        hp = [-x for x in arr[:k]]
        heapq.heapify(hp)
        #后面的元素依次取负入堆
        for i in range(k, len(arr)):
            #最小堆，求topk大
            #所以如果加入的-arr[i] 比堆顶元素hp[0]大的话，堆顶元素出堆，此元素入堆
            if -arr[i] > hp[0]:
                #heapq.heappop(hp)
                #heapq.heappush(hp, -arr[i])
                heapq.heapreplace(hp, -arr[i])
        res = [-x for x in hp]   #输出是无序的
        #要获取有序输出：
        #res = [-x for x in reversed([heapq.heappop(hp) for _ in range(len(hp))])]
        return res
        '''
if __name__ == "__main__":
    arr = [4,5,1,6,2,7,3,8]
    k = 4
    ans = Solution().getLeastNumbers(arr, k)
    print(ans)