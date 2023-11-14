<h2><a href="https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1">Check if strings are rotations of each other or not</a></h2><h3>Difficulty Level : Basic</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">You are given two strings of equal lengths, <strong>s1&nbsp;</strong>and&nbsp;<strong>s2</strong>. The task is to check&nbsp;if <strong>s2</strong> is a rotated version of the string <strong>s1</strong>. </span></p>
<p><span style="font-size: 18px;"><strong>Note:</strong> The characters in the strings are in lowercase.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>geeksforgeeks
forgeeksgeeks
<strong>Output: 
</strong>1<strong>
Explanation: </strong>s1 is geeksforgeeks, s2 is
forgeeksgeeks. Clearly, s2 is a rotated
version of s1 as s2 can be obtained by
left-rotating s1 by 5 units.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>mightandmagic
andmagicmigth
<strong>Output: 
</strong>0<strong>
Explanation: </strong>Here with any amount of
rotation s2 can't be obtained by s1.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:<br></strong>You don't have to read or print anything. </span><span style="font-size: 18px;">The task is to complete the function&nbsp;<strong>areRotations() </strong>which takes two strings, <strong>s1</strong> and <strong>s2 </strong>as inputs and checks if the two strings are rotations of each other. The function returns <strong>true </strong>if <strong>s1 </strong>can be obtained by rotating <strong>s2</strong>, else it returns <strong>false</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O( |s1|&nbsp;).<br><strong>Expected Space Complexity:</strong> O( |s1| ).<br></span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= |s1|,&nbsp;|s2| &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Oracle</code>&nbsp;<code>Adobe</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;