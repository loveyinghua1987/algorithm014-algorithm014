# @lc app=leetcode.cn id=236 lang=python3
#
# [235] 二叉树的最近公共祖先
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
        '''
        #方法1：递归
        #时间复杂度：O(n)
        #空间复杂度：O(n)
        # 递归写法1
        #定义f(x):x结点的子树是否包含p,q结点,如果包含则返回True，否则为False
        #最近公共祖先满足：(f(x.left)&&f(x.right))||((x.val = q.val ||x.val = p.val)&&(f(x.left)||f(x.right)))
        #两种情况：1.x的左右子树分别包含p，q中的一个，2.x为p，q中的一个，并且x的左子树或者右子树包含另外一个结点
        #lson:左子树是否包含p，q结点
        #rson：右子树是否包含p，q结点
        def dfs(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
            if not root:
                return False
            lson = dfs(root.left, p, q)
            rson = dfs(root.right, p, q)
            if (lson and rson) or ((p == root or q == root) and
                                   (lson or rson)):
                res.append(root)
            return lson or rson or (p == root or q == root)

        res = []
        dfs(root, p, q)
        return res[0]
        '''                     
        
		#递归写法2
        #terminator 返回三种情况：root==None，p，q
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        #如果left and right为真，说明左右子树均有找到p或q，此时root为最近公共祖先
        #如果left and right为假，说明left和right当中至少有一个为None
        #如果left为None，即时左子树没有找到p和q，所以p，q都在右子树，此时要求的公共祖先就是right
        #反之right为None，公共祖先为left
        return root if left and right else left or right
        


# @lc code=end