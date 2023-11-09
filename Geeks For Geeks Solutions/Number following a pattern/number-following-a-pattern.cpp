//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends

class Solution{   
public:
    string printMinNumberForPattern(string s){
        // code here 
        int n=s.size();
        string ans(n+1,'0');
        int nextnum=1;
        int countD=0;
        
        for(int i = 0; i < n; i++) 
        {
            
            if(s[i] == 'I') 
            {
                if(countD)
                {
                int k=i-countD;
                int num=nextnum;
                while(k<=i)
                {
                    ans[k++]='0'+num--;
                }
                countD=0;
                }
                else ans[i]='0'+nextnum;
               
            } 
            else countD++;
            
            nextnum++;
        }
        
        if(s[n-1]=='I') ans[n]=nextnum+'0';
        else
        {
                int k=n-countD;
                int num=nextnum;
                while(k<=n)
                {
                    ans[k++]='0'+num--;
                }
                countD=0;
                
        }
        
        
        return ans;
        
    }
};

//{ Driver Code Starts.
int main() 
{ 
    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin >> S;
        Solution ob;
        cout << ob.printMinNumberForPattern(S) << endl;
    }
    return 0; 
} 

// } Driver Code Ends