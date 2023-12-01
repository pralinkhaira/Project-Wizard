//{ Driver Code Starts
//Initial template for C++

#include<bits/stdc++.h>

using namespace std;

struct Node
{
	int data;
	struct Node *left;
	struct Node *right;
	
	Node(int x){
	    data = x;
	    left = NULL;
	    right = NULL;
	}
};


void insert(Node ** tree, int val)
{
    Node *temp = NULL;
    if(!(*tree))
    {
        temp = new Node(val);
        *tree = temp;
        return;
    }

    if(val < (*tree)->data)
    {
        insert(&(*tree)->left, val);
    }
    else if(val > (*tree)->data)
    {
        insert(&(*tree)->right, val);
    }

}




int getCountOfNode(Node *root, int l, int h)
{

    if (!root) return 0;


    if (root->data == h && root->data == l)
        return 1;

    if (root->data <= h && root->data >= l)
         return 1 + getCountOfNode(root->left, l, h) +
                    getCountOfNode(root->right, l, h);

    else if (root->data < l)
         return getCountOfNode(root->right, l, h);


    else return getCountOfNode(root->left, l, h);
}


// } Driver Code Ends
/*The Node structure is
struct Node {
int data;
Node * right, * left;
};*/

/*You are required to complete below method */
class Solution{
  public:
    bool isDeadEnd(Node *root)
    {
        //Your code here
        queue<Node*>q;
        vector<int>leaf;
        vector<int>visited;
        q.push(root);
        
        while(!q.empty()){
            Node* node=q.front();
            visited.push_back(node->data);
            q.pop();
            if(node->left)q.push(node->left);
            if(node->right)q.push(node->right);
            if(node->left==NULL && node->right==NULL)leaf.push_back(node->data);
        }
        
        int n=leaf.size();
        for(int i=0;i<n;i++){
            if((leaf[i]==1 && find(visited.begin(),visited.end(),2)!=visited.end())||(find(visited.begin(),visited.end(),leaf[i]-1)!=visited.end() && find(visited.begin(),visited.end(),leaf[i]+1)!=visited.end()))
                return true;
        }
        
        return false;
        
    }
};

//{ Driver Code Starts.
// bool isDeadEnd(Node *root);
int main()
{
    int T;
    cin>>T;
    while(T--)
    {
        Node *root;
        Node *tmp;
    //int i;

        root = NULL;

        int N;
        cin>>N;
        for(int i=0;i<N;i++)
        {
            int k;
            cin>>k;
            insert(&root, k);

        }

     Solution ob;
     cout<<ob.isDeadEnd(root);
     cout<<endl;
    }
}


// } Driver Code Ends