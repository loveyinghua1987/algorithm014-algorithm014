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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #递归
        #1.recursion terminator
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        #如果上面没有return，tail此时为下一k个链表的头节点
        #2. process logic in current level
        #3. dirll down  
        prev = self.reverseKGroup(tail, k)
        while head != tail:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

        #4. reverse
   


# @lc code=end
