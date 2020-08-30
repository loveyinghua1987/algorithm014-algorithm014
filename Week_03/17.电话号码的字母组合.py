#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#


# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        phoneMap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrace(digits, start, path):
            if len(path) == len(digits):
                res.append(''.join(path))
                return
            for i in range(start, len(digits)):
                s = phoneMap[digits[i]]
                for j in range(len(s)):
                    path.append(s[j])
                    backtrace(digits, i + 1, path)
                    path.pop()

        res = []
        backtrace(digits, 0, [])
        return res


# @lc code=end
