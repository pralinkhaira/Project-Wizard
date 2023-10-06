# Problem Link: https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        return (n - 1) if n <= 3 else (3 ** (n // 3)) if n % 3 == 0 else (3 ** (n // 3 - 1) * 4) if n % 3 == 1 else (3 ** (n // 3) * 2)
