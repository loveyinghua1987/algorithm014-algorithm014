#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        #方法2：迭代
        #时间复杂度： O(n)
        #空间复杂度： O(1)
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root
        '''
        #方法1：递归
        #时间复杂度：O(n) n为节点的个数
        #空间复杂度：O(h) 递归栈的深度，h为树的高度，树的高度最坏情况为n
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        '''

# @lc code=end
