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
        #递归
        def helper(start, end):
            if start > end:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            idx = dic[val]
            root.left = helper(start, idx - 1)
            root.right = helper(idx + 1, end)
            return root

        dic = {val: idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder) - 1)


# @lc code=end
