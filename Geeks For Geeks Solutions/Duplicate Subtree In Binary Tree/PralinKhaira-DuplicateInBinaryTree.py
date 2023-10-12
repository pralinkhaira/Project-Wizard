# Problem Link: https://practice.geeksforgeeks.org/problems/duplicate-subtree-in-binary-tree/1



#User function Template for python3
'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:
    dp={}
    
    def dupRecur(self,root):
        if root==None:
            return ""
        left=self.dupRecur(root.left)
        mid=str(root.data)
        right=self.dupRecur(root.right)
        key=left+","+mid+","+right
        if root.left!=None or root.right!=None:
            self.dp[key]=self.dp.get(key,0)+1
        return key
        
    def dupSub(self, root):
        # code here
        self.dp={}
        self.dupRecur(root)
        for i in self.dp.values():
            if i>1:
                return 1
        return 0
        # code here
