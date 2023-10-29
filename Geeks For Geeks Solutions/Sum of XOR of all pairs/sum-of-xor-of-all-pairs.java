//{ Driver Code Starts
//Initial Template for Java

//Initial Template for Java

//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;


class Array {
    
    // Driver code
	public static void main (String[] args) throws IOException{
		// Taking input using buffered reader
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testcases = Integer.parseInt(br.readLine());
		
		// looping through all testcases
		while(testcases-- > 0){
		    String line = br.readLine();
		    String[] element = line.trim().split("\\s+");
		    int sizeOfArray = Integer.parseInt(element[0]);
		    
		    int arr [] = new int[sizeOfArray];
		    
		    line = br.readLine();
		    String[] elements = line.trim().split("\\s+");
		    for(int i = 0;i<sizeOfArray;i++){
		        arr[i] = Integer.parseInt(elements[i]);
		    }
		    
		    
		    Solution obj = new Solution();
		    long res = obj.sumXOR(arr, sizeOfArray);
		    System.out.println(res);
		}
	}
}



// } Driver Code Ends

class Solution{
   
    // Function for finding maximum and value pair
    public long sumXOR (int arr[], int n) {
        //Complete the function
         long ans = 0;
		long left ;
		long pos = 0;
		for(int i=0;i<32;i++) {
			long one=0,zero=0;
			left = 1<<i;
			for(int j=0;j<arr.length;j++) {
				if((arr[j] & left)==0) {
					zero++;
				}else {
					one++;
				}
			}
			ans += (zero * one ) * (long)Math.pow(2, pos);
			pos++;
		}
		
		return ans;
    }
    
    
}
