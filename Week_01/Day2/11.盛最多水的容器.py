#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#


# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        #暴力解法  超时！！！时间复杂度O(n)
        max_area = 0
        for i in range(len(height)-1):
            for j in range(i+1, len(height)):
                max_area = max(max_area, min(height[i],height[j])*(j-i))
        return max_area
        """
        #左右夹逼法  时间复杂度O(n)
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j-i)*min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
        
# @lc code=end
