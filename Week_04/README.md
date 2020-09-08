学习笔记
一、主要学习内容：
1. **深度优先搜索(DFS)、广度优先搜索(BFS)**
   - 熟记下面DFS、BFS模板
   - 特点：需要**visited**记录已经访问过的节点，防止重复访问超时
   - 树、图的遍历实质上，就是DFS和BFS
   
    ``` 
    # Python

    # DFS递归模板
    visited = set() 

    def dfs(node, visited):
        if node in visited: # terminator
            # already visited 
            return 

        visited.add(node) 

        # process current node here. 
        ...
        for next_node in node.children(): 
            if next_node not in visited: 
                dfs(next_node, visited)

    # DFS非递归模板
    def DFS(self, tree): 

        if tree.root is None: 
            return [] 

        visited, stack = set(), [tree.root]

        while stack: 
            node = stack.pop() 
            visited.add(node)

            process (node) 
            nodes = generate_related_nodes(node) 
            stack.append(nodes) 

        # other processing work 
	...

    # BFS代码模板 
    def BFS(graph, start, end):
        visited = set()
        queue = collections.deque() 
        queue.append([start])

        while queue: 
            node = queue.popleft() 
            visited.add(node)

            process(node) 
            nodes = generate_related_nodes(node) 
            queue.append(nodes)

        # other processing work 
        ...
    ``` 

2. 贪心算法
   贪心算法定义：一种在每步选择中，都采取在当前状态下最好或最优（最有利）的选择，从而希望导致结果是全局最好或最优的选择。  

   局部最优不一定是全局最优，所以，贪心算法有一定的局限性。  
   一般如下情况可以使用贪心：  
   （1）在某些局部最优可以导致全局最优的情况下，可以使用贪心算法。
   （2）在很多情况下，在某一步可以用贪心算法，然后在全局再加一个搜索递归、或者动态规划等类似的方法。

    **贪心、回溯、动态规划算的共同点：**  
    完成一件事情，是分步决策的

    **贪心算法、回溯、动态规划 的区别**  
    贪心算法：对每个子问题的解决方案都做出选择，不能回退。形象地可以理解为：只顾眼前不考虑未来。贪心算法的关键：它对子问题解决办法，就直接在当下做出最粗暴的选择，也就是局部最优的选择，同时是不能回退的。如果能回退的话，就是回溯，以及带最优判断的回溯（也就是动态规划）。
    
    动态规划：会保存以前的的运行结果，并根据以前的结果对当前进行选择，有回退功能。（在适当的时候回退，重新做选择）  

    **贪心**：当下做出最优判断  
    **回溯**：能够回退  
    **动态规划**：最优判断 + 回退

    贪心算法和动态规划相比，它既不看前面（也就是说它不需要从前面的状态转移过来），也不看后面（无后效性，后面的选择不会对前面的选择有影响），因此贪心算法时间复杂度一般是线性的，空间复杂度是常数级别的。

    **贪心算法应用场景**
    贪心算法可以解决一些最优化问题，如：求图中的最小生成树、求哈夫曼编码等。然而对于工程和生活中的问题，贪心法一般不能得到我们所要求的答案。  
    一旦一个问题可以通过贪心法来解决，那么贪心法一般是解决这个问题的最好的办法。由于贪心法的高效性以及其所求得的答案比较接近最优结果，贪心法也可以用作辅助算法或者直接解决一些要求结果不特别精确的问题。比如说，最短路径问题-dijkstra算法里面都会用一些所谓的辅助的办法，用贪心来进行解决。

1. 二分查找
   推荐下面labuladong对二分查找算法的详解：
   https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/ 

    **基本二分、寻找左侧边界二分、寻找右侧边界二分逻辑*

    第一个，最基本的二分查找算法：

    ``` 
    因为我们初始化 right = nums.length - 1
    所以决定了我们的「搜索区间」是 [left, right]
    所以决定了 while (left <= right)
    同时也决定了 left = mid+1 和 right = mid-1

    因为我们只需找到一个 target 的索引即可
    所以当 nums[mid] == target 时可以立即返回

    def binarySearch(nums, target):
        left, right = 0, len(nums) - 1  #注意
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  #注意
            else:  #nums[mid] > target
                right = mid - 1  #注意
        return -1
    ``` 

    第二个，寻找左侧边界的二分查找：

    ``` 
    因为我们初始化 right = nums.length
    所以决定了我们的「搜索区间」是 [left, right)
    所以决定了 while (left < right)
    同时也决定了 left = mid + 1 和 right = mid

    因为我们需找到 target 的最左侧索引
    所以当 nums[mid] == target 时不要立即返回
    而要收紧右侧边界以锁定左侧边界

    def left_bound(nums, target):
        left, right = 0, len(nums)  #注意
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid  #注意
            elif nums[mid] < target:
                left = mid + 1
            else:  #nums[mid] > target
                right = mid
        return left  #注意
    ``` 

    第三个，寻找右侧边界的二分查找：

    ``` 
    因为我们初始化 right = nums.length
    所以决定了我们的「搜索区间」是 [left, right)
    所以决定了 while (left < right)
    同时也决定了 left = mid + 1 和 right = mid

    因为我们需找到 target 的最右侧索引
    所以当 nums[mid] == target 时不要立即返回
    而要收紧左侧边界以锁定右侧边界

    又因为收紧左侧边界时必须 left = mid + 1
    所以最后无论返回 left 还是 right，必须减一

    def right_bound(nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1  #注意
            elif nums[mid] < target:
                left = mid + 1
            else:  #nums[mid] > target
                right = mid
        return left - 1  #注意
    ``` 
    将「搜索区间」全都统一成了两端都闭，便于记忆，只要修改两处即可变化出三种写法  

    ```
    #最基本情况
    def binarySearch(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  #nums[mid] == target
                return mid
        return -1

    #寻找左侧边界
    def left_bound(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  #nums[mid] == target
                # 别返回，锁定左侧边界
                right = mid - 1
        # 最后要检查 left 越界的情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    #寻找右侧边界
    def right_bound(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  #nums[mid] == target
                #别返回，锁定右侧边界
                left = mid + 1
        # 最后要检查 right 越界的情况
        if right < 0 or nums[right] != target:
            return -1
        return right
    ``` 
# 做题情况
课后作业：
使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方

``` 
def findDisordpos(self, nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    if nums[left] <= nums[right]:  #整个有序，没有无序的地方
        return -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        if nums[mid - 1] > nums[mid]:
            return mid
        if nums[mid] >= nums[left]:#前面有序
            left = mid + 1
        else:
            right = mid - 1
``` 
## 第四周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)| 🟡| DFS、BFS | 1 ||
| [433](https://leetcode.com/problems/minimum-genetic-mutation/discuss/?currentPage=1&orderBy=most_votes&query=) | [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)| 🟡| DFS、BFS | 1 ||
| [22](https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)| 🟡| DFS、BFS | 1 ||
| [515](https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/?currentPage=1&orderBy=most_votes&query=) | [在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/)| 🟡| DFS、BFS | 1 ||
| [127](https://leetcode.com/problems/word-ladder/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词接龙](https://leetcode-cn.com/problems/word-ladder/)| 🟡| DFS、BFS | 1 |BFS、双向BFS|
| [126](https://leetcode.com/problems/word-ladder-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)| 🔴️| DFS、BFS | 1 |BFS、双向BFS|
| [200](https://leetcode.com/problems/number-of-islands/discuss/?currentPage=1&orderBy=most_votes&query=) | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)| 🟡| DFS、BFS | 1 ||
| [529](https://leetcode.com/problems/minesweeper/discuss/?currentPage=1&orderBy=most_votes&query=) | [扫雷游戏](https://leetcode-cn.com/problems/minesweeper/)| 🟡| DFS、BFS | 1 ||
| [860](https://leetcode.com/problems/lemonade-change/discuss/?currentPage=1&orderBy=most_votes&query=) | [柠檬水找零](https://leetcode-cn.com/problems/lemonade-change/)| 🟢| 贪心 | 1 ||
| [122](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)| 🟢| 贪心 | 1 ||
| [455](https://leetcode.com/problems/assign-cookies/discuss/?currentPage=1&orderBy=most_votes&query=) | [分发饼干](https://leetcode-cn.com/problems/assign-cookies/)| 🟢| 贪心 | 1 |排序+贪心|
| [874](https://leetcode.com/problems/walking-robot-simulation/discuss/?currentPage=1&orderBy=most_votes&query=) | [模拟行走机器人](https://leetcode-cn.com/problems/walking-robot-simulation/)| 🟢| 贪心 | 1 ||
| [55](https://leetcode.com/problems/jump-game/discuss/?currentPage=1&orderBy=most_votes&query=) | [跳跃游戏](https://leetcode-cn.com/problems/jump-game/)| 🟡| 贪心 | 1 ||
| [45](https://leetcode.com/problems/jump-game-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/)| 🔴️| 贪心 | 1 ||
| [69](https://leetcode.com/problems/sqrtx/discuss/?currentPage=1&orderBy=most_votes&query=) | [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)| 🟢| 二分查找 | 1 |二分查找、袖珍计算器、牛顿迭代法|
| [367](https://leetcode.com/problems/valid-perfect-square/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的完全平方数](https://leetcode-cn.com/problems/valid-perfect-square/)| 🟢| 二分查找 | 1 |二分查找、牛顿迭代法|
| [33](https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/)| 🟡| 二分查找 | 1 ||
| [74](https://leetcode.com/problems/search-a-2d-matrix/) | [搜索二维矩阵](https://leetcode-cn.com/problems/search-a-2d-matrix/)| 🟡| 二分查找 | 1 ||
| [153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/)| 🟡| 二分查找 | 1 ||