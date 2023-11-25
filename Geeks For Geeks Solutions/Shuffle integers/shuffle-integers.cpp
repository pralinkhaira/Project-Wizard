//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution{
	
	
	
	public:
	void shuffleArray(int arr[],int n)
	{
	    // Your code goes here
	    int start = 0, end = n/2, mod = 1e4;
        for(int i = 0; i < n; i++)
        {
            if(i % 2 == 0)
                arr[i] = (arr[start++] % mod) * mod + arr[i];
            else 
                arr[i] = (arr[end++] % mod) * mod + arr[i];
        }
        
        for(int i = 0; i < n; i++)
        arr[i] = arr[i]/mod;
	}
		 

};

//{ Driver Code Starts.


int main() 
{
   
   
   	int t;
    cin >> t;
    while (t--)
    {
    	int n;
	    cin>>n;
	    int a[n] ;
	    for(int i=0;i<n;i++)
	    {
	        cin>>a[i];
	    }


       

        Solution ob;
        ob.shuffleArray(a, n);

		for (int i = 0; i < n; i++) 
			cout << a[i] << " ";
    
	
        
	    cout << "\n";
	     
    }
    return 0;
}
// } Driver Code Ends