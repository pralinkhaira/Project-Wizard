/* Optimized tabulation technique */

#define vi vector<int> 
#define vvi vector<vi>

class Solution {
    vi DP;  
public:
    int uniquePaths(int m, int n) {
        DP = vi(n); 

        for(int i=0; i<n; i++) DP[i] = 1; 

        for(int i=1; i<m; i++) {
            vi temp(n, 1);  
            for(int j=1; j<n; j++) {
                temp[j] = DP[j] + temp[j-1];
            }
            DP = temp; 
        }

        return DP[n-1]; 
    }
};