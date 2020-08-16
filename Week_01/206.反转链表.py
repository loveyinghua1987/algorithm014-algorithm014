#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #递归2
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

        """
        #迭代
        prev = None
        while head:
           
            #curr =  head.next
            #head.next = prev
            #prev = head
            #head = curr
           
            head.next, prev, head = prev, head, head.next
        return prev
        """
    """
        #递归1
        return self._reverseList(head)

    def _reverseList(self, head, prev=None):
        if not head:
            return prev
        n = head.next
        head.next = prev
        return self._reverseList(n, head)
    """


# @lc code=end
