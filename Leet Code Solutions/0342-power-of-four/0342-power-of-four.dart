class Solution {
  bool isPowerOfFour(int n) {
if (n <= 0) return false;
  double x = log(n) / log(4);
  return x % 1 == 0;
  }
}