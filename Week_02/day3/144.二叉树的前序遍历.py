#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        #迭代2：
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
        """
        #迭代1：
        stack, res = [], []
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            node = stack.pop()
            root = node.right
        return res
        
        #递归2
        def helper(root, res):
            if not root:
                return
            res.append(root.val)
            helper(root.left, res)
            helper(root.right, res)

        res = []
        helper(root, res)
        return res

        #递归1
        if not root:
            return []
        return [root.val] + self.preorderTraversal(
            root.left) + self.preorderTraversal(root.right)
        """

# @lc code=end
