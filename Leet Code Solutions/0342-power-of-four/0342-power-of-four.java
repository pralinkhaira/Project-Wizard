class Solution {
    public boolean isPowerOfFour(int n) {
      if (n <= 0) return false;
        double x = Math.log(n) / Math.log(4);
        return x % 1 == 0;  
    }
}