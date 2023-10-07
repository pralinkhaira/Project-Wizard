class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        
        dp = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prevDp = [[0] * (k+1) for _ in range(m+1)]
        prevPrefix = [[0] * (k+1) for _ in range(m+1)]
        
        for j in range(1, m+1):
            prevDp[j][1] = 1
            prevPrefix[j][1] = j
        
        for _ in range(2, n+1):
            dp = [[0] * (k+1) for _ in range(m+1)]
            prefix = [[0] * (k+1) for _ in range(m+1)]
            
            for maxNum in range(1, m+1):
                for cost in range(1, k+1):
                    dp[maxNum][cost] = (maxNum * prevDp[maxNum][cost]) % mod
                    
                    if maxNum > 1 and cost > 1:
                        dp[maxNum][cost] += prevPrefix[maxNum - 1][cost - 1]
                        dp[maxNum][cost] %= mod
                    
                    prefix[maxNum][cost] = (prefix[maxNum - 1][cost] + dp[maxNum][cost]) % mod
            
            prevDp, prevPrefix = [row[:] for row in dp], [row[:] for row in prefix]
        
        return prefix[m][k]