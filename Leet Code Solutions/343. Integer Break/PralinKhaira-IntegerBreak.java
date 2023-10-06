/*
Problem Link: https://leetcode.com/problems/integer-break/description/
*/

class Solution {
    public int integerBreak(int n) {
        if (n <= 3) return n - 1;
        int quotient = n / 3, remainder = n % 3;
        return remainder == 0 ? (int)Math.pow(3, quotient) : (remainder == 1 ? (int)Math.pow(3, quotient - 1) * 4 : (int)Math.pow(3, quotient) * 2);
    }
}
