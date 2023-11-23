<h2><a href="https://www.geeksforgeeks.org/problems/avl-tree-insertion/1">AVL Tree Insertion</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given an AVL tree and N values to be inserted in the tree. Write a function to insert elements into the given&nbsp;<strong>AVL tree</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>Note:</strong><br>The tree will be checked after each insertion.&nbsp;<br>If it violates the properties of balanced BST, an error message will be printed followed by the inorder traversal of the tree at that moment.<br>If instead all insertions are successful, inorder traversal of the tree will be printed.</span></p>
<p><span style="font-size: 14pt;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:<br></strong>N = 3<strong><br></strong>Values to be inserted = {5,1,4}<strong> </strong>
<strong>Output:<br></strong>1 4 5<br><strong>Explanation:<br></strong>Value to be inserted = 5<strong><br></strong>    5
Value to be inserted = 1
    5
   /
  1
Value to be inserted = 4
  5                     4
 /    <strong>LR rotation</strong>        /  \
1    -----------&gt;       1   5
&nbsp;\
&nbsp;4<br>Therefore the inorder of the final tree will be 1, 4, 5.</span></pre>
<p><span style="font-size: 14pt;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong><br>N = 7<strong><br></strong>Values to be inserted = {21,26,30,9,4,14,28}<strong> </strong>
<strong>Output:<br></strong>4 9 14 21 26 28 30<br><strong style="font-family: sans-serif;">Explanation:</strong><br>Value to be inserted = 21<strong><br></strong>    21
Value to be inserted = 26
    21
     \
     26
Value to be inserted = 30
  21                        26
   \      <strong>LL rotation</strong>         /  \
   26    -----------&gt;       21  30
    \
     30<br>Value to be inserted = 9<br>    26<br>   /  \<br>  21  30<br> /<br>9<br>Value to be inserted = 4<br>      26                          26<br>     /  \                          /  \<br>    21  30                      9   30<br>   /          <strong>RR rotation</strong>        /  \<br>  9          -----------&gt;       4  21<br> /<br>4<br>Value to be inserted = 14<br>      26                          21<br>     /  \                          /  \<br>    9   30                      9   26<br>   / \          <strong>LR rotation</strong>      /  \    \<br>  4  21        -----------&gt;    4  14  30<br> &nbsp; &nbsp; /<br>    14<br>Value to be inserted = 28<br>      21                          21<br>     /  \                          /  \<br>    9   26                      9   28<br>   / \    \     <strong>RL rotation</strong>       / \    / \<br>  4  14   30   -----------&gt;   4  14 26 30<br>          /<br>         28<br>Therefore the inorder of the final tree will be 4, 9, 14, 21, 26, 28, 30.</span></pre>
<p><span style="font-size: 14pt;"><strong>Your Task: &nbsp;</strong><br>You don't need to read input or print anything. Complete the function<strong>&nbsp;insertToAVL()</strong>&nbsp;which takes the root of the tree and the value of the node to be inserted as input parameters and returns the root of the modified tree.</span></p>
<p><span style="font-size: 14pt;"><strong>Expected Time Complexity:</strong>&nbsp;O(log N)<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(height of tree)</span></p>
<p><span style="font-size: 14pt;"><strong>Constraints:</strong><br>1 ≤ N ≤ 2000</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Morgan Stanley</code>&nbsp;<code>Amazon</code>&nbsp;<code>Snapdeal</code>&nbsp;<code>MakeMyTrip</code>&nbsp;<code>Oracle</code>&nbsp;<code>Oxigen Wallet</code>&nbsp;<code>Informatica</code>&nbsp;<code>Citicorp</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;