<h2><a href="https://www.geeksforgeeks.org/problems/check-whether-bst-contains-dead-end/1">Check whether BST contains Dead End</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 20px;">Given a&nbsp;<a title="Binary Search Tree" href="https://www.geeksforgeeks.org/binary-search-tree-data-structure/" target="_blank" rel="noopener">Binary Search Tree</a> that contains <strong>unique positive integer values greater than 0</strong>. The task is to complete the function <strong>isDeadEnd</strong> which returns <strong>true</strong> if&nbsp;the BST contains a <strong>dead end </strong>else returns <strong>false</strong>. Here <strong>Dead End </strong>means a&nbsp;<strong>leaf</strong> node, at which no other node can be inserted.</span></p>
<p><strong><span style="font-size: 20px;">Example 1:</span></strong></p>
<pre><span style="font-size: 20px;"><strong>Input :</strong>   
&nbsp;              8
             /   \ 
           5      9
         /  \     
        2    7 
       /
      1     
          
<strong>Output :</strong> <br>Yes
<strong>Explanation :</strong> <br>Node 1 is a Dead End in the given BST.</span></pre>
<p><strong><span style="font-size: 20px;">Example 2:</span></strong><span style="font-size: 20px;"> </span></p>
<pre><span style="font-size: 20px;"><strong>Input :</strong>     
&nbsp;             8
            /   \ 
           7     10
         /      /   \
        2      9     13

<strong>Output :</strong> <br>Yes
<strong>Explanation :</strong> <br>Node 9 is a Dead End in the given BST.<br></span></pre>
<p><span style="font-family: sans-serif; font-size: 20px; white-space: normal;"><strong>Your Task:</strong> You don't have to input or print anything. Complete the function <strong>isDeadEnd()&nbsp;</strong>which takes <strong>BST</strong> as input and returns a boolean value.</span></p>
<p><span style="font-family: sans-serif; font-size: 20px; white-space: normal;"><strong>Expected Time Complexity:</strong> <strong>O(N),</strong> where <strong>N</strong> is the number of nodes in the <strong>BST.<br></strong></span><strong style="font-family: sans-serif; font-size: 20px; white-space: normal;">Expected Space Complexity:</strong><span style="font-family: sans-serif; font-size: 20px; white-space: normal;">&nbsp;</span><strong style="font-family: sans-serif; font-size: 20px; white-space: normal;">O(N)</strong></p>
<p><span style="font-size: 20px;"><strong>Constraints:</strong></span><span style="font-size: 20px;"><br>1 &lt;= N &lt;= 1001<sup><br></sup>1 &lt;= Value of Nodes &lt;= 10001<sup><br></sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;