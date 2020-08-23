#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#


# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #循环替换
        n = len(nums)
        if n < 2: return  #长度小于2的旋转多少都还是自己
        k = k % n  #k有可能比n大，求模处理后，保证k<n
        if k ==0: return  #不用移动
        count = 0  #count用于计算移动的次数，总共移动的次数不超过n
        start = 0  #start记录每次循环替换开始的位置下标
        while count < n:
            curr = start  #curr记录的是下标
            prev = nums[start]  #prev记录的是值
            while True:
                nex = (curr + k) % n
                temp = nums[nex]
                nums[nex] = prev
                prev = temp
                count += 1
                if nex == start:
                    break
                curr = nex
            start += 1


# @lc code=end
