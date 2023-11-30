<h2><a href="https://www.geeksforgeeks.org/problems/shortest-path-from-1-to-n0156/1">Shortest path from 1 to n</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Consider a <strong>directed graph </strong>whose vertices are numbered from <strong>1</strong> <strong>to n</strong>. There is an edge from a vertex <strong>i</strong> to a vertex <strong>j</strong> if and only if either <strong>j = i + 1 or j = 3 * i</strong>. The task is to find the <strong>minimum </strong>number of edges in a path from vertex <strong>1</strong> to vertex <strong>n</strong>.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:
</strong>n = 9
<strong>Output:</strong>
2
<strong>Explanation</strong>:
Many paths are possible from 1 to 9.<br>Shortest one possible is,<br>1 -&gt; 3 -&gt; 9, of length 2.</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input</strong>:
n = 4
<strong>Output:</strong>
2
<strong>Explanation</strong>:
Possible paths from 1 to 4 are,<br>1 -&gt; 2 -&gt; 3 -&gt; 4 and<br>1 -&gt; 3 -&gt; 4.<br>Second path of length 2 is the shortest.</span></pre>
<p><span style="font-size: 18px;"><strong>Your Task:&nbsp;&nbsp;</strong><br>You don't need to read input or print anything. Your task is to complete the function&nbsp;<strong>minimumStep()</strong> which takes an integer <strong>n</strong><strong> </strong>as inputs and returns the <strong>minimum </strong>number of edges in a path from vertex 1 to vertex N.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity:</strong> O( log(n) )<br><strong>Expected Auxiliary Space:</strong>&nbsp;O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 ≤ N ≤ 10<sup>5</sup></span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Morgan Stanley</code>&nbsp;<code>Accolite</code>&nbsp;<code>Samsung</code>&nbsp;<code>Synopsys</code>&nbsp;<code>Cisco</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Mathematical</code>&nbsp;<code>Graph</code>&nbsp;<code>Shortest Path</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;