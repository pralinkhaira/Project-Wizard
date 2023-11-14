//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution
{
    public:
    //Function to check if two strings are rotations of each other or not.
    bool areRotations(string s1,string s2)
    {
        // Your code here
        if(s1.length()!=s2.length()) 
            return false;
    
        for(int i = s2.length() - 1 ; i >=0 ; i--)
        {
            char ch = s2[s2.length()-1];
            s2.pop_back();
            s2 = ch + s2;
            if(s1 == s2)
                return true;
        }
        
        return false;
    }
};

//{ Driver Code Starts.

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s1;
        string s2;
        cin>>s1>>s2;
        Solution obj;
        cout<<obj.areRotations(s1,s2)<<endl;

    }
    return 0;
}

// } Driver Code Ends