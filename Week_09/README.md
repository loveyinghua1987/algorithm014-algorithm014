学习笔记
本周主要学习内容： 
一、**高级动态规划**
1. 动态规划复习；附带递归、分治

- 递归、分治、回溯、动态规划复习
    
  (1) **递归：函数自己调用自己**。

  递归和分治、回溯其实没有一个所谓是A就不是B之间的关系，它其实就是定义一个问题的不同方面。本身它的函数调用是自己调用自己的话，我们就可以叫做递归。  

  递归代码模板：
    ```
    # Python
    def recursion(level, param1, param2, ...): 
        # recursion terminator 
        if level > MAX_LEVEL: 
        process_result 
        return 
        # process logic in current level 
        process(level, data...) 
        # drill down 
        self.recursion(level + 1, p1, ...) 
        # reverse the current level status if needed
    ```
    (2)**分治：分而治之**
    它用不用递归，它肯定要用递归，当然你也可以不写出递归的程序，让它分而治之也是行的，如果你是强行起循环的话也是可以的，但是从计算机本身设计的语言角度来说，绝大部分用递归来写是非常自然的。就是做分治，还是要改变自己的思维习惯，就是切换成机器，或者是程序编程语言的思维，也就是说递归经常要用。  
    
    分治代码模板：
    ```
    # Python
    def divide_conquer(problem, param1, param2, ...): 
    # recursion terminator 
    if problem is None: 
        print_result 
        return 

    # prepare data 
    data = prepare_data(problem) 
    subproblems = split_problem(problem, data) 

    # conquer subproblems 
    subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
    subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
    subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
    …

    # process and generate the final result 
    result = process_result(subresult1, subresult2, subresult3, …)
        
    # revert the current level states
    ```
    分治本身的代码模板套用之前的递归代码部分，先是递归终止条件，然后是准备数据和拆分问题，同时每一个子问题都调分治函数进行递归求解，最后得到一些中间的结果，中间的结果最终合并起来，合并完了之后返回。

    上一节的快速排序和归并排序就是这么一个结构，以归并排序为例，归并排序就是一个典型的分而治之，把一个数组劈成两半，左边部分先排好序，右边部分再排好序的情况下，然后把它们进行merge，merge的过程最后可以让整个数组变得有序。这就是所谓归并排序的思想。

    **感触**
    (1) 人肉递归低效、很累  
    (2) 找到最近最简方法，将其拆分成可重复解决的问题
  
    - 最近重复性的理解：你就想象成是最大公约数就好了。如果你拆得非常小的时候，这时候你会发现你的递归的话就是非常累，因为你的程序会写得特别繁琐，这个时候就要找那种最大公约数的关系。
    (3) 数学归纳法

    - 这点其实是比较反人类的，因为很多时候人的思维习惯，在现实中就比较希望把每一个步骤，自己都能够看到和把控住，不然你心里面没底，一般你很难会觉得你只要把你的下一层管好，同时再制定整个制度，让下一层再把下一层管好，最后整个体系就是完美的，一般不适合于这样的思想，但是你要处理复杂的问题，或者在复杂的公司里面工作，或者在复杂的社会里面要工作的话，都是要用这样的一种管理的方式，也就是同理可得的方式，那么还是这样自己慢慢来习惯这样的一种思维习惯。

    **本质：寻找重复性 --> 计算机指令集**

    - 为什么寻找重复性？
        因为任何一个复杂问题，最后在面试中一般来说不超过十行，最为复杂的问题也不超过二十行到三十行。把这么复杂的问题，你要用计算机指令，在十行二十行的程序能够完成的话，说明它肯定是有重复性的，那么这个重复性最后就反映在代码指令集上面的话，肯定就是for循环，或者是while循环，或者是递归调用，那么最后的本质就是寻找重复性。

      

    从分治的递归状态树，引申到动态规划，动态规划和分治其实没有非常显著或者本质上的区别。但是，很多时候，当我们发现分治的问题，它本身的子问题具有所有的重叠，或者是所谓的最优子结构的时候，这个时候我们就会发现，很多时候我们就可以去重或者是淘汰次优解。那么在这种情况下，这种分治的方法，你能够在中间每一步淘汰次优解的话，就变成了所谓的动态规划。
    举例：从Fibnacci的状态数，可以看到右很多重复的计算，当我们发现有重复的问题，加了一个缓存进去的话，也就是分治再加上记忆化的缓存的话，这个时候我们就可以认为已经从分治过渡到所谓的动态规划了。

    (3) **动态规划Dynamic Programming**

    a. "Simplifying a complicated problem by breaking it down into simpler sub-problems"(in a recursive manner) 

    b. Divide & Conquer + Optimal substructure
        分治 + 最优子结构

    c. 顺推形式：动态递推

    初学者可以从分治的角度加上记忆化搜索来开始切入动态规划的题目，然后再转为递推的问题，这样你会觉得思维习惯上比较顺畅。如果内动练得越来越多的时候，建议直接从递推开始，因为大部分的动态规划，最后肯定是递推的程序是最为简化的，也是符合动态规划整体思想的。


    DP顺推模板
    ```
    def DP():
        dp = [][] #二维情况

        for i in  range(M + 1):
            for j in range(N + 1):
                dp[i][j] = _Function(dp[i'][j'] ...)
        reutrn dp[M][N]
    ```
    
    由此可见，本身的话就是一个嵌套的循环，然后从之前的dp的状态，推到最新的dp[i][j]的状态，最后还有dp[M][N]反映最后的最终结果。还可以看到一点，本身模板并不复杂，复杂在什么地方？第一个复杂的地方就是DP状态的定义，状态的定义需要你的经验，同时需要你把现实的问题定义成一个数组，里面保存状态，这个数组可能是一维的，两维的，三维的都有可能；第二个复杂的地方毋庸置疑就是这个状态转移方程要怎么写，很多时候，很简化的情况就是Fibonacci数列直接把dp[i-1]加上dp[i-2]就等于dp[i]，但是更多的情况下，我们会求一个最小值，或者是我们可以累加累减，或者是在这里面有一层小的循环，从之前的k个状态里面找到它的最值放到这个地方。

**关键点**
- 动态规划和递归或者分治没有根本上的区别(关键看有无最优的子结构)
- 拥有共性：找重复子问题

    - 都是找重复子问题，然后化繁为简，庖丁解牛地把一个大的问题分解成各个重复的子问题
- **差异性：最优子结构、中途可以淘汰次优解**

    - 动态规划用来处理，有所谓中间的重复性以及所谓的最优子结构，在中途可以淘汰次优解。

2. **常见的DP题目和状态方程**
   
    **爬楼梯**

    递归公式：
    f(n) = f(n - 1) + f(n - 2) ,    f(1) = 1, f(0) = 0

    ```
    #最朴素的递归
    def f(n):                            O(2^n)
        if n <= 1: return 1 
        return f(n - 1) + f(n - 2) 
    #分治里面直接加记忆化搜索，用一个mem的数组缓存存储起来  
    def f(n):                            O(n)
        if n <= 1: return 1 
        if n not in mem: 
            mem[n] = f(n - 1) + f(n - 2) 
        return mem[n]

    #把递归转换成顺推的一种形式
    def f(n):                            O(n)
        dp = [1] * (n + 1) 
        for i in range(2, n + 1): 
            dp[i] = dp[i - 1] + dp[i - 2] 
        return dp[n]

    #内存上的小优化，将空间复杂度优化为O(1)
    def f(n):                          O(n), O(1)  
        x, y = 1, 1 
        for i in range(1, n): 
            y, x = x + y, y 
        return y
    ```
    第一点，爬楼梯问题本质上可以转化为Fibonacci问题  

    第二点：爬楼梯问题和硬币置换问题有异曲同工之处

    **不同路径**

    递归公式：
    f(x, y) = f(x-1, y) + f(x, y-1)

    ```
    def f(x, y):                        #指数级的时间复杂度
        if x <= 0 or y <= 0: return 0     
        if x == 1 and y == 1: return 1 
        return f(x - 1, y) + f(x, y - 1) 
        
    def f(x, y):                          O(mn)，O(mn)
        if x <= 0 or y <= 0: return 0 
        if x == 1 and y == 1: return 1 
        if (x, y) not in mem: 
            mem[(x, y)] = f(x - 1, y) + f(x, y - 1)
        return mem[(x, y)]

    def f(x, y):                          O(mn)，O(mn)
        dp = [[0] * (m + 1) for _ in range(n + 1)] 
        dp[1][1] = 1 
        for i in range(1, y + 1): 
            for j in range(1, x + 1): 
                dp[i][j] = dp[i - 1][j] + dp[j][i - 1] 
        return dp[y][x]

    #不同路径2
    def f(x, y):                          O(mn)，O(mn)

        m = len(obstacleGrid)
        if not m: return 0
        n = len(obstacleGrid[0])
        if not n: return 1

        dp = [[0] * (m + 1) for _ in range(n + 1)] 

        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1

        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1

        for i in range(1, y + 1): 
            for j in range(1, x + 1): 
                obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[j][i - 1] 
        return dp[y][x]
    ```
    **打家劫舍**

    dp[i]状态的定义： max $ of robbing A[0 -> i] 
    dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])


    dp[i][0]状态定义：max $ of robbing A[0 -> i] 且没偷 nums[i] 
    dp[i][1]状态定义：max $ of robbing A[0 -> i] 且偷了 nums[i]
    dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]); 
    dp[i][1] = dp[i - 1][0] + nums[i];

    **最小路径和**

    dp[i][j]状态的定义： minPath(A[1 -> i][1 -> j])
    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + A[i][j]

    **股票买卖**
    股票买卖
    dp[i][k][0 or 1] (0 <= i <= n-1, 1 <= k <= K) 
    •i 为天数 
    •k 为最多交易次数 
    •[0,1] 为是否持有股票 
    总状态数： n * K * 2 种状态
    ```
    for 0 <= i < n:    
        for 1 <= k <= K:        
            for s in {0, 1}:            
                dp[i][k][s] = max(buy, sell, rest)
    ```

        
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])              
                    max(   选择 rest  ,           选择 sell      )
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])              
                    max(   选择 rest  ,           选择 buy         )
        
    解释：今天我没有持有股票，有两种可能：
    - 我昨天就没有持有，然后今天选择 rest，所以我今天还是没有持有；
    - 我昨天持有股票，但是今天我 sell 了，所以我今天没有持有股票了。
    解释：今天我持有着股票，有两种可能：
    - 我昨天就持有着股票，然后今天选择 rest，所以我今天还持有着股票；
    - 我昨天本没有持有，但今天我选择 buy，所以今天我就持有股票了。

    ```
    dp[-1][k][0] = dp[i][0][0] = 0 
    dp[-1][k][1] = dp[i][0][1] = -infinity

    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i]) 
    dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - price)
    ```

    2、**高阶的 DP 问题**
        
    1. 复杂度来源
    - 状态拥有更多维度（二维、三维、或者更多、甚至需要压缩）
        
        - DP本质：第一，状态的定义；第二，状态转移方程。复杂度也同理可得，状态拥有更多的维度，这是它的复杂度来源一，这就意味着：第一，你的数组变成二维三维了，每一个维度是什么？你必须更加的清晰，且在写的时候不能逻辑出错或者是混乱。第二，也说明了你要从现实问题，也就是你从面试题本身能抽象出来不同维度如何定义，对你的逻辑思维要求能力肯定也会更高，有些时候它的状态空间会变得特别的大，就导致循环变慢，这个时候你还要考虑所谓的压缩状态，简单的压缩状态就犹如Fibonacci问题，我们不用存整个一维的数组，我们只需要存两个变量，也就是它的前一者和再前一者。同理可得，在更复杂的问题，它的压缩状态会更加复杂。
    - 状态方程更加复杂

        - 状态转移方程更难，一方面是题目本身的逻辑关系很难，另外一个方面是由于状态空间的维度太多，也会导致状态转移方程本身也变难，所以在这里要如何提高就是一点：多练，多思考，也就是内功。

    **本质：内功、逻辑思维、数学**

    当碰到一个问题的话，就认真去思考一下这个状态应该怎么定义，如果一维不行的话，马上想到升一维，变成二维来解决，如果二维都不行的话，想想是不是变成三维。
    
    (1). 爬楼梯问题改进
    - 1、2、3
    
        - f(n) = f(n - 1) + f(n - 2) + f(n-3) ,    f(1) = 1, f(0) = 0

    - x1, x2, …, xm 步

        - f(n) += f(n-x[j])
    
    -  前后不能走相同的步伐

        - f(n, k) += f(n-x[k]，x[i]) for i in range(1, m) and i != k
        - 这个时候一维不够用，需要增加到二维，
        - n：表示我上了多少级台阶
        - k：表示当前这步我走了几步的下标
    

    (2). 编辑距离
        dp[i][j]: word1.substr(0, i) 与word2.substr(0, j)之间的编辑距离
        

        if word1[i] ==  word2[j]:
            dp[i][j] = dp[i-1][j-1]   
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
             
    • 如果 word1[i] 与 word2[j] 相同，显然 dp[i][j]=dp[i-1][j-1]
    • 如果 word1[i] 与 word2[j] 不同，那么 dp[i][j] 可以通过        
        1. 在 dp[i-1][j-1] 的基础上做 replace 操作达到目的        
        2. 在 dp[i-1][j] 的基础上做 insert 操作达到目的
        3. 在 dp[i][j-1] 的基础上做 delete 操作达到目的 
        取三者最小情况即可

二、字符串算法
    最重要的是：在字符串里面如何运用算法和其他的数据结构来解决各种问题，字符串本身在面试的时候出的比较频繁，所以这一章节也是比较重要的，同时会和前面的递归以及动态规划相结合，所以要反复对这一章节的题目进行练习，都是很重要的题目。
1. 字符串基础知识
**字符串**

- python
  ```
  x = 'abbc'
  x = "abbc"
  ```
- Java:
  ```
  String x = "abbc"
  ```
- C++:
  ```
  string x( "abbc" )
  ```

  注意：Python和Java的string是immutable的，immutable指的是不可变的，也就是说你定义了这个String之后，它就是不可变的，当你把它加一个字母或者减一个字母的话，它其实是新生成了一个String，原来的String还是原来的内容。C++的话，它是可变的，把这一点一定要记清楚。所以，不管你用Python还是Java的话，你每次改变String里面的内容的话，其实你都是创建了一个新的String，immutable的话有好处，就是说它是线程安全的，可变的话就会有可能在多线程的环境里面，有一些问题，同时最关键的是下面这篇文章：

  string immutable:
  https://lemire.me/blog/2017/07/07/are-your-strings-immutable/

  记住下面这部分内容：
  In Java, C#, JavaScript, Python and Go, strings are immutable. Furthermore, Java, C#, JavaScript and Go have the notion of a constant: a “variable” that cannot be reassigned. (I am unsure how well constants are implemented and supported in JavaScript, however.)

  In Ruby and PHP, strings are mutable.

  The C language does not really have string objects per se. However, we commonly represent strings as a pointer char *. In general, C strings are mutable. The C++ language has its own string class. It is mutable.
  In both C and C++, string constants (declared with the const qualifier) are immutable, but you can easily “cast away” the const qualifier, so the immutability is weakly enforced.

  In Swift, strings are mutable.
  However, if you declare a string to be a constant (keyword let), then it is immutable.

  关于可变和不可变的性质，有可能在面试的时候面试官会问你，所以一定要弄清楚


  **遍历字符串**
  String最常用的就是：遍历String里面的每一个字符。

- Python：
  ```
  for ch in "abbc":
      print(ch)
  ```

- Java:
  ```
  String x = "abbc"
  for(int i = 0; i < x.size(); ++i){
      char ch = x.charAt(i);
  }
  for ch in x.toCharArray() {
      System.out.println(ch);
  }
  ```
- C++:
  ```
  string x( "abbc" );
  for(int i = 0; i < s1.length(); i++){
      cout<<x[i];
  }
  ```
  **字符串比较**
  在比较字符串这块，特别是Java，以及Python和JavaScript里面也有相应的问题，就是如果在Java里面x==y的话，它是比较它们的指针，比较它们的reference的地址，而不是比较字符串里的内容。
  Java:
  ```
    String x = new String(“abb”);
    String y = new String(“abb”);
    x == y —-> false
    x.equals(y) —-> true
    x.equalsIgnoreCase(y) —-> true
  ```

   字符串转换整数 (atoi)[https://leetcode-cn.com/problems/string-to-integer-atoi/]

   ```
   # Python
    class Solution(object):
        def myAtoi(self, s):
            if len(s) == 0 : return 0
            ls = list(s.strip())
            
            sign = -1 if ls[0] == '-' else 1
            if ls[0] in ['-','+'] : del ls[0]
            ret, i = 0, 0
            while i < len(ls) and ls[i].isdigit() :
                ret = ret*10 + ord(ls[i]) - ord('0')
                i += 1
            return max(-2**31, min(sign * ret,2**31-1))
   ```

2. 高级字符串算法
    **最长子串、子序列**

    子序列和子串的区别：子序列可以有间隔的，而子串没有。

    a. Longest common sequence (最长子序列)
    https://leetcode-cn.com/problems/longest-common-subsequence/

    ```
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1 
    else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    ```

    b. Longest common substring (最长子串)

    ```
    if s1[i-1] == s2[j-1]:
        dp[i][j] = dp[i-1][j-1] + 1 
    else:
        dp[i][j] = 0
    ```

    c. Edit distance (编辑距离)
    https://leetcode-cn.com/problems/edit-distance/

    ```
   
    if word1[i] ==  word2[j]:
        dp[i][j] = dp[i-1][j-1]   
    else:
        dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    ```

    最长回文子串[https://leetcode-cn.com/problems/longest-palindromic-substring/]
    method1: 暴力 O(n^3)
    method2: 中间向两边扩张法 O(n^2)
    method3: 动态规划

    首先定义P(i,j):
    ```
              true  s[i, j] 是回文串
    P(i, j) =
              false  s[i, j] 不是回文串
    ```
    
    接下来：
    P(i, j) = P(i + 1, j - 1) && s[i] == s[j]

    正则表达式匹配[https://leetcode-cn.com/problems/regular-expression-matching/]

    ```
    def isMatch(text, pattern) -> bool:
        if not pattern: return not text
        first_match = bool(text) and pattern[0] in {text[0], '.'}
        if len(pattern) >=2 and pattern[1] == '*':
            #发现'*'通配符
            return isMatch(text, pattern[2:]) or first_match and isMatch(text[1:], pattern)
            #解释：如果发现字符和'*'结合，
            #或者匹配该字符0次，然后跳过该字符和'*'
            #或者当pattern[0]和text[0]和pattern[0]匹配后，移动text
        else:
            return first_match and isMatch(text[1:], pattern[1:])
    ```
    
    
    不同的子序列[https://leetcode-cn.com/problems/distinct-subsequences/]

    a. 暴力递归
    b. 动态规划

    dp[i][j]代表T前i字符串可以由S前j字符串组成最多匹配子序列的个数

    所以动态方程：

    当S[j] == T[i], dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

    当S[j] != T[i], dp[i][j] = dp[i][j-1]

 
3. 字符串匹配算法
   这部分重点要求理解
   (1) 暴力法(brute force) - O(mn)
   (2) Rabin-Krap算法
   (3) KMP算法
  
  - 课后了解：
    Boyer-Moore算法：
    https://www.ruanyifeng.com/blog/2013/05/boyer-moore_string_search_algorithm.html
    Sunday算法：
    https://blog.csdn.net/u012505432/article/details/52210975

    字符串匹配暴力法代码示例：
    ```
    # Python
    def forceSearch(txt, pat):
        n, m = len(txt), len(pat)
        for i in range(n-m+1):
            for j in range(m):
                if txt[i+j] != pat[j]:
                    break
                if j == m:
                    return i
        return -1 
    ```

    **Rabin-Karp算法**
    在朴素算法中，我们需要挨个比较所有字符，才知道目标字符串中是否包含子串。那么，是否有别的方法可以用来判断目标字符串是否包含子串呢？

    答案是肯定的，确实存在一种更快的方法。为了避免挨个字符对目标字符串和子串进行比较，我们可以尝试一次性判断两者是否相等。因此，我们需要一个好的哈希函数(hash function)。通过哈希函数，我们可以算出子串的哈希值，然后将它和目标字符串中的子串的哈希值进行比较。这个新方法在速度上比暴力法有显著提升。

    Rabin-Karp算法的思想：
    1. 假设子串的长度为M(pat), 目标字符串的长度为N(txt)
    2. 计算子串的hash值hash_pat
    3. 计算目标字符串txt中每个长度为M的子串的hash值(共需要计算N-M+1)
    4. 比较hash值：如果hash值不同，字符串必然不匹配；如果hash值相同，还需要使用朴素算法再次判断。

    ```
    Python
    class Solution:
        def strStr(self, haystack: str, needle: str) -> int:
            d = 256
            q = 9997
            n = len(haystack)
            m = len(needle)
            h = pow(d,m-1)%q
            p = 0
            t = 0
            if m > n:
                return -1
            for i in range(m): # preprocessing
                p = (d*p+ord(needle[i]))%q
                t = (d*t+ord(haystack[i]))%q
            for s in range(n-m+1): # note the +1
                if p == t: # check character by character
                    match = True
                    for i in range(m):
                        if needle[i] != haystack[s+i]:
                            match = False
                            break
                    if match:
                        return s
                if s < n-m:
                    t = (t-h*ord(haystack[s]))%q
                    t = (t*d+ord(haystack[s+m]))%q
                    t = (t+q)%q
            return -1
    ```

    **KMP算法**

    KMP算法(Knuth-Morris-Pratt)的思想就是，当子串与目标字符串不匹配时，其实你已经知道了前面已经匹配成功那一部分的字符(包括子串与目标字符串)。以阮一峰的文章为例，当空格与D不匹配时，你其实知道前面六个字符是"ABCDAB"。KMP算法的想法是，设法利用这个已知信息，不要把"搜索位置"移回已经比较过的位置，继续把它向后移，这样就提高了效率。

    https://www.bilibili.com/video/av11866460?from=search&seid=17425875345653862171

    http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html



