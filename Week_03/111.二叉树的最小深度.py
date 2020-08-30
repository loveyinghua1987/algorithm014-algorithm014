#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        #广度优先搜索
        if not root:
            return 0
        que = collections.deque([(root, 1)])
        while que:
            node, depth = que.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                que.append((node.left, depth + 1))
            if node.right:
                que.append((node.right, depth + 1))
        '''
        #深度优先搜索
        if not root:
            return 0
        m1 = self.minDepth(root.left)
        m2 = self.minDepth(root.right)
        return min(m1, m2) + 1 if m1 and m2 else m1 + m2 + 1
        '''


# @lc code=end
