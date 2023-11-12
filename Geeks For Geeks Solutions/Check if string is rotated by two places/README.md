<h2><a href="https://www.geeksforgeeks.org/problems/check-if-string-is-rotated-by-two-places-1587115620/1">Check if string is rotated by two places</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings <strong>a </strong>and <strong>b</strong>. The task is to find if the string 'b' can be obtained by rotating</span><span style="font-size: 18px;">&nbsp;</span><span style="font-size: 18px;">(<strong>in any direction</strong>)</span><span style="font-size: 18px;"> </span><span style="font-size: 18px;">string 'a' by </span><strong style="font-size: 18px;">exactly 2</strong><span style="font-size: 18px;"> places.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>a = amazon
b = azonam
<strong>Output: <br></strong>1<strong>
Explanation: <br></strong>amazon can be rotated anti-clockwise by two places, which will make it as azonam.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>a = geeksforgeeks
b = geeksgeeksfor
<strong>Output: <br></strong>0<strong>
Explanation: <br></strong>If we rotate geeksforgeeks by two place in any direction, we won't get geeksgeeksfor.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>The task is to complete the function&nbsp;<strong>isRotated()</strong> which takes two strings as input parameters and&nbsp;checks if given strings can be formed by rotations. The function returns&nbsp;true&nbsp;if string 1 can be obtained by rotating string 2 by two places, else it returns&nbsp;false.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong>&nbsp;O(N).<br><strong>Expected Auxilary Complexity:</strong>&nbsp;O(N).<br><strong>Challenge: </strong>Try doing it in O(1) space complexity.</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ length of a, b ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Accolite</code>&nbsp;<code>Amazon</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;