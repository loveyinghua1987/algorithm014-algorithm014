#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start

class MinStack:
    #方法1：链表，将min加到节点中
    #方法2：数据栈+辅助栈
    #方法3：只是用一个栈
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper = [math.inf]  #float('inf')

    def push(self, x: int) -> None:
        self.data.append(x)
        self.helper.append(min(x, self.helper[-1]))

    def pop(self) -> None:
        self.data.pop()
        self.helper.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.helper[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

