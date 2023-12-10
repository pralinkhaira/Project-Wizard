//{ Driver Code Starts

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends


class Solution {
public:
    int digitsum(int n){
        int sum=0;
        while(n>0){
            sum += n%10;
            n/=10;
        }
        return sum;
    }
    int smithNum(int n) {
        int i=2,sum = digitsum(n),a=1;
        while(i*i<=n){
            if(n%i==0){
                a=0;
                sum -= digitsum(i);
                n/=i;
            }
            else{
                i++;
            }
        }
        sum-=a;
        sum -= digitsum(n);
        return sum==0;
        
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        
        cin>>n;

        Solution ob;
        cout << ob.smithNum(n) << endl;
    }
    return 0;
}
// } Driver Code Ends