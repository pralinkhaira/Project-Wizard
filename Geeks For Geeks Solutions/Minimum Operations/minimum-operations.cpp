//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
  public:
    int minOperation(int n)
    {
        int count = 0;
        while(n!=0)
            {
                // if n is even then it will be good to
                // reach n from n/2 by multiplying it by 2.
                if(n%2==0)
                    n/=2;
                // if n is odd then we can reach n from n-- only. 
                else
                    n--;
                
                count++;     
            }
        return count;
    }
};


//{ Driver Code Starts.
int main()
{
	int t;
	cin>>t;
	while(t--)
	    {
	        int n;
	        cin>>n;
	        Solution ob;
	        cout<<ob.minOperation(n)<<endl;
	    }
}
// } Driver Code Ends