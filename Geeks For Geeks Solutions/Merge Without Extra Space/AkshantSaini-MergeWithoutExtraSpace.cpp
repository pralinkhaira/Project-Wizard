/*
Merge Without Extra Space
Problem Link: https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
*/


class Solution{
    public:
        //Function to merge the arrays.
        void merge(long long arr1[], long long arr2[], int n, int m) 
        { 
        int i = n - 1; // Index of last element in arr1
        int j = 0; // Index of first element in arr2

        while (i >= 0 && j < m) {
            if (arr1[i] > arr2[j]) {
                swap(arr1[i], arr2[j]);
                i--;
                j++;
            } else {
                break;
            }
        }

        sort(arr1, arr1 + n);
        sort(arr2, arr2 + m); 
        } 
};
