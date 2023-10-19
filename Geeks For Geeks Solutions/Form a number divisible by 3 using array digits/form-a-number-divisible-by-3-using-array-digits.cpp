//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    int isPossible(int N, int arr[]) {
        string temp;
        for(int i=0;i<N;i++)
        {
            temp+=to_string(arr[i]);
        }
        int sum=0;
        for(int i=0;i<temp.size();i++)
        {  
            sum+=(temp[i]-'0');
        }
        
        return sum%3==0;
        
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        cin >> N;
        int arr[N];
        for (int i = 0; i < N; i++) cin >> arr[i];

        Solution ob;
        cout << ob.isPossible(N, arr) << endl;
    }
    return 0;
}
// } Driver Code Ends