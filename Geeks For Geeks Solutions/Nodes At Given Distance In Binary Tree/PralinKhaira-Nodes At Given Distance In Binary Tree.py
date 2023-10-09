# Problem Link: https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1

#User function Template for python3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
from collections import deque 
class Solution:
    
    def KDistanceNodes(self,root,target,k):
        #  relating the parents to their child nodes so that we can acces the path 
        dct = {}
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()  # popping out the first element
                if node.data == target:
                    Target = node
                if node.left:   # if the left child exist 
                    dct[node.left] = node   # adding the child--> parent
                    q.append(node.left)   # appending the child into the queue
                if node.right:     # same if the right child exist 
                    dct[node.right] = node
                    q.append(node.right)
        
        # Step2 : 
        vis = set()
        pq = deque([Target])
        ds = 0
        while ds != k:
            for i in range(len(pq)):
                node = pq.popleft()
                vis.add(node)
                if node.left not in vis and node.left:
                    pq.append(node.left)
                    vis.add(node.left)
                if node.right not in vis and node.right:
                    pq.append(node.right)
                    vis.add(node.right)
                if dct.get(node)!=None and dct[node] not in vis:
                    pq.append(dct[node])
                    vis.add(dct[node])
            ds += 1
        ans = []
        while pq:
            ans.append(pq.pop().data)
        ans.sort()
        return ans
