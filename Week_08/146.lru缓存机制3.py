#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#


# @lc code=start
class DLinkedNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.add_to_head(node)
            self.cache[key] = node
            self.size += 1
            if self.size > self.capacity:
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1

    def move_to_head(self, node):
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        node.prev = self.head

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def remove_tail(self):
        node = self.tail.prev
        self.remove_node(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
