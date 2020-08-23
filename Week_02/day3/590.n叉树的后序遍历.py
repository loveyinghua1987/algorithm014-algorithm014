#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        #迭代：先求 根-右-左，再倒序输出
        if not root:  #注意边界条件
            return []
        stack, res = [root], []
        #stack, res = root and [root], []  # root and [root]等价于root if root else [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            for child in root.children:
                stack.append(child)
            #stack.extend(root.children)
        return res[::-1]
        """
        #递归2
        def helper(root, res):
            if not root:
                return []
            for child in root.children:
                helper(child, res)
            res.append(root.val)
        res = []
        helper(root, res)
        return res

        
        #递归1
        if not root:
            return []
        res = []
        for child in root.children:
            res += self.postorder(child)
        res += [root.val]
        return res
        """


# @lc code=end
