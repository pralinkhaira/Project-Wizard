//{ Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

// } Driver Code Ends
class Solution{   
public:
      string helper(string &num1, string &num2) {
        string res = "";
        int n = num1.size(), m = num2.size();
        int carry = 0;
        int i = n-1, j = m-1;
        while(i >= 0 || j >= 0 || carry > 0) {
            int val1 = (i >= 0) ? num1[i--] - '0' : 0;
            int val2 = (j >= 0) ? num2[j--] - '0' : 0;
            int sum = val1 + val2 + carry;
            int rem = sum % 10;
            carry = sum / 10;
            res.push_back(rem + '0');
        }
        reverse(res.begin(), res.end());
        return res;
    }
    
    bool check(string& first, string& second, string &str) {
        int n = str.size();
        int j = first.size() + second.size();
        while(j < n) {
            string third = helper(first, second);
            if(j + third.size() > n) 
                return false;
            for(int i = 0; i < third.size(); i++) {
                if(third[i] != str[j+i])
                    return false;
            }
            first = second;
            second = third;
            j += third.size();
        }
        return true;
    }

    int isSumString(string str) {
        int n = str.size();
        // 0-i, i+1 - j
        for(int i = 0; i < n; i++) {
            for(int j = i+1; j < n-1; j++) {
                string first = str.substr(0, i+1);
                string second = str.substr(i+1, j-i);
                if(check(first, second, str))
                    return 1;
            }
        }
        return 0;
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
        cout << ob.isSumString(S) << endl;
    }
    return 0; 
} 

// } Driver Code Ends