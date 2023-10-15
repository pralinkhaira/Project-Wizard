var numWays = function(steps, arrLen) {
    const m = steps;
    const n = Math.min(steps / 2 + 1, arrLen);
    
    const dp = new Array(m + 1).fill(0).map(() => new Array(n).fill(0));
    dp[0][0] = 1;
    
    const mod = 1000000007;
    
    for (let i = 1; i <= m; i++) {
        for (let j = 0; j < n; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j > 0) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j - 1]) % mod;
            }
            if (j < n - 1) {
                dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod;
            }
        }
    }
    
    return dp[m][0];
};
