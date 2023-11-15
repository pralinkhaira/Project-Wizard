<h2><a href="https://www.geeksforgeeks.org/problems/find-the-string/1">Find the String</a></h2><h3>Difficulty Level : Hard</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two integers<strong> N</strong> and <strong>K, </strong>the task is to find the string <strong>S</strong> of <strong>minimum </strong>length such that it contains <strong>all possible strings </strong>of size <strong>N</strong> as a <strong>substring</strong>. The characters of the string should be from integers ranging from <strong>0 to K-1</strong>.&nbsp;&nbsp;</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
N = 2, K = 2
<strong>Output:</strong> 
00110
<strong>Explanation: 
</strong>Allowed characters are from 0 to k-1 (i.e., 0 and 1).<br></span><span style="font-size: 18px;">There are 4 string possible of size N=2 
(i.e "00", "01","10","11")
"00110" contains all possible string as a 
substring. It also has the minimum length.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>N = 2, K = 3
<strong>Output: 
</strong>0010211220
<strong>Explanation: <br></strong></span><span style="font-size: 18px;">Allowed characters are from 0 to k-1 (i.e., 0, 1 and 2).<strong><br></strong>There are total 9 strings possible
of size N, given output string has the minimum
length that contains all those strings as substring.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;</strong><br>You don't need to read input or print anything. Complete the function<strong>&nbsp;findString( )</strong>&nbsp;which takes the integer <strong>N</strong> and the integer <strong>K</strong>&nbsp;as input parameters and returns the string.<br><strong>Note:</strong> In case of multiple answers, return <strong>any string of minimum length </strong>which satisfies above condition. The driver will print the <strong>length</strong> of the&nbsp;string. In case of wrong answer it will print <strong>-1</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O(K<sup>N</sup>logK)<br><strong>Expected Space Complexity: </strong>O(K<sup>N</sup>N)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N&nbsp;≤ 4<br>1 <u>&lt;</u> K <u>&lt;</u> 10<br>1&nbsp;<u>&lt;</u> K<sup>N</sup>N &lt; 10<sup>6</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Graph</code>&nbsp;<code>Backtracking</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;