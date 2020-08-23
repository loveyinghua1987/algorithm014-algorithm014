学习笔记

要点:
1. 哈希表
2. 二叉树的DFS遍历（前、中、后序）和BFS遍历（层次遍历）
   - **前、中、后序遍历通用迭代模板**
    ``` 
    #中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
	stack, res = [], []
	while stack or root:
		while root:
			stack.append(root)      
			root = root.left
		node = stack.pop()
		res.append(node.val)   #区别在这里
		root = node.right
	return res
    #前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
	stack, res = [], []
	while stack or root:
		while root:
			res.append(root.val)    #区别在这里
			stack.append(root)
			root = root.left
		node = stack.pop()
		root = node.right
	return res
    #后序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
	stack, res = [], []
	while stack or root:
		while root:
			res.append(root.val)    #区别在这里
			stack.append(root)
			root = root.right     #区别在这里
		node = stack.pop()
		root = node.left         #区别在这里
	return res[::-1]             #区别在这里
    ```
    - **前、后序遍历常用模板**
    ``` 
    #前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
	if not root:
		return []
	stack, res = [root], []
	while stack:
		root = stack.pop()
		res.append(root.val)
		if root.right:
			stack.append(root.right)
		if root.left:
			stack.append(root.left)
	return res
    #后序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
	if not root:
		return []
	stack, res = [root], []
	while stack:
		root = stack.pop()
		res.append(root.val)
		if root.right:
			stack.append(root.left)
		if root.left:
			stack.append(root.right)
	return res[::-1]
    ```
    - **前、中、后序通用递归模板**
    ``` 
    #前序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
	if not root:
		return []
	return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    #中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
	if not root:
		return []
	return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    #后序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
	if not root:
		return []
	return self.inorderTraversal(root.left) + self.inorderTraversal(root.right) + [root.val]
    ``` 
    ``` 
    #先序遍历
    def preorderTraversal(self, root: TreeNode) -> List[int]:
	def helper(root, res):
		if not root:
			return
		res.append(root.val)
		helper(root.left, res)
		helper(root.right, res)

	res = []
	helper(root, res)
	return res
    #中序遍历
    def inorderTraversal(self, root: TreeNode) -> List[int]:
	def helper(root, res):
		if not root:
			return
		helper(root.left, res)
		res.append(root.val)
		helper(root.right, res)
	res = []
	helper(root, res)
	return 
    #后序遍历
    def postorderTraversal(self, root: TreeNode) -> List[int]:
	def helper(root, res):
		if not root:
			return
		helper(root.left, res)
		helper(root.right, res)
		res.append(root.val)
	res = []
	helper(root, res)
	return 
3. N叉树的DFS遍历（前、后序）和BFS遍历（层次遍历）
   跟二叉树的类似
4. 堆的使用（TopK大对应最小堆，TopK小对应最大堆）
   python 自有的堆 heapq是最小堆
   遇到需要使用最大堆的时候，可以采用元素取负值后再入heapq最小堆，处理完后，取出再取负即可
5. 图(DFS遍历和BFS遍历，注意要加visited)
   


# 做题情况

## 第二周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [242](https://leetcode.com/problems/valid-anagram/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)| 🟢| 哈希表、映射、集合 | 2 |哈希表|
| [49](https://leetcode.com/problems/group-anagrams/discuss/?currentPage=1&orderBy=most_votes&query=) | [字母异位词分组](https://leetcode-cn.com/problems/group-anagrams/)| 🟡 | 哈希表、映射、集合 | 2 |哈希表|
| [1](https://leetcode.com/problems/two-sum/discuss/?currentPage=1&orderBy=most_votes&query=) | [两数之和](https://leetcode-cn.com/problems/two-sum/)| 🟢  | 哈希表、映射、集合 | 2 |哈希表|
| [94](https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)| 🟡 | 树、二叉树、二叉搜索树 | 2 |前、中、后序遍历通用模板，递归模板|
| [144](https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)| 🟡 | 树、二叉树、二叉搜索树 | 2 |前、中、后序遍历通用模板，前、后序常用模板，递归模板|
| [590](https://leetcode.com/problems/n-ary-tree-postorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)| 🟢 | 树、二叉树、二叉搜索树 | 2 |前、后序常用模板，递归模板|
| [589](https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [N叉树的前序遍历](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/)| 🟢 | 树、二叉树、二叉搜索树 | 2 |前、后序常用模板，递归模板|
| [429](https://leetcode.com/problems/n-ary-tree-level-order-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/)| 🟡 | 树、二叉树、二叉搜索树 | 2 |迭代、递归写法|
| [剑指Offer 40]() | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)| 🟢 | 堆、二叉堆、图 | 2 |最大堆|
| [239](https://leetcode.com/problems/sliding-window-maximum/discuss/?currentPage=1&orderBy=most_votes&query=) | [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)| 🔴️ | 堆、二叉堆、图 | 2 |最大堆|
| [264](https://leetcode.com/problems/ugly-number-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [丑数 II](https://leetcode-cn.com/problems/ugly-number-ii/)| 🟡 | 堆、二叉堆、图 | 2 |最小堆|
| [347](https://leetcode.com/problems/top-k-frequent-elements/discuss/?currentPage=1&orderBy=most_votes&query=) | [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)| 🟡 | 堆、二叉堆、图 | 2 |最小堆|
| [200](https://leetcode.com/problems/number-of-islands/discuss/?currentPage=1&orderBy=most_votes&query=) | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)| 🟡 | 堆、二叉堆、图 | 2 |图，dfs，bfs|

其他
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [1021](https://leetcode.com/problems/remove-outermost-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [删除最外层的括号](https://leetcode-cn.com/problems/remove-outermost-parentheses/)| 🟢| - | 2 |-|
| [412](https://leetcode.com/problems/fizz-buzz/discuss/?currentPage=1&orderBy=most_votes&query=) | [Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)| 🟢| - | 2 |哈希表|
| [647](https://leetcode.com/problems/palindromic-substrings/discuss/?currentPage=1&orderBy=most_votes&query=) | [回文子串](https://leetcode-cn.com/problems/palindromic-substrings/)| 🟡| - | 1 |中心拓展|
| [104](https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/)| 🟢| - | 2 |dfs，bfs|
