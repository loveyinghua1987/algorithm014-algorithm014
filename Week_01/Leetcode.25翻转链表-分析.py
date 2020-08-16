#Leetcode 25. Reverse Nodes in k-GroupK 个一组翻转链表
#https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

#方法1：迭代解法
#思想：
#把链表结点按照 k 个一组分组，所以可以使用一个指针 head 依次指向每组的头结点。这个指针每次向前移动 k 步，直至链表结尾。
#对于每个分组，我们先判断它的长度是否大于等于 k。若是，我们就翻转这部分链表，否则不需要翻转。

#Q1：如何翻转一个分组内的子链表
#    参见：Leetcode 206. 反转链表（https://leetcode-cn.com/problems/reverse-linked-list/）
#Q2: 如何将子链表的头部与上一个子链表连接，以及子链表的尾部与下一个子链表连接
#	 发现对于第一个子链表，它的头结点 head 前面是没有结点 pre 的，怎么办？
#    可以新建一个哑节点（dummy），把它接到链表的头部，让它作为 prev 的初始值，这样 head 前面就有了一个结点，我们就可以避开链表头部的边界条件。
#    这么做还有一个好处，链表翻转之后，链表的头结点发生了变化，需要利用prev，将它与前面已翻转好的链表连接起来



#时间复杂度：O(n)，其中 n为链表的长度。head 指针会在O(math.floor(n/k))个结点上停留，每次停留需要进行一次 O(k)的翻转操作。
#空间复杂度：O(1)，我们只需要建立常数个变量

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
--------------------------------------------------------------------
class Solution:
    def reverse(self, head: ListNode, tail: ListNode)-> List:
        prev = None    # different 1
        p = head
        while prev != tail:
            temp = p.next
            p.next = prev
            prev = p
            p = temp
        return  tail, head       
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
			#找到tail，保存tail后面的节点
            nex = tail.next     # different 2   
            head, tail = self.reverse(head, tail)
			#两边连接
            prev.next = head
            tail.next = nex     # different 3
			#更新prev和head
            prev = tail
            head = tail.next
        return dummy.next
		

#对比下面的写法，reverse函数定义不一样，连接处理的地方也有相应的改变。 见# different
---------------------------------------------------------------------------------------
class Solution:
    def reverse(self, head: ListNode, tail: ListNode) -> List:
        prev = tail.next   # different 1
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
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
								# different 2
            head, tail = self.reverse(head, tail)
            prev.next = head
								# different 3
            prev = tail
            head = tail.next
        return dummy.next

#方法2：递归解法
#思想：		
#时间复杂度：O(n)
#空间复杂度：O(n/k) 栈的深度 
-----------------------------------------------------------------------------------------
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        #递归
        #1.recursion terminator   
        tail = head
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next  #tail最终记录下一个链表开始的地方
        #2. process logic in current level
        #3. dirll down
        prev = self.reverseKGroup(tail, k)
        while head != tail:
            temp = head.next
            head.next = prev
            prev = head
            head = temp    
        #4. reverse
        return prev

		
