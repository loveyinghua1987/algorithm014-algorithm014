#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        #递归
        if not head or not head.next:
            return head
        a = head
        b = head.next

        a.next = self.swapPairs(b.next)
        b.next = a

        return b
        """
        #迭代
        dummy = ListNode(-1)  #哑节点
        dummy.next = head
        prev = dummy

        while head and head.next:
            a = head
            b = head.next

            prev.next = b
            a.next = b.next
            b.next = a

            prev = a
            head = prev.next

        return dummy.next


# @lc code=end
