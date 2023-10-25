//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG{
    public static void main(String args[])throws IOException
    {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(in.readLine());
        while(t-- > 0){
            String line1[] = in.readLine().trim().split("\\s+");
            int N = Integer.parseInt(line1[0]);
            int W = Integer.parseInt(line1[1]);
            String line2[] = in.readLine().trim().split("\\s+");
            int val[] = new int[N];
            for(int i = 0;i < N;i++)
                val[i] = Integer.parseInt(line2[i]);
            String line3[] = in.readLine().trim().split("\\s+");
            int wt[] = new int[N];
            for(int i = 0;i < N;i++)
                wt[i] = Integer.parseInt(line3[i]);
                
            Solution ob = new Solution();
            System.out.println(ob.knapSack(N, W, val, wt));
        }
    }
}
// } Driver Code Ends

class Solution{
    static int knapSack(int N, int W, int val[], int wt[])
    {
        // code here
        int[][] dp = new int[N][W+1];
        for(int[] is: dp) Arrays.fill(is, -1);
        
        return function(N-1, W, val, wt, dp);
    }
    
    static int function(int index, int target, int[] values, int[] arr, int[][] dp) {
        if(index == 0) 
            return (target >= arr[0]) ? (target/arr[0])*values[0] : 0;
        
        
        if(dp[index][target] != -1) 
            return dp[index][target];
        
        int notTake = function(index-1, target, values, arr, dp);
        int take = 0;
        
        if(target >= arr[index]) 
            take = values[index] + function(index, target-arr[index], values, arr, dp);
        
        return dp[index][target] = Math.max(take, notTake);
    }
}