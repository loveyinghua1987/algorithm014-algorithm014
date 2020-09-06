#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层序遍历
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #方法1：DFS
        #写法1
        res = []
        q = root and [root]
        while q:
            res.append([n.val for n in q])
            q = [child for n in q for child in (n.left, n.right) if child]
        return res
        '''
        #写法2
        res, q = [], root and [root]
        while q:
            temp = []
            layer = []
            for n in q:
                layer.append(n.val)
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
            res.append(layer)
            q = temp
        return res
        
        #写法3
        if not root:
            return []
        res = []
        q = collections.deque([root])
        while q:
            size = len(q)
            layer = []
            for _ in range(size):
                node = q.popleft()
                layer.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(layer)
        return res
        '''


# @lc code=end
