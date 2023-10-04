/*
Next Smallest Palindrome
Problem Link: https://practice.geeksforgeeks.org/problems/next-smallest-palindrome4740/1
*/

class Solution{
public:
vector<int> generateNextPalindrome(int arr[], int n) {
       vector<int> num(arr,arr+n);
    int mid = (n+1)/2;
    bool flag = true;
    for(int i=mid;i<n;i++)
    {
        if(num[i]==num[n-i-1]) continue;
        if(num[i]<num[n-i-1]) flag = false;
        if(num[i]>num[n-i-1]) flag = true;
        break;
    }
    if(flag)
    {
        int carry = 1;
        for(int i=mid-1;i>=0 && carry==1;i--)
        {
            num[i] = (num[i]==9? 0:num[i]+carry--);
        }
        if(carry){
            vector<int> res;
            res.push_back(1);
            for(int i=1;i<n;i++) res.push_back(0);
            res.push_back(1);
            return res;
        }
    }
    for(int i=mid-1;i>=0;i--)
    {
        num[n-i-1]=num[i];
    }
    return num;
}
 
};
