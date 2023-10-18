//Eventual Safe States
// Problem link: https://practice.geeksforgeeks.org/problems/eventual-safe-states/1


class Solution {
  public:
    vector<int> eventualSafeNodes(int n, vector<int> adj[]) {
        // code here
        vector<int> v(n , 0);
        vector<int> graph[n];
        for(int i =0; i < n; i++){
            v[i] = adj[i].size();
            for(int j:adj[i]){
                graph[j].push_back(i);
            }
        }
        queue<int> q;
        vector<int> ans;
        for(int i = 0 ; i< n; i++){
            if(v[i] == 0){
                q.push(i);
                ans.push_back(i);
            }
        }
        while(!q.empty()){
            int i = q.front();
            q.pop();
            for(auto j:graph[i]){
                if(--v[j] == 0){
                    q.push(j);
                    ans.push_back(j);
                }
            }
        }
        sort(ans.begin() , ans.end());
        return ans;
    }
};
