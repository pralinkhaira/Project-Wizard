#Problem Link: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1

#User function Template for python3


'''class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None'''


#Function to check whether a binary tree is balanced or not.
class Solution:
    def isBalanced(self,root):
        def height(root):
            if not root:
                return [True , 0]
            left , right = height(root.left) , height(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1])<=1
            return [balanced , 1+ max(left[1],right[1])]
        return height(root)[0]

#DriverCode..
