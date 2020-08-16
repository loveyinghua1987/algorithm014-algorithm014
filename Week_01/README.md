学习笔记

# 不要死磕！！！
# 最大的误区：刷题只刷一遍
有种被戳中的感觉。之前有自己在Leetcode上面刷题，一天下来能刷两道就不错了，特别慢，刷完回头去看不记得了，后面也难得坚持下去了，也感觉东西是零散的，不系统，看到题不知道要如何思考，或者有想法就是写不出来。

这一周严格按五毒神掌进行，感觉效果还不错。现在看到题目会有想法了，知道往哪个方向去思考了，通过多次反复练习，也发现自己对这个越来越熟悉，有些题目自己也能一下子写出来，没那么多受挫感了。

通过这周的题目有以下的一些体会：
1.  时间复杂度和空间复杂度总算弄明白了，要有空间换时间的思维。优化思考方向：升维和空间换时间
2.  对于觉得复杂没有什么具体的实现思路的问题，尝试用数学归纳法，向递归的方向思考，递归要注意使用带缓存的递归，不然效率会很低。勤用递归模块，不要人肉递归。递归就是找重复子问题(最近最简单方法，将其拆解成可重复解决的问题)
    ##### 递归模板(python)   
        def recursive(level, param1, param2,...):
            #1.recursion terminator
            if level > MAX_LEVEL:
                process_result
                return
            #2.process logic in current level
            process(level, data,...)
            #3.drill down
            self.recursion(level+1, p1, ...)
            #4.reverse the current level status if needed
3. 链表的题目，觉得边界条件不好处理的时候，引入dummy哑节点作为prev的初始值。
   同时有递归和迭代的解法。
   迭代解法：一般都会引入dummy节点指向head头节点，prev指向dummy节点，和head、head.next 3个指针一起更新信息，接着自我更新指引整个迭代过程。
   递归解法：按递归模板写，弄清楚指针连接位置情况，注意#2和#4位置的操作步骤。有时候会借助一个辅助函数helper(),自己内部实现一个递归，再内部调用helper()
4. 栈：如果问题有对称相似结构，形象的打个比方，像剥洋葱，可以考虑借助栈来解决。灵活运用入栈、出栈条件可以实现中间向两边搜索这种问题。柱状图中最大的矩形、接雨水这两道hard的题目都可以使用这个思路写出来。
5. 如果问题需要同时对头、尾都要进行操作，最好考虑用deque双端队列来解决，可以快速在头、尾插入和删除，O(1)常数的时间复杂度。滑动窗口的问题需要处理两端的元素，所以使用双端队列。
6. 双指针的使用情况很多，在数组、链表、栈里面都频繁有使用。所以遇到问题，可以想一下可不可以用双指针。
7. 如果要求在常数内的时间获取数据，可以往哈希表想想。
8. 熟悉各种数据结构(stack,que,deque,list, skip list)的特点，根据题目，选择合适符合要求的使用。



附上“五毒神掌”和“切题四件套”时刻警醒自己！！！
### 五毒神掌
1. 5分钟读题和思考，直接看题解，多解法比较解法优劣（时间、空间复杂度），默写背诵最好的算法
2. 马上自己写，提交LeetCode，多种解法，体会、优化（刷题第一次）
3. 24 小时之后，再重复做题（不同解法的熟练程度，专项训练）(刷题第二次)
4. 一周后重复做题  (刷题第三次)
5. 面试前一周恢复性训练 (刷题第四次)
可根据自身情况增加练习次数

### 切题四件套
1. 理清题意，明确题目的要求
2. 想尽可能多的解法，对比几种写法的时间、空间复杂度，找到比较好的解法
3. 尽可能多动手写
4. 测试用例
   


# 做题情况

## 第一周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [70](https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)| 🟢| 数组 | 2 |数学归纳法、递归(加缓存)、动态规划及优化|
| [283](https://leetcode.com/problems/move-zeroes/discuss/?currentPage=1&orderBy=most_votes&query=) | [移动零](https://leetcode-cn.com/problems/move-zeroes/)| 🟢 | 数组 | 2 |双指针(空间优化)|
| [11](https://leetcode.com/problems/container-with-most-water/discuss/?currentPage=1&orderBy=most_votes&query=) | [盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)| 🟡 | 数组 | 2 |左右指针两边夹逼 |
| [15](https://leetcode.com/problems/3sum/discuss/?currentPage=1&orderBy=most_votes&query=) | [三数之和](https://leetcode-cn.com/problems/3sum/)| 🟡 | 数组 | 2 |排序+双指针(两边夹逼)+排重，高频老题|
| [206](https://leetcode.com/problems/reverse-linked-list/discuss/?currentPage=1&orderBy=most_votes&query=) | [反转链表](https://leetcode-cn.com/problems/reverse-linked-list/)| 🟢 | 链表 | 2 | 迭代、递归、指针变换顺序|
| [24](https://leetcode.com/problems/swap-nodes-in-pairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/)| 🟡 | 链表 | 2 |递归、指针变换顺序、迭代(引入dummy哑节点作为prev的初始值)|
| [141](https://leetcode.com/problems/linked-list-cycle/discuss/?currentPage=1&orderBy=most_votes&query=) | [环形链表](https://leetcode-cn.com/problems/linked-list-cycle/)| 🟢 | 链表 | 2 |哈希、快慢指针|
| [142](https://leetcode.com/problems/linked-list-cycle-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/)| 🟡 | 链表 | 2 | 快慢指针、哈希|
| [25](https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/?currentPage=1&orderBy=most_votes&query=) | [K 个一组翻转链表](https://leetcode-cn.com/problemsreverse-nodes-in-k-group/)| 🔴️ | 链表 | 2 |迭代(引入dummy哑节点作为prev的初值)、递归|
| [20](https://leetcode.com/problems/valid-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)| 🟢 | 栈、队列 | 2 |字典、栈|
| [155](https://leetcode.com/problems/min-stack/discuss/?currentPage=1&orderBy=most_votes&query=) | [最小栈](https://leetcode-cn.com/problems/min-stack/)| 🟢  | 栈、队列 | 2 |借助辅助栈、值和min成对入栈|
| [84](https://leetcode.com/problemslargest-rectangle-in-histogram/discuss/?currentPage=1&orderBy=most_votes&query=) | [柱状图中最大的矩形](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/)| 🔴️ | 栈、队列 | 2 |栈、中间到两边搜索、边界确定|
| [239](https://leetcode.com/problems/sliding-window-maximum/discuss/?currentPage=1&orderBy=most_votes&query=) | [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/)| 🔴️ | 栈、队列 | 2 |双端队列、始终保持窗口内第一个元素是最大值|
| [146](https://leetcode.com/problems/lru-cache/discuss/?currentPage=1&orderBy=most_votes&query=) | [LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)| 🟡  | 链表 | - |哈希表+双向链表|





### 课后作业
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- |---|
| [66](https://leetcode.com/problems/plus-one/discuss/?currentPage=1&orderBy=most_votes&query=) | [加一](https://leetcode-cn.com/problems/plus-one/)| 🟢 | 数组、链表、跳表 | 2 |-|
| [1](https://leetcode.com/problems/two-sum/discuss/?currentPage=1&orderBy=most_votes&query=) | [两数之和](https://leetcode-cn.com/problems/two-sum/)| 🟢  | 数组、链表、跳表 | 2 |哈希|
| [283](https://leetcode.com/problems/move-zeroes/discuss/?currentPage=1&orderBy=most_votes&query=) | [移动零](https://leetcode-cn.com/problems/move-zeroes/)| 🟢  | 数组、链表、跳表 | 2 |双指针(空间优化)|
| [26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [删除排序数组中的重复项](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)| 🟢 | 数组、链表、跳表 | 2 |双指针|
| [189](https://leetcode.com/problems/rotate-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [旋转数组](https://leetcode-cn.com/problems/rotate-array/)| 🟢 | 数组、链表、跳表 | 2 | 三反转、环状替换|
| [21](https://leetcode.com/problems/merge-two-sorted-lists/discuss/?currentPage=1&orderBy=most_votes&query=) | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/)| 🟢 | 数组、链表、跳表 | 2 |递归、双指针迭代(引入dummy哑节点作为prev初始值)|
| [88](https://leetcode.com/problems/merge-sorted-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [合并两个有序数组](https://leetcode-cn.com/problems/merge-sorted-array/)| 🟢 简单 | 数组、链表、跳表 |  2 |双指针(从前往后、从后往前) |
| [641](https://leetcode.com/problems/design-circular-deque/discuss/?currentPage=1&orderBy=most_votes&query=) | [设计循环双端队列](https://leetcode-cn.com/problems/design-circular-deque/)| 🟡  | 栈、队列 | 2 |front：指向队列头；  rear：指向队列尾的下一个位置。为了避免“队列为空”和“队列为满”的判别条件冲突，有意浪费了一个位置
| [42](https://leetcode.com/problems/trapping-rain-water/discuss/?currentPage=1&orderBy=most_votes&query=) | [接雨水](https://leetcode-cn.com/problems/trapping-rain-water/)| 🔴️  | 栈、队列 | 2 |栈、中间向两边边界确定|
