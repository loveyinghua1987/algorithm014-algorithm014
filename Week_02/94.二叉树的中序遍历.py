#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        #迭代：
        #时间复杂度： O(n)
        #空间复杂度：O(n)
        #迭代写法1 (前、中、后序通用模板)
        stack, res = [], []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            res.append(node.val)
            root = node.right
        return res

        '''
        #递归  
        # 时间复杂度 O(n)
        #空间复杂度 O(logn)  最坏情况 O(n)
        #递归写法1
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        

        #递归写法2: 借助辅助函数helper()
        def helper(root, res):
            if not root:
                return
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)

        res = []
        helper(root, res)
        return res
        '''

# @lc code=end
