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
        #迭代 prev -> head -> head.next   head.next.next->head.next.next.next
        #时间复杂度：O(n)  空间复杂度：O(1)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            #nxt = head.next.next
            #prev.next = head.next
            #head.next.next = head
            #head.next = nxt
            prev.next, head.next.next, head.next = head.next, head, head.next.next
            #prev = head
            #head = head.next 
            prev, head = head, head.next
        return dummy.next


        """
        #递归  head -> head.next ->nxt_head(head.next.next开始的链表已交换好，返回头节点)
        时间复杂度：o(n)  空间复杂度：栈 O(n)
        #terminator
        if not head or not head.next: #不需要交换操作
            return head
        nxt = head.next
        head.next = self.swapPairs(head.next.next)
        nxt.next = head
        return nxt
        """
# @lc code=end
