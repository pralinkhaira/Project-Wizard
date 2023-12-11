<h2><a href="https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1">Max Sum Subarray of size K</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given an array of integers <strong>Arr</strong> of size <strong>N</strong> and a number <strong>K</strong>. Return&nbsp;the <strong>maximum sum</strong> of a subarray of size <strong>K</strong>.</span></p>
<p><span style="font-size: 14pt;"><strong>NOTE*:&nbsp;</strong>A subarray is a contiguous part of any given array.</span></p>
<p><strong><span style="font-size: 18px;">Example 1:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:</span></strong>
<span style="font-size: 18px;">N = 4, K = 2
Arr = [100, 200, 300, 400]</span>
<strong><span style="font-size: 18px;">Output:</span></strong>
<span style="font-size: 18px;">700</span>
<strong><span style="font-size: 18px;">Explanation:</span></strong>
<span style="font-size: 18px;">Arr<sub>3 </sub> + Arr<sub>4</sub> =700,</span>
<span style="font-size: 18px;">which is maximum.</span></pre>
<p><strong><span style="font-size: 18px;">Example 2:</span></strong></p>
<pre><strong><span style="font-size: 18px;">Input:</span></strong>
<span style="font-size: 18px;">N = 4, K = 4</span>
<span style="font-size: 18px;">Arr = [100, 200, 300, 400]</span>
<strong><span style="font-size: 18px;">Output:</span></strong>
<span style="font-size: 18px;">1000</span>
<strong><span style="font-size: 18px;">Explanation:</span></strong>
<span style="font-size: 18px;">Arr<sub>1</sub> + Arr<sub>2</sub> + Arr<sub>3 </sub>+ Arr<sub>4</sub> =1000,</span>
<span style="font-size: 18px;">which is maximum.</span></pre>
<p><strong><span style="font-size: 18px;">Your Task:</span></strong></p>
<p><span style="font-size: 18px;">You don't need to read input or print anything. Your task is to complete the function <strong>maximumSumSubarray</strong>() which takes the integer <strong>K</strong>, vector <strong>Arr</strong> with size <strong>N</strong>, containing the elements of the array and returns the <strong>maximum sum</strong> of a subarray of size <strong>K</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(N)<br><strong>Expected Auxiliary Space:</strong> O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= N &lt;= 10<sup>5<br></sup>1 &lt;= Arr<sub>i</sub> &lt;= 10<sup>5</sup><sup><br></sup></span><span style="font-size: 18px;">1 &lt;= K &lt;= N</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>OYO Rooms</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>prefix-sum</code>&nbsp;<code>sliding-window</code>&nbsp;<code>Misc</code>&nbsp;<code>Algorithms</code>&nbsp;