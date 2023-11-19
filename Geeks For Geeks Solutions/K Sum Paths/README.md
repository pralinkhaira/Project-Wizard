<h2><a href="https://www.geeksforgeeks.org/problems/k-sum-paths/1">K Sum Paths</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a binary tree and an integer <strong>K</strong>. Find the number of paths in the tree which have their sum equal to K.<br></span><span style="font-size: 18px;">A path may start from any node and end at any node in the <strong>downward </strong>direction. <br>Since the answer may be very large, compute it modulo <strong>10<sup>9</sup>+7</strong>.<br></span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:      </strong>
Tree = 
          1                               
        /   \                          
       2     3</span>
<span style="font-size: 18px;">K = 3</span>
<span style="font-size: 18px;"><strong>Output:</strong> <br>2</span>
<span style="font-size: 18px;"><strong>Explanation:</strong>
Path 1 : 1 + 2 = 3
Path 2 : only leaf node 3</span>
</pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input: </strong>
Tree = 
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6    
K = 5                    
<strong>Output:</strong> <br>8</span>
<span style="font-size: 18px;"><strong>Explanation:</strong>
The following paths sum to K.  
3 2 
3 1 1 
1 3 1 
4 1 
1 -1 4 1 
-1 4 2 
5 
1 -1 5 </span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong> &nbsp;<br>You don't need to read input or print anything. Complete the function <strong>sumK()</strong> which takes root node and integer K as input parameters and returns the number of paths that have sum K.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(Height of Tree)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 2*10<sup>4</sup><br>-10<sup>5</sup> ≤ Node Value ≤ 10<sup>5</sup><br>-10<sup>9</sup> ≤ K ≤ 10<sup>9</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<code>Amazon</code>&nbsp;<code>Walmart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;