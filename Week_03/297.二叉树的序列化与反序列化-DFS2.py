#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'None,'
        return str(root.val) + ',' + self.serialize(root.left) + self.serialize(root.right)
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        root = self.buildTree(data)
        return root
    
    def buildTree(self, data):
        if not data:
            return None
        val= data.pop(0)
        if val == 'None':
            return None
        root = TreeNode(int(val))
        root.left = self.buildTree(data)
        root.right = self.buildTree(data)
        return root

if __name__ == "__main__":
    codec = Codec()
    data = "1,2,3,None,None,4,5"
    print(codec.serialize(codec.deserialize(data)))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

