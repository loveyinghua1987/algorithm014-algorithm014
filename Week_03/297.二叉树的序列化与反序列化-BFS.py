#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        que = collections.deque([root])
        s = str(root.val) + ','
        while que:
            node = que.popleft()
            if not node.left:
                s += 'None,'
            else:
                s += str(node.left.val) + ','
                que.append(node.left)
            if not node.right:
                s += 'None,'
            else:
                s += str(node.right.val) + ','
                que.append(node.right)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        que = collections.deque([root])
        i = 1
        while i < len(data) - 1:
            node = que.popleft()
            if i < len(data) - 1 and data[i] != 'None':
                left = TreeNode(int(data[i]))
                node.left = left
                que.append(left)
            if i + 1 < len(data) - 1 and data[i + 1] != 'None':
                right = TreeNode(int(data[i + 1]))
                node.right = right
                que.append(right)
            i += 2
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end
