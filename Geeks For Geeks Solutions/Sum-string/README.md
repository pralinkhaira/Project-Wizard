<h2><a href="https://www.geeksforgeeks.org/problems/sum-string3151/1">Sum-string</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 14pt;">Given a string of <strong>digits</strong>, the task is to check if it is a ‘<strong>sum-string</strong>’. A string <strong>S</strong> is called a sum-string when it is broken down into more than one substring and the rightmost substring can be written as a sum of two substrings before it and the same is recursively true for substrings before it. </span></p>
<p><span style="font-size: 14pt;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong>
S = "12243660"
<strong>Output:</strong>
1
<strong>Explanation:</strong>
"12243660" can be broken down as {"12", "24", "36", "60"}.<br>We can get 60 from 24 and 36 as 24 + 36 = 60. Similarly 36 can be written as 12 + 24.</span></pre>
<p><span style="font-size: 14pt;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 14pt;"><strong>Input:</strong>
1111112223
<strong>Output:</strong>
1
<strong>Explanation:<br></strong>"1111112223" can be broken down as {"1", "111", "112", "223"}.<br></span><span style="font-size: 14pt;">We can get 223 from 111 and 1112 as 111 + 112 = 223. Similarly 112 can be written as 1 + 111.</span></pre>
<p><span style="font-size: 14pt;"><strong>Your Task:</strong></span></p>
<p><span style="font-size: 14pt;">You don't need to read input or print anything. Your task is to complete the function <strong>isSumString()</strong> which takes the string S and returns 1 is S is a sum-string otherwise returns 0.</span></p>
<p><span style="font-size: 14pt;"><strong>Expected Time Complexity: </strong>O(|S|<sup>3</sup>)<br><strong>Expected Auxiliary Space:</strong> O(|S|)</span></p>
<p><span style="font-size: 14pt;"><strong>Constraints:<br></strong>1 &lt;= |S| &lt;= 500</span><span style="font-size: 14pt;"><br><span style="font-size: 14pt;">String consists of characters from '0' to '9'.</span></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Nutanix</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Recursion</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;