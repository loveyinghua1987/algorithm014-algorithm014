#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #方法2：迭代 中序遍历
        stack, prev = [], float('-inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            root = node.right
        return True
        '''
        #方法1：递归
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            if root.val <= lower or root.val >= upper:
                return False
            return helper(root.left, lower, root.val) and helper(
                root.right, root.val, upper)

        return helper(root)
        '''


# @lc code=end
