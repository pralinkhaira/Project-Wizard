/*
Problem Link: https://practice.geeksforgeeks.org/problems/level-of-nodes-1587115620/1
*/


class Solution
{
	public:
	//Function to find the level of node X.
	int nodeLevel(int V, vector<int> adj[], int X) 
	{
	    queue<pair<int,int>> q;
	    q.push({0,0});
	    bool visited[V]={false};
	    visited[0]=true;
	    while(!q.empty()){
	        int node = q.front().first;
	        int ans = q.front().second;
	        q.pop();
	        if(node == X) return ans;
	        for(auto it : adj[node]){
	            if(!visited[it]) {
	                q.push({it, ans+1});
	                visited[it]=true;
	            }
	        }
	    }
	    return -1;
	}
};
