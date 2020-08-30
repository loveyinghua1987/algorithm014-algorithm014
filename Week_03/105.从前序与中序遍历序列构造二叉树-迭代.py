#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #迭代
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        stack = [root]
        pre = 1
        ino = 0
        while pre < len(preorder):
            node = TreeNode(preorder[pre])
            pre += 1
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino += 1
            if prev:
                prev.right = node
            else:
                stack[-1].left = node
            stack.append(node)
        return root


# @lc code=end
