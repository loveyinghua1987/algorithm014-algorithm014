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


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #DFS
        def helper(root, level):
            if not root:
                return []
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)

        res = []
        helper(root, 0)
        return res


# @lc code=end
