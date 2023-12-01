<h2><a href="https://www.geeksforgeeks.org/problems/inorder-traversal-and-bst5855/1">Inorder Traversal and BST</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array <strong>arr&nbsp;</strong>of size <strong>N,&nbsp;</strong>determine whether this array represents an <strong>inorder traversal</strong> of a <strong>BST.&nbsp;</strong></span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong>&nbsp;All keys in BST must be unique.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N = 3
arr = {2, 4, 5}
<strong>Output:</strong> 1
<strong>Explaination:</strong> <br>Given array is inorder traversal for the following tree:<br>    4<br>   / \<br>  2   5</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N = 3
arr = {2, 4, 1}
<strong>Output:</strong> 0
<strong>Explaination:</strong> <br>Given array can not represent any BST.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>isRepresentingBST()</strong>&nbsp;which takes the array <strong>arr[]</strong> and its size <strong>N&nbsp;</strong>as input parameters&nbsp;and returns&nbsp;<strong>1</strong> if array represents Inorder traversal of a BST, else returns <strong>0</strong>. </span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup><br>1 ≤ arr[i]&nbsp;≤ 10<sup>5</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Binary Search Tree</code>&nbsp;<code>Tree</code>&nbsp;<code>Data Structures</code>&nbsp;