//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution{   
public:
    long maximumSumSubarray(int K, vector<int> &Arr , int N){
        // code here 
        long maxSum = 0;
        long currentSum = 0;

        // Calculate the sum of the first subarray of size K
        for (int i = 0; i < K; ++i) {
            currentSum += Arr[i];
        }

        // Initialize maxSum with the sum of the first subarray
        maxSum = currentSum;

        // Iterate through the remaining subarrays using the sliding window
        for (int i = K; i < N; ++i) {
            // Add the current element to the window
            currentSum += Arr[i];
            // Subtract the first element of the previous subarray
            currentSum -= Arr[i - K];

            // Update maxSum if the currentSum is greater
            maxSum = max(maxSum, currentSum);
        }

        return maxSum;
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        int N,K;
        cin >> N >> K;;
        vector<int>Arr;
        for(int i=0;i<N;++i){
            int x;
            cin>>x;
            Arr.push_back(x);
        }
        Solution ob;
        cout << ob.maximumSumSubarray(K,Arr,N) << endl;
    }
    return 0; 
} 
// } Driver Code Ends