#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:

        #迭代
        #if not root:
        #    return []
        #stack, res = [root], []
        stack, res = root and [root], []
        # root and [root]等价于root if root else [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            #for child in root.children[::-1]:
            #    stack.append(child)
            stack.extend(root.children[::-1])
        return res
        '''
        #递归2
        def helper(root, res):
            if not root:
                return []
            res.append(root.val)
            for child in root.children:
                helper(child, res)
        res = []
        helper(root, res)
        return res
            

        
        #递归1
        if not root:
            return []
        res = [root.val]
        for child in root.children:
            res += self.preorder(child)
        return res            
        '''


# @lc code=end
