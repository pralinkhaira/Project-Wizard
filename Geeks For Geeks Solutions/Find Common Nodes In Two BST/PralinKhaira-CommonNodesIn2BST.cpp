class Solution {
  public:
    //Function to find the nodes that are common in both BST. 
    void mark(Node * & root, map < int, bool > & visited) {

      if (root == NULL) {

        return;

      }

      mark(root -> left, visited);

      visited[root -> data] = true;

      mark(root -> right, visited);

    }

  void chk(Node * & root, vector < int > & v, map < int, bool > & visited) {

    if (root == NULL) {

      return;

    }

    chk(root -> left, v, visited);

    if (visited[root -> data] == true) {

      v.push_back(root -> data);

    }

    chk(root -> right, v, visited);

  }

  vector < int > findCommon(Node * root1, Node * root2)

  {

    //Your code here

    map < int, bool > visited;

    vector < int > v;

    mark(root1, visited);

    chk(root2, v, visited);

    sort(v.begin(), v.end());

    return v;

  }

};