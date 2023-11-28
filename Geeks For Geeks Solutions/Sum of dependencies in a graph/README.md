<h2><a href="https://www.geeksforgeeks.org/problems/sum-of-dependencies-in-a-graph5311/1">Sum of dependencies in a graph</a></h2><h3>Difficulty Level : Easy</h3><hr><div class="problems_problem_content__Xm_eO"><p><span style="font-size: 18px;">Given a directed graph with <strong>V</strong> nodes and <strong>E</strong> edges, if there is an edge from <strong>u</strong> to <strong>v</strong>, then we will say that <strong>u</strong> <strong>depends</strong> on <strong>v</strong>. <strong>Number of Dependencies (NoD) </strong>for a node <strong>x </strong>is the total <strong>count</strong> of nodes that <strong>x</strong> <strong>depends</strong> upon. Find out the <strong>sum </strong>of <strong>number</strong> of <strong>dependencies</strong> of every node.</span></p>
<p><span style="font-size: 18px;"><strong>Example 1:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
<strong>V </strong>= 4
<strong>E </strong>= 4
<strong>Edges</strong> = { {0,2}, {0,3}, {1,3}, {2,3} }</span>
<span style="font-size: 18px;"><img style="height: 234px; width: 211px;" src="https://contribute.geeksforgeeks.org/wp-content/uploads/tree-6.png" alt=""></span>
<span style="font-size: 18px;"><strong>Output:</strong>
4
<strong>Explanation:</strong>
For the graph in diagram, <br>A depends on C and D i.e. A's NoD is 2, <br></span><span style="font-size: 18px;">B depends on D i.e. B's NoD is 1,<br>C depends on D i.e. D's NoD is 1,
and D depends on none.
Hence answer -&gt; 0 + 1 + 1 + 2 = 4</span></pre>
<p><span style="font-size: 18px;"><strong>Example 2:</strong></span></p>
<pre><span style="font-size: 18px;"><strong>Input:</strong>
<strong>V </strong>= 4
<strong>E </strong>= 3
<strong>Edges </strong>= { {0,3}, {0,2}, {0,1} }
<strong>Output:</strong>
3
<strong>Explanation:</strong>
The sum of dependencies=3+0+0+0=3.</span></pre>
<pre><span style="font-size: 18px;"><strong style="font-family: sans-serif; white-space: normal;">Your Task:</strong><br>You don't need to read input or print anything. Your task is to complete the function <strong>sumOfDependencies()</strong> which takes the <strong>adj </strong>(Adjacency list) and <strong>V </strong>(Number of nodes) as input parameters and returns the <strong>total sum </strong>of <strong>Number of Dependencies </strong>of <strong>all nodes</strong>.</span></pre>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity: </strong>O(V)<br><strong>Expected Auxillary Space: </strong>O(1)</span></p>
<p><span style="font-size: 18px;"><strong>Constraints:</strong><br>1 &lt;= V &lt;= 10<sup>5<br></sup>1 &lt;= E &lt;= 10<sup>5</sup><sup><br></sup></span></p>
<p><span style="font-size: 18px;">0 &lt;= Edges[i][0], Edges[i][1] &lt;= V-1</span></p></div><p><span style=font-size:18px><strong>Company Tags : </strong><br><code>Flipkart</code>&nbsp;<br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Graph</code>&nbsp;<code>Data Structures</code>&nbsp;