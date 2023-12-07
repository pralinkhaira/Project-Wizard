<h2><a href="https://www.geeksforgeeks.org/problems/number-of-subarrays-with-maximum-values-in-given-range5949/1">Number of subarrays with maximum values in given range</a></h2><h3>Difficulty Level : Medium</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of <strong>N</strong> elements and <strong>L</strong> and <strong>R</strong>, print the number of sub-arrays such that the value of the <strong>maximum</strong> array element in that subarray is at least L and at most R.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> <br>Arr = {2, 0, 11, 3, 0}
L = 1 and R = 10
<strong>Output :</strong> <br>4
<strong>Explanation:
</strong>The sub-arrays {2}, {2, 0}, {3} and {3, 0} have maximum in range 1-10.
</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input :</strong> <br>Arr = {3, 4, 1}
L = 2 and R = 4
<strong>Output :</strong> <br>5<br><strong>Explanation:</strong><strong style="font-family: sans-serif;"><br></strong>The sub-arrays {3}, {3, 4}, {3,4,1}, {4} and {4, 1} have maximum in range 2-4.
</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>This is a function problem. The input is already taken care of by the driver code. You only need to complete the function <strong>countSubarrays()</strong> that takes an array <strong>arr</strong>, sizeOfArray <strong>(n)</strong>, element <strong>L, </strong>integer <strong>R,</strong> and return the number of subarray with the maximum&nbsp;in range L-R. The driver code takes care of the printing.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong>&nbsp;O(N).<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1).</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup><br></span><span style="font-size: 18px;">0 </span><span style="font-size: 18px;">≤ arr[i]&nbsp;</span><span style="font-size: 18px;">≤&nbsp;</span><span style="font-size: 18px;">10</span><sup>9</sup><span style="font-size: 18px;"><br></span><span style="font-size: 18px;">1 ≤ L ≤ R ≤ 10</span><sup>9</sup></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>sliding-window</code>&nbsp;<code>two-pointer-algorithm</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;