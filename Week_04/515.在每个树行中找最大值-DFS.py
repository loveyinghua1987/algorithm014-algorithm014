#
# @lc app=leetcode.cn id=515 lang=python3
#
# [515] 在每个树行中找最大值
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        #DFS
        def dfs(root, depth):
            if not root:
                return
            if len(res) <= depth:
                res.append(float('-inf'))
            res[depth] = max(res[depth], root.val)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)

        res = []
        dfs(root, 0)
        return res


# @lc code=end
