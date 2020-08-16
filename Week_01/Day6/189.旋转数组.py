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
        #方法2：循环替换  时间复杂度O(n) 空间复杂度O(1)
        #把元素看做同学，把下标看做座位，大家换座位。
        #第一个同学离开座位去第k+1个座位，第k+1个座位的同学被挤出去了，他就去坐他后k个座位，如此反复。
        # 但是会出现一种情况，就是其中一个同学被挤开之后，坐到了第一个同学的位置（空位置，没人被挤出来），
        # 但是此时还有人没有调换位置，这样就顺着让第二个同学换位置。 那么什么时候就可以保证每个同学都换完了呢？
        # n个同学，换n次，所以用一个count来计数即可。
        if len(nums)*k ==0:
            return
        n = len(nums) 
        k %= n
        start = 0    #开始移动的位置点
        prev = start   #要prev记录每轮移动开始的位置，初始值为start
        count =0 #计算移动的次数
        while count < n:
            current = start
            prev = nums[start]
            while True and count <n:
                next = (current+k)%n
                #前面的值赋值给后面第k个位置的值，一次循环下去
                temp = nums[next]
                nums[next] = prev
                prev = temp  #prev保存上一个位置的值
                #print("prev = %d, nums[next]=%d, nums = %s \n "%(prev,nums[next],nums))
                current = next
                count +=1
                if start == current:
                    break
            start +=1
 
        '''
        #方法1：时间复杂度：O(n) 空间复杂度：O(1)
        def swap(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        if len(nums) * k == 0:  #len(nums) or k equal 0
            return
        k = k % len(nums)   #k有可能大于nums的长度，需要预先处理下

        nums.reverse()
        swap(nums, 0, k - 1)
        swap(nums, k , len(nums) - 1)
        return nums
        '''

# @lc code=end
