学习笔记
本周主要学习内容：
**动态规划**
``` 
递归代码模板
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
``` 
```
分治代码模板
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
``` 

动态规划 Dynamic Programming
1.Wiki 定义： https://en.wikipedia.org/wiki/Dynamic_programming
2.“Simplifying a complicated problem by breaking it down into simpler sub-problems”  (in a recursive manner)
3.Divide & Conquer + Optimal substructure            分治 + 最优子结构

关键点：
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构） 
共性：找到重复子问题 
差异性：最优子结构、中途可以淘汰次优解

动态规划 steps：
1. 分治找它的重复性和子问题
2. 定义出状态空间  (难点！！！) 
3. 用记忆化搜索递归或从下到上进行递推（也就是自底向上进行递推）

DP：
重复性（分治）
定义状态数组 (难点！！！) 
DP方程

## 第六周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [62](https://leetcode.com/problems/unique-paths/discuss/?currentPage=1&orderBy=most_votes&query=) | [不同路径](https://leetcode-cn.com/problems/unique-paths/)| 🟡| DP | 1 ||
| [63](https://leetcode.com/problems/unique-paths-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)| 🟡| DP | 1 ||
| [1143](https://leetcode.com/problems/longest-common-subsequence/discuss/?currentPage=1&orderBy=most_votes&query=) | [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)| 🟡| DP | 1 ||
| [70](https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)| 🟢| DP | 1 ||
| [120](https://leetcode.com/problems/triangle/discuss/38735/Python-easy-to-understand-solutions-(top-down-bottom-up)) | [三角形最小路径和](https://leetcode-cn.com/problems/triangle/)| 🟡| DP | 1 ||
| [53](https://leetcode.com/problems/maximum-subarray/discuss/?currentPage=1&orderBy=most_votes&query=) | [最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)| 🟢| DP | 1 ||
| [152](https://leetcode.com/problems/maximum-product-subarray/discuss/?currentPage=1&orderBy=most_votes&query=) | [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/)| 🟡| DP | 1 ||
| [322](https://leetcode.com/problems/coin-change/discuss/?currentPage=1&orderBy=most_votes&query=) | [零钱兑换](https://leetcode-cn.com/problems/coin-change/)| 🟡| DP | 1 ||
| [198](https://leetcode.com/problems/house-robber/discuss/?currentPage=1&orderBy=most_votes&query=) | [打家劫舍](https://leetcode-cn.com/problems/house-robber/)| 🟢| DP | 1 ||
| [213](https://leetcode.com/problems/house-robber-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [打家劫舍 II](https://leetcode-cn.com/problems/house-robber-ii/)| 🟡| DP | 1 ||
| [337](https://leetcode.com/problems/house-robber-iii/discuss/?currentPage=1&orderBy=most_votes&query=) | [打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/)| 🟡| DP | 1 ||
| [121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)| 🟢| DP | 1 ||
| [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)| 🟢| DP | 1 ||
| [123](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)| 🔴️| DP | 1 ||
| [309](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/?currentPage=1&orderBy=most_votes&query=) | [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)| 🟡| DP | 1 ||
| [188](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机 IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)|🔴️| DP | 1 ||
| [714](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)|🟡| DP | 1 ||

### 作业
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [64](https://leetcode.com/problems/minimum-path-sum/discuss/?currentPage=1&orderBy=most_votes&query=) | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)|🟡| DP | 1 ||
| [91](https://leetcode.com/problems/decode-ways/discuss/?currentPage=1&orderBy=most_votes&query=) | [解码方法](https://leetcode-cn.com/problems/decode-ways/)|🟡| DP | 1 ||
| [221](https://leetcode.com/problems/maximal-square/discuss/?currentPage=1&orderBy=most_votes&query=) | [最大正方形](https://leetcode-cn.com/problems/maximal-square/)|🟡| DP | 1 ||
| [621](https://leetcode.com/problems/task-scheduler/discuss/?currentPage=1&orderBy=most_votes&query=) | [任务调度器](https://leetcode-cn.com/problems/task-scheduler/)|🟡|  | 1 ||
| [647](https://leetcode.com/problems/palindromic-substrings/discuss/?currentPage=1&orderBy=most_votes&query=) | [回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)|🟡| DP | 1 ||
| [32](https://leetcode.com/problems/longest-valid-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses/)|🔴️| DP | 1 ||
| [72](https://leetcode.com/problems/edit-distance/discuss/?currentPage=1&orderBy=most_votes&query=) | [编辑距离](https://leetcode-cn.com/problems/edit-distance/)|🔴️| DP | 1 ||
