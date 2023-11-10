<h2><a href="https://www.geeksforgeeks.org/problems/isomorphic-strings-1587115620/1">Isomorphic Strings</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given two strings '<strong>str1</strong>' and '<strong>str2</strong>', check if these two&nbsp;strings are <strong>isomorphic </strong>to each other.<br></span></p>
<p><span style="font-size: 18px;">If the characters in str1 can be changed to get str2, then two strings, str1 and str2, are isomorphic. </span><span style="font-size: 18px;">A character must be completely swapped out for another character while maintaining the order of the characters. A character may map to itself, but no two characters may map to the same character.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>str1 = aab
str2 = xxy
<strong>Output: <br></strong>1<strong>
Explanation: <br></strong>There are two different characters in aab and xxy, i.e a and b with frequency 2 and 1 respectively.</span>
</pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>str1 = aab
str2 = xyz
<strong>Output: <br></strong>0<strong>
Explanation: <br></strong>There are two different characters in aab but there are three different charactersin xyz. So there won't be one to one mapping between str1 and str2.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:</strong><br>You don't need to read input or print anything.Your task is to complete the function <strong>areIsomorphic</strong>()&nbsp;which takes the string <strong>str1</strong>&nbsp;and string <strong>str2</strong>&nbsp;as input parameter&nbsp;and</span>&nbsp;<span style="font-size: 18px;">&nbsp;check&nbsp;if two strings are isomorphic. The function returns <strong>true </strong>if strings are isomorphic else it returns <strong>false</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:&nbsp;</strong>O(|str1|+|str2|).<br><strong>Expected Auxiliary Space:&nbsp;</strong>O(Number of different characters).<br><strong>Note:</strong>&nbsp;|s| represents the length of string s.</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= |str1|, |str2| &lt;= 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Google</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Strings</code>&nbsp;<code>Data Structures</code>&nbsp;