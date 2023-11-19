//{ Driver Code Starts
//Initial template for C++

#include <bits/stdc++.h>
using namespace std;

struct Node 
{
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};

// Function to Build Tree
Node *buildTree(string str) 
{
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node *root = new Node(stoi(ip[0]));

    // Push the root to the queue
    queue<Node *> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node *currNode = queue.front();
        queue.pop();

        // Get the current Node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current Node
            currNode->left = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current Node
            currNode->right = new Node(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
//User function template for C++

/*
struct Node 
{
    int data;
    Node *left;
    Node *right;

    Node(int val) {
        data = val;
        left = right = NULL;
    }
};
*/
class Solution{
  public:
    int mod = (int)1e9+7;
    
    void solve(Node* root, int k, unordered_map<int, int> &sumCount, int sum, int &ans) {
        if (root == NULL) {
            return;
        }
        
        sum += root->data; // Adding the Valve of Current Node to the Path Sum
        
        ans += sumCount[sum - k] % mod; // Adding the No. of Remaining Sum Paths to the Answer
        
        sumCount[sum] += 1 % mod; // Storing the Current Sum to the 'sumCount' map
        
        if (sum == k) // Checking if Current Sum == k
        {
            ans += 1 % mod;
        }
        
        // Recursively Calling For Left & Right Subtrees 
        solve(root->left, k, sumCount, sum, ans);
        solve(root->right, k, sumCount, sum, ans);
        
        // Decrement the Count Of Current Sum from the map while returning 
        sumCount[sum] -= 1;
    }
    
    int sumK(Node *root,int k)
    {
        int ans = 0;
        unordered_map<int, int> sumCount;
        
        solve(root, k, sumCount, 0, ans);
        
        return ans;
    }
};

//{ Driver Code Starts.

int main() {
    string tc;
    getline(cin, tc);
    int t = stoi(tc);
  
    while(t--)
    {
        string s ,ch;
        getline(cin, s);
        Node* root = buildTree(s);

        string key;
        getline(cin, key);
        int k=stoi(key);
        Solution ob;
        cout << ob.sumK(root, k) << "\n";
    }
    return 0;
}
// } Driver Code Ends