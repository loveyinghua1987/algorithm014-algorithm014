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
        #BFS
        #写法1
        res = []
        q = root and [root]
        while q:
            res.append(max([n.val for n in q]))
            q = [child for n in q for child in [n.left, n.right] if child]
        return res
        '''
        #写法2：
        if not root: return
        res, q = [], [root]
        while q:
            nxt = []
            res.append(float('-inf'))
            for node in q:
                res[-1] = max(res[-1], node.val)
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            q = nxt
        return res
        '''
# @lc code=end
