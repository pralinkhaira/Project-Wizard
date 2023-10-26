const MOD = 10**9 + 7;

function numFactoredBinaryTrees(arr) {
    arr.sort((a, b) => a - b);
    const s = new Set(arr);
    const dp = {};
    for (let x of arr) dp[x] = 1;
    
    for (let i of arr) {
        for (let j of arr) {
            if (j > Math.sqrt(i)) break;
            if (i % j === 0 && s.has(i / j)) {
                dp[i] += (i / j === j ? dp[j] * dp[j] : dp[j] * dp[i / j] * 2);
                dp[i] %= MOD;
            }
        }
    }
    
    return Object.values(dp).reduce((acc, val) => (acc + val) % MOD, 0);
}