/*
Problem Link: https://practice.geeksforgeeks.org/problems/nodes-at-given-distance-in-binary-tree/1
*/

/* A binary Tree node
struct Node
{
    int data;
    struct Node *left, *right;
};
*/

class Solution
{
private:

void markParent(Node* root, unordered_map<Node*, Node*>&parent_track){
        queue<Node*>q;
        q.push(root);
        while(!q.empty()){
            Node* node=q.front();
            q.pop();
            if(node->left){
                parent_track[node->left]=node;
                q.push(node->left);
            }
            if(node->right){
                parent_track[node->right]=node;
                q.push(node->right);
            }
        }
    }
public:
    Node* getRef(Node* root, int target)
    {
        if(root==NULL || root->data == target)
            return root;
        Node *left= getRef(root->left,target);
        Node *right= getRef(root->right, target);
        if(left!=NULL)
        return left;
        if(right!=NULL)
        return right;
    }
    
    vector <int> KDistanceNodes(Node* root, int target , int k)
    {
        // return the sorted vector of all nodes at k dist
        //Node* t=findRootOfTarget(root, target);
        Node* t= getRef(root,target);
        unordered_map<Node*, Node*>parent_track;
        markParent(root, parent_track);
        
        queue<Node*>q;
        unordered_map<Node*, bool>visited;
        q.push(t);
        visited[t]=1;
        int cnt=0;
        while(!q.empty()){
            int size=q.size();
            if(cnt++==k) break;
            for(int i=0; i<size; i++){
                Node* node=q.front();
                q.pop();
                if(node->left && !visited[node->left]){
                    q.push(node->left);
                    visited[node->left]=1;
                }
                if(node->right && !visited[node->right]){
                    q.push(node->right);
                    visited[node->right]=1;
                }
                if(parent_track[node] && !visited[parent_track[node]]){
                    q.push(parent_track[node]);
                    visited[parent_track[node]]=1;
                }
            }
        }
        vector<int>ans;
        while(!q.empty()){
            Node* cur=q.front();
            q.pop();
            ans.push_back(cur->data);
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};
