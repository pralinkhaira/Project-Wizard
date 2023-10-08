/*
Problem Link: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1
*/

//User function template for C++

/*
struct Node
{
    int data;
    struct Node* left;
    struct Node* right;
    
    Node(int x){
        data = x;
        left = right = NULL;
    }
};
*/
class Solution{
    public:
    int height(struct Node* node){
        if(!node)return 0;
         return  max(height(node->left),height(node->right))+1;
    }
};
