#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #hashtable
        visible = set()
        while head:
            if head in visible:
                return head
            visible.add(head)
            head = head.next
        return None
        """
        #快慢指针
        slow = fast = head
        while True:
            if not fast or not fast.next: return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
        """


# @lc code=end
