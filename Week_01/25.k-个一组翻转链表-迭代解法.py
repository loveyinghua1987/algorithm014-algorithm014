#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def reverse(self, head: ListNode, tail: ListNode) -> List:
        prev = tail.next
        p = head
        while prev != tail:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head:
            #找tail
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:       #遍历找不到k个，直接返回
                    return dummy.next
            #找到tail
            nex =tail.next  #保存tail后面的节点

            head, tail = self.reverse(head, tail)
            #两边连接
            prev.next = head
            tail.next = nex
            #更新prev和head
            prev = tail
            head = tail.next
        return dummy.next


# @lc code=end

