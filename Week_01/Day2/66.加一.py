#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#


# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #加1进位会遍历到不等于9的数停止 或者 整个数组遍历完（所有数都为9）
        # 第一种情况：不全为9，从最后一位开始加1计算除以10的余数，并更新digits
        # 如果余数为0则需要继续循环、判断，遇到余数不为零，则返回digits
        # 第二种情况：全为9，上面整个遍历完后，还需在数组前添加[1]，之前digits的所有数都为0
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits


# @lc code=end
