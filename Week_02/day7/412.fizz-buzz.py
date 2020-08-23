#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        dic = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1, n+1):
            s = ''
            for key in dic:
                if i%key == 0:
                    s += dic[key]
            if s:
                res.append(s)
            else:
                res.append(str(i))
        return res
        
# @lc code=end

