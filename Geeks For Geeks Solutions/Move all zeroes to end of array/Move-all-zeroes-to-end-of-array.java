//User function Template for Java

class Solution {
    void pushZerosToEnd(int[] arr, int n) {
          
        int left=0, right=0;
        while(right<n) {
            if(arr[right]!=0) {
                int temp=arr[left];
                arr[left]=arr[right];
                arr[right]=temp;
                left++;
            }
            right++;
        }
    }
}
