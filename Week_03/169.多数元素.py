#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        '''
        #方法1：hash
        #写法1
        counter = collections.Counter(nums)
        #for val, count in counter.items():
        #    if count > len(nums)//2:
        #         return val
        return max(counter.keys(), key=counter.get)
        
        #写法2
        dic = {}
        for num in nums:
                dic[num] = dic.get(num, 0) + 1
        for val, count in dic.items():
            if count > len(nums)//2:
                return val 
        
        #方法2：排序
        nums.sort()
        return nums[len(nums)//2]
        
        #方法3：随机化
        import random
        majority_count = len(nums)//2
        while True:
            candiate = random.choice(nums)
            if sum(1 for num in nums if num == candiate) > majority_count:
                return candiate
        
        #方法4：分治
        def helper(left, right):
            if left == right:
                return nums[left]
            mid = left+(right-left)//2
            l = helper(left, mid)
            r = helper(mid+1, right)
            l_cnt = sum(1 for i in range(left, right+1) if nums[i] == l)
            r_cnt = sum(1 for i in range(left, right+1) if nums[i] == r)
            return l if l_cnt > r_cnt else r
        return helper(0, len(nums)-1)
        '''
        #Boyer-Moore 投票算法
        count = 0
        candiate = None
        for num in nums:
            if count == 0:
                candiate = num
            count += 1 if num==candiate else -1
        return candiate



# @lc code=end

