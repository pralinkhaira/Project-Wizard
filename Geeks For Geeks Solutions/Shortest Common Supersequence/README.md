<h2><a href="https://www.geeksforgeeks.org/problems/shortest-common-supersequence0322/1">Shortest Common Supersequence</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two&nbsp;strings <strong>X</strong> and <strong>Y</strong>&nbsp;of lengths&nbsp;<strong>m</strong> and <strong>n</strong>&nbsp;respectively, find the length of the <strong>smallest string </strong>which has both, <strong>X and Y </strong>as its <strong>sub-sequences</strong>.<br><strong>Note:</strong>&nbsp;<strong>X</strong>&nbsp;and <strong>Y </strong>can have both uppercase and lowercase letters.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>X = abcd, Y = xycd
<strong>Output: </strong>6<strong>
Explanation: </strong>Shortest Common Supersequence
would be <strong>abxycd</strong> which is of <strong>length 6 </strong>and
has both the strings as its subsequences.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>X = efgh, Y = jghi
<strong>Output: </strong>6<strong>
Explanation: </strong>Shortest Common Supersequence
would be <strong>ejfghi </strong>which is of <strong>length 6</strong> and
has both the strings as its subsequences.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't have to take any input or print anything. Your task is to complete <strong>shortestCommonSupersequence()</strong>&nbsp;function that takes <strong>X, Y, m, </strong>and <strong>n </strong>as arguments and&nbsp;returns&nbsp;the <strong>length </strong>of the required string.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(Length(X) * Length(Y)).<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(Length(X) * Length(Y)).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1&lt;= |X|, |Y| &lt;= 100</span></p>
<p>&nbsp;</p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Dynamic Programming</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;