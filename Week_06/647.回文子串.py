#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#


# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        #方法2：Manacher 算法
        #时间复杂度： O(n)
        #空间复杂度： O(1)

        #预处理
        t = '$#'
        for c in s:
            t += c + '#'
        n = len(t)
        t += '!'
        rm = im = res = 0
        dp = [0] * n
        for i in range(1, n):
            #初始化
            dp[i] = min(dp[2 * im - i], rm - i + 1) if i <= rm else 1
            #中心拓展
            while t[i + dp[i]] == t[i - dp[i]]:
                dp[i] += 1
            #动态维护rm, im
            if i + dp[i] - 1 > rm:
                rm = i + dp[i] - 1
                im = i
            #统计结果 各个以i为中心的回文子串的最大长度-> (dp[i]-1)/2 之和，
            #dp[i]经过前面预处理，求出来的回文子串一定是奇数长度
            res += dp[i] // 2
        return res

        #1. 重复性（分治）：
        # step1：初始化
        # (1)当i <= rm:
        # f(i) : 以i为中心的回文子串的最大半径
        # 假设已经知道k = 0 ... i-1 对应的 f(k),
        # rm: 0 ... i-1为中心的回文子串的最大右边界
        # im: rm 对应的回文中中心位置
        # j: 为 i 以 im 为中心对应的回文子串的另一边的位置
        # j = 2*im - i
        # y: 以j为中心的最大回文子串的边界
        # x: 以i为中心的最大回文子串的边界
        # 情况1： i + f(j) -1 <= rm
        # --------y--j--y---im---x--i--x----rm---
        # f(i) = f(j)
        # 情况2： i + f(j) -1 > rm
        # -y---------j---x--im--y---i-------rm-x-
        # f(i) = rm - i + 1
        # 因为f(j)有上面两种情况,所以
        # f(i) = min(f(j), rm - i + 1)
        #     = min(f(2 * im - i), rm - i + 1)

        # (2)当 i > rm:
        #     f(i) = 1

        # step2： 中心扩展
        # 上面初始化后，可以保证 t[i + f(i) -1] == t[i - f(i) + 1]
        # 向两边扩展，直到两边的字符不相等时停止

        # step3：动态维护rm，im
        # rm, im= 0
        # for k in range(i):
        #     if k + f(k)-1 > rm:
        #         rm = k + f(k) -1
        #         im = k

        # 2. 定义dp数组 dp[i] : 以i为中心的回文子串的最大半径
        #                     通过dp[i]可以得到最右边界rm = i + dp[i] -1
        #                     通过最大半径dp[i],可以推算出以i为中心的回文子串的个数为dp[i] - 1
        # 3. dp方程
        #     dp[i] = min(dp[2 *im - i], rm - i + 1)

        # 预处理：
        # 回文子串的长度有两种可能，奇数子串和偶数子串，
        # 可以对其做预处理，字符之间加'#',这样求出来的回文子串的长度都为奇数了
        # 在step2中心扩展时，我们需要注意的是不能让下标越界，
        # 有一个很简单的办法，就是在开头加一个 $，并在结尾加一个
        # 这样开头和结尾的两个字符一定不相等，循环就可以在这里终止。头、尾加$、!，以便好处理头尾相等时的停止条件
        '''
        #方法1：中心拓展  
        #时间复杂度：O(n)
        #空间复杂度: O(1) 
        n = len(s)
        res = 0
        #l= i/2  r=i/2+i%2   i:0~2n-1
        for i in range(2 * n - 1):
            l = i // 2
            r = i // 2 + i % 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res
        '''


# @lc code=end
