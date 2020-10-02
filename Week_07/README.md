学习笔记
本周主要学习内容：  

**字典树**
Trie 树代码模板 
```
# Python 
class Trie(object):
  
	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True
```

**并查集**
并查集代码模板
```
# Python 
def init(p): 
	# for i = 0 .. n: p[i] = i; 
	p = [i for i in range(n)] 
 
def union(self, p, i, j): 
	p1 = self.parent(p, i) 
	p2 = self.parent(p, j) 
	p[p1] = p2 
 
def parent(self, p, i): 
	root = i 
	while p[root] != root: 
		root = p[root] 
	while p[i] != i: # 路径压缩 
		x = i; i = p[i]; p[x] = root 
	return root
```
**高级搜索**
(1) **双向BFS模板**
\#行的代码都是可以根据实际情况进行相应修改

```
import string
class Solution:
    def bidirectionBFS(self, begin: str, end: str,
                     wList: List[str]) -> int:
        if not List or end not in List: return 0
        wSet = set(wList)
        beginSet, endSet = {begin}, {end}
        #dis = 1

        while beginSet:
            #dis += 1
            nxt_beginSet = set()
            for w in beginSet:
                #for i in range(len(begin)):
                #    for c in string.ascii_lowercase:
                #        if c != w[i]:
                #            nxt = w[:i] + c + w[i + 1:]
                            if nxt in endSet:
                #                return dis
                            if nxt in wSet:
                                nxt_beginSet.add(nxt)
                                wSet.remove(nxt)
            beginSet = nxt_beginSet
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
        return 0
```
(2)**启发式搜索**
 A*代码模板
```
# Python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue() # 优先级 —> 估价函数
	pq.append([start]) 
	visited.add(start)
	while pq: 
		node = pq.pop() # can we add more intelligence here ?
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
   unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```
**红黑树和AVL树**
树和链表没有本质上的区别，当一个链表分出两个next，我们可以认为它是树。所以，它的数据结构本质，是从一维空间扩散到二维空间了。这种扩散的好处是什么呢？就是引入了二叉搜索树，当它本身是有序的话，那么每一次的话就可以根据它和当前结点的大小的关系分出来它只走左分支还是只走右分支，这样的话查询插入和搜索的效率就从O(n)的变成了log2n的时间复杂度。
极端情况：
在你维护二叉搜索树的时候，没有特殊处理的话，在极端情况下，它会变成一根棍子，这根棍子就是你在插入的时候始终插在左边或右边，当这根棍子出现的时候，这个二叉搜索树就退化成一个链表了，就类似于链表的查询的时间复杂度了，所以要保证性能的关键就是要保证二维的维度，也就是左右子树高度尽量是平衡的，且左右子树以此类推下去都尽量是平衡的。所以，这里引入了一个叫平衡二叉树这样的一个概念。
*保证性能的关键*
1. 保证二维维度！ -> 左右子树结点平衡（recursively）
2. Balanced
3. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

所有的平衡二叉树有很多种，在面试的时候一般喜欢出AVL和红黑树，以及比如说treap以及splay叫伸展树，以及后面的话，还有B+树和二三树，主要在数据库的索引结构里面用得很多，但是它整个平衡二叉树有很多。二三树、AVL树和B+树一定要了解，如果对自己要求高的，Splay tree和Treap相对也要比较了解。

如何保证一棵树的平衡？
在真正的自平衡二叉树（红黑树和AVL树），不会等到这个树已经病入膏肓，就是已经变成很极端的这根棍子的时候，再去平衡，而是在每一步进行插入或者删除操作的时候，我们都去判断它是否平衡，以及将它维护成平衡二叉树的状态。

AVL树
1. 发明者G.M.Adelson-Velsky和EvgeniiLandis
2. Balance Factor(平衡因子)
   是它的左子树的高度减去它的右子树的高度（有时相反）。
   balance factor = {-1， 0， 1}
注意：这里是高度，因为查询二叉搜索树查询效率只与高度有关，和它的结点个数是没有关系的。
3. 通过旋转操作来进行平衡（四种）
   1. 左旋
   2. 右旋
   3. 左右旋
   4. 右左旋
   5. 带有子树的旋转（看图）
4. https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree

为什么会出来AVL？平衡因子是怎么定的？
平衡因子定的由来就是：它的查询的时间复杂度是等于树的深度，所以它就会记录深度差，就得到平衡因子。平衡因子不平衡的时候要怎么办？去旋转操作，就会变成这四种基础的旋转：左旋、右旋、左右旋、右左旋，基于树的形态就这四种，然后树的形态本身带有子树的情况下的话，就按照图来，基本就掌握了整个AVL。
关于代码怎么写？不要求，面试的时候没有人写得出来，可以不用去看代码。

AVL总结
1. 平衡二叉搜索树
2. 每个结点存balance factor = {-1， 0， 1}
3. 四种旋转操作
   
不足：结点需要存储额外信息、且调整次数频繁

你稍微动它一个结点或者两个结点，有时候就要触发一次平衡，正是因为这样，它调整得有点多，导致这个树的维护成本偏高。有些时候，我们其实并不要求它高度差差-1或1，超过-1或者比如说2，-2就要调，因为有些时候我们可能会认为-1和-2还能够接受，-3和-4有时候也可能接受，那么我们就调得少一点，因为你调那些结点的话本身也要费操作的。正是因为这个原因，就会引入其他的一些树，这些树我们就叫做近似平衡二叉树。所谓叫近似平衡二叉树就是不需要每次非常严格地来平衡。你会发现近似平衡二叉树它整个都是一些取舍(tradeoff)，当你觉得另外一种好的话，它可能是在其他地方有所这种妥协(compromise)。

**红黑树Red-black Tree**
红黑树是一种近似平衡的二叉搜索树(Binary Search Tree)，它能够确保任何一个结点的左右子树的高度差小于两倍。
具体来说，红黑树是满足如下条件的二叉搜索树：

- 每个结点要么是红色，要么是黑色
- 根结点是黑色
- 每个叶结点（NIL结点，空结点）是黑色的
- 不能有相邻接的两个红色结点
- 从任一结点到其每个叶子的所有路径都包含相同数目的黑色结点

宽度更广了，这样导致的一个好处就是：它旋转的频次降低，维护这个二叉树花的时间更少，它的总体的性能更好。

通过最后两点关系，可以证明它的高度差是小于两倍的。
这个性质可以证明在这种近似平衡的状态下，它的时间复杂度平均来说还是很好的logn的时间复杂度，它不会进行所谓的退化，而它所需要的的调整时间也是折中了之后相对比较小的调整时间。

关键性质：
从根到叶子的最长的可能路径不多于最短的可能路径的两倍长。

正是因为它有这个关系，所以会发现通过这5个性质就可以保证这一点。

**AVL树与红黑树对比**

- AVL Trees provide **faster lookups** than Red Black Trees because they are **more strictly balanced**.
- Red Black Trees provide **faster insertion and removal** operations than AVL trees as fewer rotations are done due to relatively relaxed balancing.
- AVL trees store balance **factors or heights** with each node, thus requires storage for an integer per node whereas Red Black Tree requires only 1 bit of information per node.
- Red Black Trees are used in most of the **language libraries like map, multimap, multisetin C++** whereas AVL Trees are used in **databases** where faster retrievals are required.

如果在读操作非常非常多，写操作很少的时候，就用AVL就好了。AVL的问题就是插入删除调整得比较频繁，但它的好处是非常平衡，所以查询很快。
如果这个东西插入操作也比较多，或者插入操作和查询操作一半一半的话，一般来说使用红黑树，因为红黑树比较简洁，比较好实现。
一般来说，红黑树是用在我们常常写的一些高级语言的库里面，比如写Java或写C++的那些map，set，全部用的都是红黑树，在DB里面的话，一般来说DB读会比较多，写会比较少，Databases里面一般是用AVL。

## 第七周
### 实战
🟢Easy  🟡Middle  🔴️Hard
| Leetcode | 名称 | 难度 | 分类 | 刷题次数 |备注|
| --- | --- | --- | --- | --- | ---|
| [102](https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/?currentPage=1&orderBy=most_votes&query=) | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/)| 🟡|  | 1 ||
| [208](https://leetcode.com/problems/implement-trie-prefix-tree/discuss/?currentPage=1&orderBy=most_votes&query=) | [实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)| 🟡| 字典树 | 1 ||
| [212](https://leetcode.com/problems/word-search-ii/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)| 🔴️| 字典树 | 1 ||
| [547](https://leetcode.com/problems/friend-circles/discuss/?currentPage=1&orderBy=most_votes&query=) | [朋友圈](https://leetcode-cn.com/problems/friend-circles/)| 🟡| 并查集 | 1 ||
| [200](https://leetcode.com/problems/number-of-islands/discuss/?currentPage=1&orderBy=most_votes&query=) | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)| 🟡| 并查集  | 1 ||
| [130](https://leetcode.com/problems/surrounded-regions/discuss/?currentPage=1&orderBy=most_votes&query=) | [被围绕的区域](https://leetcode-cn.com/problems/surrounded-regions/)| 🟡|  并查集 | 1 ||
| [70](https://leetcode.com/problems/climbing-stairs/discuss/?currentPage=1&orderBy=most_votes&query=) | [爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)| 🟢| 递归+去重 | 1 ||
| [22](https://leetcode.com/problems/generate-parentheses/discuss/?currentPage=1&orderBy=most_votes&query=) | [括号生成](https://leetcode-cn.com/problems/generate-parentheses/)| 🟡| 回溯+剪枝 | 1 ||
| [51](https://leetcode.com/problems/n-queens/discuss/?currentPage=1&orderBy=most_votes&query=) | [N 皇后](https://leetcode-cn.com/problems/n-queens/)| 🔴️| 回溯+剪枝 | 1 ||
| [36](https://leetcode.com/problems/valid-sudoku/discuss/?currentPage=1&orderBy=most_votes&query=) | [有效的数独](https://leetcode-cn.com/problems/valid-sudoku/)| 🟡|  | 1 ||
| [37](https://leetcode.com/problems/sudoku-solver/discuss/?currentPage=1&orderBy=most_votes&query=) | [解数独](https://leetcode-cn.com/problems/sudoku-solver/)| 🔴️| 回溯+剪枝 | 1 ||
| [127](https://leetcode.com/problems/word-ladder/discuss/?currentPage=1&orderBy=most_votes&query=) | [单词接龙](https://leetcode-cn.com/problems/word-ladder/)| 🟡| 双向BFS | 1 ||
| [433](https://leetcode.com/problems/minimum-genetic-mutation/discuss/?currentPage=1&orderBy=most_votes&query=) | [最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/)| 🟡| 双向BFS | 1 ||
