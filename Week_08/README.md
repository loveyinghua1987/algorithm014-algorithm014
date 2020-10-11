学习笔记
本周主要学习内容：  
**位运算**

指定位置的位运算
1. 将x最右边的n位清零： x & (~0 << n)
2. 获取x的第n位值(0或者1)： (x >> n) & 1
3. 获取x的第n位的幂值： x & (1 << n)
4. 仅将第n位置为1： x | (1 << n)
5. 仅将第n位置为0： x & (~ (1 << n))
6. 将x最高位至第n位(含)清零： x & ((1 << n) - 1)

实战位运算要点(重点掌握)

- 判断奇偶 
  
  x % 2 == 1  --> (x & 1) == 1
  x % 2 == 0 --> (x & 1) == 0

  位运算比模快不少，建议以后判断奇偶性能用位运算就用位运算。

  当然，用java或其他高级语言，用左边模的形式，它的编译器足够智能，肯定也是转换成二进制的，不会傻傻得去模的。

- x >> 1  --> x // 2
  
  mid = (left + right) // 2  --> mid = (left + right) >> 1

- x & (x - 1) ：清除最低位的1
- x & -x ：得到最低位的1
- x & ~x ： 0

N 皇后位运算代码示例
```
# Python
def totalNQueens(self, n): 
	if n < 1: return [] 
	self.count = 0 
	self.DFS(n, 0, 0, 0, 0) 
	return self.count
def DFS(self, n, row, cols, pie, na): 
	# recursion terminator 
	if row >= n: 
		self.count += 1 
		return
	bits = (~(cols | pie | na)) & ((1 << n) — 1)  # 得到当前所有的空位
	while bits: 
		p = bits & —bits # 取到最低位的1
		bits = bits & (bits — 1) # 表示在p位置上放入皇后
		self.DFS(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1) 
        # 不需要revert  cols, pie, na 的状态
```

**布隆过滤器（Bloom Filter）**

bloom Filter vs Hash Table

- 一个很长的**二进制**向量和一系列**随机映射函数**。布隆过滤器可以用于检索一个元素是否在一个集合中。
- 和哈希表最大的一个区别：哈希表不仅可以判断它是否在集合中，同时还可以存元素本身和元素的各种额外信息。但是布隆过滤器只是用于检索一个元素的是否在还是不在，它只能存在和不在的信息，而不能存其他额外的信息。
- 优点：空间效率和查询效率都**远远超过**一般的算法  
  
    为什么远远高于一般算法？  

    一方面，它是用了二进制向量来表示，所以它很节省空间；另一个方面，它是一种模糊的查询方式。
- 缺点：有一定的误识别率和删除困难

布隆过滤器的原理：

对于任何一个元素，它会分配到一系列的二进制位中，把对应的位置置为1。


当布隆过滤器把元素全部都插入完之后，对于测试元素（新来的一个元素），要来验证它是否存在？

当它验证这个元素所对应的二进制位是1的时候，我们只能说它可能存在在布隆过滤器里面，但当这个元素所对应的二进制位，只要有一个不为1，我们可以百分之百肯定它不在。也就是说，这个元素取布隆过滤器里面查，如果查到它不在的话，那么它肯定就是不在的，如果查这个元素（比如：B）在布隆过滤器里面，它的二进制位都是1，为存在的一个状态的话，我们只能说它可能是存在的。

布隆过滤器只是放在最外面来当一个缓存使用的，也就是说来当一个很快速地判断使用的，当B查到之后，布隆过滤器里面是存在的，那么B就会继续在这台机器上的DB（data base），也就是说放在数据库里面去查，到时候会查出来B到底是不是存在的。查到不在布隆过滤器里面的，就会发现在这台机器的数据库里面肯定就不存在了，就不用查了，这样就节省下来访问数据库的时间了。

布隆过滤器只是挡在一台机器前面的快速查询的缓存，真正要确定这个元素一定存在的话，必须再访问这个机器里面的一个完整的存储数据结构，一般来说就是数据库了。

在工业上的应用：
1. 比特币网络
2. 分布式系统（Map-Reduce） - hadoop、search engine
3. Redis缓存
4. 垃圾邮件、评论等的过滤

搜索引擎经常做的很多事情，把大量的网页信息和图片信息都存在它的整个服务器里面。一般来说，不同的网页是存在不同的集群里面的，当我在search的时候，查到一个东西之后，它就会根据索引就会知道它应该是在这个集群，它就先在集群的布隆过滤器里面去查一下，看是否存在，如果存在的话，它再去集群的DB里面进行访问，如果不存在的话，就直接略过了，所以在大型分布式系统里面，很多在使用布隆过滤器。

```
# Python 
from bitarray import bitarray 
import mmh3 
class BloomFilter: 
	def __init__(self, size, hash_num): 
		self.size = size 
		self.hash_num = hash_num 
		self.bit_array = bitarray(size) 
		self.bit_array.setall(0) 
	def add(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			self.bit_array[result] = 1 
	def lookup(self, s): 
		for seed in range(self.hash_num): 
			result = mmh3.hash(s, seed) % self.size 
			if self.bit_array[result] == 0: 
				return "Nope" 
		return "Probably" 
bf = BloomFilter(500000, 7) 
bf.add("dantezhao") 
print (bf.lookup("dantezhao")) 
print (bf.lookup("yyj")) 
```

**LRU Cache**
- 两个要素：大小、替换策略
- HashTable + Double LinkedList
- O(1)查询
- O(1)修改、更新

替换策略
- LFU - least frequently used
- LRU - least recently used

替换算法总览：
https://en.wikipedia.org/wiki/Cache_replacement_policies

本质上它的替换算法和现在的推荐系统有异曲同工之妙。本质上，它的推荐算法就是根据之前的元素被使用的频次和使用的时间来预测新来的一个元素，它是某个老元素的概率是多少，这就类似于好像推荐系统里面的，我自己读了很多老的新闻，或者是我自己浏览了很多老的短视频，那么推荐系统就通过我之前看过的东西来给我推荐我可能会感兴趣的新的内容。所以，在现在的计算机里面替换算法就变得越来越使用人工智能来做，而不是这种简单的基于逻辑式的，很简单的这种公式的。

**排序算法**
1. 比较类排序
   通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也称为非线性时间比较类排序。  
   大部分用到的排序都属于比较类排序。
2. 非比较类排序
   不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。  
   缺点：一般来说只能用于整型相关的数据类型，也就是说对于一些比如说字符串的排序，或对象之间的排序就无能为力。同时它一般要辅助用额外的内存空间

排序算法  

- 比较类排序
  - 交换排序
    - 冒泡排序
    - 快速排序
  - 插入排序
    - 简单插入排序
    - 希尔排序
  - 选择排序
    - 简单选择排序
    - 堆排序
  - 归并排序
    - 二路归并排序
    - 多路归并排序
- 非比较类排序
  - 计数排序
  - 桶排序
  - 基数排序


**重点了解时间复杂度O(nlogn)的排序：（要求会手写出来）**

- **堆排序**
- **快速排序**（用到分治的思想）
- **归并排序**（用到分治的思想）

初级排序-O(n^2)
1. 选择排序(Selection Sort)
   每次找最小值，然后放到待排序数组的起始位置。
2. 插入排序(Insertion Sort)
   从前到后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
3. 冒泡排序(Bubble Sort)
   嵌套循环，每次查看相邻的元素，如果逆序，则交换

高级排序 -O(N*logN)
1. 快速排序(Quick Sort)
   数组取标杆pivot，将小元素放pivot左边，大元素放右侧，然后依次对右边和左边的子数组继续快排，以达到整个序列有序。
```
#Python

def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)
    
def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
```

2. 归并排序(Merge Sort) - 分治
  
	- 把长度为n的输入序列分成两个长度为n/2的子序列；
	- 对这两个子序列分别采用归并排序；
	- 将两个序列号的子序列合并成一个最终的排序序列
```
#Python

def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
```

总结：
归并和快排具有相似性，但步骤顺序相反

归并：先排序左右子数组，然后合并两个有序数组

快排：先调配出左右子数组，然后对于左右子数组进行排序

3. 堆排序(Heap Sort) - 堆插入O(logN)，取最大/小值O(1)
  
  - 数组元素一次建立小顶堆
  - 依次取堆元素，并删除
  
```
#Python

def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)

```

特殊排序- O(n) (了解即可)
1. 计数排序(Counting Sort)
   计数排序要求输入的数据必须有确定范围的整数。将输入的数据值转化为键存储在额外开辟的数组空间中；然后依次把计数大于1的填充回原数组。
2. 桶排序(Bucket Sort)
   桶排序的工作原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序(有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序)
3. 基数排序(Radix Sort)
   基数排序时按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。

## 第八周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [191](https://leetcode.com/problems/number-of-1-bits/discuss/?currentPage=1&orderBy=most_votes&query=) | [ 位1的个数](https://leetcode-cn.com/problems/number-of-1-bits/)| 🟢| 位运算 | 1 ||
| [231](https://leetcode.com/problems/power-of-two/discuss/?currentPage=1&orderBy=most_votes&query=) | [2的幂](https://leetcode-cn.com/problems/power-of-two/)| 🟢| 位运算 | 1 ||
| [190](https://leetcode.com/problems/reverse-bits/discuss/?currentPage=1&orderBy=most_votes&query=) | [颠倒二进制位](https://leetcode-cn.com/problems/reverse-bits/)| 🟢| 位运算 | 1 ||
| [51](https://leetcode.com/problems/n-queens/discuss/?currentPage=1&orderBy=most_votes&query=) | [N 皇后](https://leetcode-cn.com/problems/n-queens/)| 🔴️| 位运算 | 1 ||
| [52](https://leetcode.com/problems/n-queens-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/)| 🔴️| 位运算 | 1 ||
| [338](https://leetcode.com/problems/counting-bits/discuss/?currentPage=1&orderBy=most_votes&query=) | [比特位计数](https://leetcode-cn.com/problems/counting-bits/)| 🟡| 位运算 | 1 ||
| [146](https://leetcode.com/problems/lru-cache/discuss/?currentPage=1&orderBy=most_votes&query=) | [LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)| 🟡| LRU Cache | 1 ||
| [1122](https://leetcode.com/problems/relative-sort-array/discuss/?currentPage=1&orderBy=most_votes&query=) | [数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array/)| 🟢| 排序算法 | 1 ||
| [242](https://leetcode.com/problems/valid-anagram/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的字母异位词](https://leetcode-cn.com/problems/valid-anagram/)| 🟢| 排序算法 | 1 ||
| [56](https://leetcode.com/problems/merge-intervals/discuss/?currentPage=1&orderBy=most_votes&query=) | [合并区间](https://leetcode-cn.com/problems/merge-intervals/)| 🟡| 排序算法 | 1 |排序+一次扫描|
| [493](https://leetcode.com/problems/reverse-pairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [翻转对](https://leetcode-cn.com/problems/reverse-pairs/)| 🔴️| 排序算法 | 1 |归并排序|