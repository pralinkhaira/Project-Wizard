//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.math.*;
import java.io.*;

class GFG {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String str1 = sc.next();
            String str2 = sc.next();

            Solution obj = new Solution();
            String ans = obj.betterString(str1, str2);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends

class Solution {
    public static String betterString(String str1, String str2) {
        int MOD = 1_000_000_007;
        int n = str1.length();
        int m = str2.length();

        int[] lastIdx1 = new int[26];
        int[] lastIdx2 = new int[26];
        int[] dp1 = new int[n + 1];
        int[] dp2 = new int[m + 1];

        Arrays.fill(lastIdx1, -1);
        Arrays.fill(lastIdx2, -1);

        dp1[0] = 1;
        dp2[0] = 1;

        for (int i = 1; i <= n; i++) {
            char ch = str1.charAt(i - 1);
            dp1[i] = (2 * dp1[i - 1]) % MOD;
            if (lastIdx1[ch - 'a'] != -1) {
                dp1[i] = (dp1[i] - dp1[lastIdx1[ch - 'a']] + MOD) % MOD;
            }
            lastIdx1[ch - 'a'] = i - 1;
        }

        for (int i = 1; i <= m; i++) {
            char ch = str2.charAt(i - 1);
            dp2[i] = (2 * dp2[i - 1]) % MOD;
            if (lastIdx2[ch - 'a'] != -1) {
                dp2[i] = (dp2[i] - dp2[lastIdx2[ch - 'a']] + MOD) % MOD;
            }
            lastIdx2[ch - 'a'] = i - 1;
        }

        long count1 = dp1[n];
        long count2 = dp2[m];

        return (count1 >= count2) ? str1 : str2;
    }
}