//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function template for C++
class Solution{
  public:
  
  int LCS(int i,int j,string s,string t){
      
      if(i==0 || j==0) return 0;
      
      int notTake=0+max(LCS(i-1,j,s,t),LCS(i,j-1,s,t));
      
      int take=INT_MIN;
      if(s[i-1]==t[j-1])
      take=1+LCS(i-1,j-1,s,t);
      
      return max(take,notTake);
  }
    int minimumNumberOfDeletions(string S) { 
        // code here
        string t=S;
        int n=S.size();
        reverse(t.begin(),t.end());
        // int res= LCS(n,n,S,t);
        // return (i-res);
        vector<vector<int>>dp(n+1,vector<int>(n+1,0));
        
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                int notTake=0+max(dp[i-1][j],dp[i][j-1]);
      
      int take=INT_MIN;
      if(S[i-1]==t[j-1])
      take=1+dp[i-1][j-1];
      
      dp[i][j] =max(take,notTake);
            }
        }
        int res= dp[n][n];
        return n-res;
    } 
};

//{ Driver Code Starts.
int main(){
    int t;
    cin >> t;
    while(t--){
        string S;
        cin >> S;
        Solution obj;
        cout << obj.minimumNumberOfDeletions(S) << endl;
    }
    return 0;
}
// } Driver Code Ends