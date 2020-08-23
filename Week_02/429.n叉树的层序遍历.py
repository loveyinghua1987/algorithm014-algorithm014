#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
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
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        #递归
        def helper(root, level):  #level从0开始
            #recursion terminator
            if not root:
                return []
            #process logic in current layer
            if len(res) < level + 1:
                res.append([])
            res[level].append(root.val)
            #drill down
            for child in root.children:
                helper(child, level + 1)
            #reverse

        res = []
        helper(root, 0)
        return res
        '''
        #迭代1
        if not root:
            return []
        q, res = [root], []
        while q:
            res.append([node.val for node in q])
            q = [child for node in q for child in node.children]
        return res
        
        #迭代2
        if not root:
            return []
        q, res = [root], []
        while q:
            layer = []
            for _ in range(len(q)):
                node = q.pop(0)
                layer.append(node.val)
                q.extend([child for child in node.children])
            res.append(layer)
        return res
        '''


# @lc code=end
