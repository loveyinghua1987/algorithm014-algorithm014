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
        #BFS
        q = root and [root]
        res = []
        while q:
            res.append([n.val for n in q])
            q = [child for n in q for child in [n.left, n.right] if child]
        return res
        '''
        #DFS
        def dfs(root, level):
            if not root:
                return
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        res = []
        dfs(root, 0)
        return res
        '''

# @lc code=end
