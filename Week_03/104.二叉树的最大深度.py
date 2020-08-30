#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        #迭代
        q = root and [root]
        level = 0
        while q:
            level += 1
            q = [node.left for node in q if node.left] + [node.right for node in q if node.right]
        return level

        #递归
        if not root:
            return 0
        return max(self.maxDepth((root.left)), self.maxDepth(root.right)) + 1
        '''
        def helper(root, level):
            if not root:
                return level
            return max(helper(root.left, level+1), helper(root.right, level+1))
        return helper(root, 0)

    # @lc code=end
