<h2><a href="https://www.geeksforgeeks.org/problems/binary-tree-to-cdll/1">Binary Tree to CDLL</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a <strong>Binary Tree </strong>of<strong> N</strong> edges. The task is to convert this to a <strong>Circular Doubly Linked List (CDLL)</strong> in-place. The <strong>left and right pointers </strong>in nodes are to be used as <strong>previous and next pointers </strong>respectively in <strong>CDLL</strong>. The order of nodes in <strong>CDLL </strong>must be same as <strong>Inorder </strong>of the given <strong>Binary Tree</strong>. The first node of <strong>Inorder traversal </strong>(left most node in <strong>BT</strong>) must be <strong>head node </strong>of the <strong>CDLL</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>&nbsp; &nbsp; &nbsp; 1
 &nbsp; &nbsp;/&nbsp; &nbsp;\
 &nbsp; 3&nbsp; &nbsp; &nbsp;2
<strong>Output:
</strong>3 1 2&nbsp;
2 1 3<strong>
Explanation: </strong>After converting tree to CDLL
when CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>&nbsp; &nbsp;&nbsp; 10
 &nbsp; /&nbsp; &nbsp; \
 &nbsp;20&nbsp; &nbsp; 30
 /&nbsp; \
40 &nbsp;60
<strong>Output:
</strong>40 20 60 10 30&nbsp;
30 10 60 20 40<strong>
Explanation:</strong>After converting tree to CDLL,
when CDLL is is traversed from head to
tail and then tail to head, elements
are displayed as in the output.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't have to take input or print anything. Complete the function <strong>bTreeToCList()&nbsp;</strong>that takes root as a parameter and <strong>returns </strong>the <strong>head of the list</strong>. The driver code prints the linked list twice, first time in the <strong>right order</strong>, and another time in <strong>reverse order</strong>. </span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>3</sup><br>0 &lt;= Data of a node &lt;= 10<sup>4</sup></span></p>
<p><span style="font-size: 18px;"><strong>Expected time complexity:&nbsp;</strong>O(N)</span></p>
<p><span style="font-size: 18px;"><strong>Expected auxiliary space:&nbsp;</strong>O(h) , where h = height of tree</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Amazon</code>&nbsp;<code>SAP Labs</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Linked List</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;