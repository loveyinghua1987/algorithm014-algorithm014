#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        
        #迭代法1
        #定义path函数，记录从root节点到target节点的路径
        def path(root, target):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path.append(node)
                        if node == target:
                            return path
                        stack.extend([node, node.right, node.left])
                    else:
                        path.pop()

        return next(a for a, b in list(zip(path(root, p), path(root, q)))[::-1]
                    if a == b)
        #zip 方法在 Python 2 和 Python 3 中的不同：在 Python 3.x 中为了减少内存，zip() 返回的是一个对象。如需展示列表，需手动 list() 转换
        '''
        #迭代法2：存储父节点
        #hash_table   建立所有结点和其父结点的映射
        #从p结点往父节点走，一直到root结点，标记已访问
        #从q结点往父节点走，如果遇到已标记访问的结点，即为最近公共祖先结点
        #hashtable
        dic = {}
        stack = root and [root]
        #建立每个节点与父节点的映射
        while stack:
            node = stack.pop()
            if node.left:
                dic[node.left] = node
                stack.append(node.left)
            if node.right:
                dic[node.right] = node
                stack.append(node.right)
        #将p到root经过的节点做标记
        parent = p
        visible = set()
        while parent != root:
            visible.add(parent)
            parent = dic[parent]
		#从q到root，判断经过的节点是否有标记
		#有标记，则返回此节点
		#整个过程都没有标记，则返回root
        parent = q
        while parent != root:
            if parent in visible:
                return parent
            parent = dic[parent]
        return root
        '''

# @lc code=end
