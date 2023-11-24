//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// #define ll long long
class Solution{
public:
    vector<long long> nthRowOfPascalTriangle(int n) {
        // code here
        vector<long long> prev;
        prev.push_back(1LL);

        for (int i = 1; i < n; i++) {
            vector<long long> next;
            next.push_back(1LL);

            for (int j = 1; j < prev.size(); j++) {
                next.push_back((prev[j] + prev[j - 1]) % 1000000007);
            }
            next.push_back(1LL);
            prev = next;
        }

        return prev;
    }
};


//{ Driver Code Starts.


void printAns(vector<long long> &ans) {
    for (auto &x : ans) {
        cout << x << " ";
    }
    cout << "\n";
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        Solution ob;
        auto ans = ob.nthRowOfPascalTriangle(n);
        printAns(ans);
    }
    return 0;
}

// } Driver Code Ends