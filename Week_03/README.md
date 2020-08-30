学习笔记

本周主要学习了递归
分治、回溯分别只是递归的一种特殊类型  

要点：  

一、分清楚分治和回溯的使用场景  
**分治**：问题可以划分为几个子问题，且对于下层递归返回后的结果需要处理  

**回溯**：排列、组合等问题，问有多少种组合，排列，或解决方案。比如：组合、全排列、子集、电话号码的字母组合、N皇后这些都是这种类型

二、记住模板，灵活套用模板

1. 泛型递归、树的递归  
   
   模板
   ```  
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

2. 分治、回溯

   分治模板
   ``` 
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
    回溯模板
    ``` 
    res = []
    def backtrack(path, choices):
        if terminator:  #满足结束条件
            res.add(path)
            return
        for choice in choices:
            # make a choice  做选择
            backtrack(path, choices)
            # cancel the choice  撤销选择
    backtrace([], choices)
    return res
    ```



# 做题情况

## 第三周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [70](https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)| 🟢| 泛型递归 | 1 |矩阵快速幂、通项公式|
| [22](https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)| 🟡| 泛型递归 | 1 |回溯|
| [226](https://leetcode.com/problems/invert-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/)| 🟢| 树的递归 | 1 |-|
| [98](https://leetcode.com/problems/validate-binary-search-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)| 🟡| 树的递归 | 1 |利用二叉搜索树的定义，或它的中序遍历是升序的|
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)| 🟢| 树的递归 | 1 |-|
| [111](https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)| 🟢| 树的递归 | 1 |-|
| [297](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/)| 🔴️| 树的递归 | 1 |-|
| [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/)| 🟡| 树的递归 | 1 |-|
| [105](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [从前序与中序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)| 🟡| 树的递归 | 1 |-|
| [77](https://leetcode.com/problems/combinations/discuss/?currentPage=1&orderBy=most_votes&query=) | [组合](https://leetcode-cn.com/problems/combinations/)| 🟡| 分治、回溯 | 1 |回溯 + 剪枝|
| [46](https://leetcode.com/problems/permutations/discuss/?currentPage=1&orderBy=most_votes&query=) | [全排列](https://leetcode-cn.com/problems/permutations/)| 🟡| 分治、回溯 | 1 |回溯|
| [47](https://leetcode.com/problems/permutations-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)| 🟡| 分治、回溯 | 1 |回溯 + 剪枝|
| [50](https://leetcode.com/problems/powx-n/discuss/?currentPage=1&orderBy=most_votes&query=) | [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)| 🟡| 分治、回溯 | 1 |分治、快速幂|
| [78](https://leetcode.com/problems/subsets/discuss/?currentPage=1&orderBy=most_votes&query=) | [子集](https://leetcode-cn.com/problems/subsets/)| 🟡| 分治、回溯 | 1 |回溯|
| [169](https://leetcode.com/problems/majority-element/discuss/?currentPage=1&orderBy=most_votes&query=) | [多数元素](https://leetcode-cn.com/problems/majority-element/)| 🟢| 分治、回溯 | 1 |分治、哈希表、排序、随机化、Boyer-Moore 投票算法|
| [17](https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/?currentPage=1&orderBy=most_votes&query=) | [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)| 🟡| 分治、回溯 | 1 |回溯|
| [51](https://leetcode.com/problems/n-queens/discuss/?currentPage=1&orderBy=most_votes&query=) | [N皇后](https://leetcode-cn.com/problems/n-queens/)| 🔴️| 分治、回溯 | 1 |回溯|