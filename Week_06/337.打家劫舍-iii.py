#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:
        #动态规划
        #1.重复性（分治）
        #   sub(root, 0) = max(sub(root.left, 0),sub(root.left, 1)) +
        #                   max(sub(root.right, 0), sub(root.right, 1))
        #   sub(root, 1) = root.val + sub(root.left, 0) + sub(root.right, 0)
        #2.定义状态数组  dp[root][0] : root为根结点，不偷的话, 能盗取到的最大金额
        #               dp[root][1] : root为根结点， 偷的话， 能盗取到的最大金额
        #3.dp方程  dp[root][0] = max(dp[root.left][0], dp[root.left, 1]) +
        #                        max(dp[root.right][0], dp[root.right][1])
        #          dp[root][1] = root.val + dp[root.left][0] + dp[root.right][0]
        def robsub(root):
            if not root:
                return [0, 0]
            left = robsub(root.left)
            right = robsub(root.right)

            res = [0] * 2
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = root.val + left[0] + right[0]
            return res

        return max(robsub(root))


# @lc code=end
