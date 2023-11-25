<h2><a href="https://www.geeksforgeeks.org/problems/print-pattern3549/1">Print Pattern</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Print a sequence of numbers starting with <strong>N</strong>,&nbsp;<strong><em>without using loop</em></strong>, where replace N with N - 5, until N &gt; 0. After that replace N with N + 5 until N regains its initial value.</span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>N = 16
<strong>Output:</strong> <br>16 11 6 1 -4 1 6 11 16
<strong>Explaination:</strong> <br>The value decreases until it is greater than 0. After that it increases and stops when it becomes 16 again.</span></pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong> <br>N = 10
<strong>Output:</strong> <br>10 5 0 5 10
<strong>Explaination:</strong> It follows the same logic as per the above example.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You do not need to read input or print anything. Your task is to complete the function <strong>pattern()</strong> which takes N as input parameters and returns a list containing the pattern.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(N)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>-10<sup>5</sup> ≤ N ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Microsoft</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>pattern-printing</code>&nbsp;<code>Recursion</code>&nbsp;<code>Algorithms</code>&nbsp;