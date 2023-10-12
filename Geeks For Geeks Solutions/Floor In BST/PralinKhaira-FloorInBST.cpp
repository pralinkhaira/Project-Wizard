class Solution{

public:
    void f(Node* root,int x, int &ans){
        if(!root) return ;
        if(root->data <=x) ans= max(ans,root->data);
        f(root->left,x,ans);
        f(root->right,x,ans);
    }
    int floor(Node* root, int x) {
        int ans=-1;
        f(root,x,ans);
        return ans;
    }
};