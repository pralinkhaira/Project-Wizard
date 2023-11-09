<h2><a href="https://www.geeksforgeeks.org/problems/predict-the-column/1">Predict the Column</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a matrix(2D array) <strong>M </strong>of size <strong>N</strong>*<strong>N</strong> consisting of <strong>0s</strong> and <strong>1s</strong> only. The task is to find the <strong>column </strong>with maximum number of <strong>0s</strong>.&nbsp;</span><span style="font-size: 18px;">If more than one column exists, print the one which comes first. If the maximum number of <strong>0s is 0 then return -1.</strong></span></p>
<p><span style="font-size: 18px;"><strong>Example:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 3
M[][] = {{0, 0, 0},
          {1, 0, 1},
          {0, 1, 1}}
<strong>Output:<br></strong>0
<strong>Explanation:
</strong>0th column (<strong>0-based indexing</strong>) is having 2 zeros which is maximum among all columns and comes first.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>Your task is to complete the function <strong>columnWithMaxZero()</strong> which should return the <strong>column numbe</strong>r with the maximum number of zeros.&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong>&nbsp;O(N * N)<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>3</sup><br>0 &lt;= A[i][j] &lt;= 1</span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Arrays</code>&nbsp;<code>Matrix</code>&nbsp;<code>Data Structures</code>&nbsp;