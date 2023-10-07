func numOfArrays(n int, m int, k int) int {
    mod := int(1e9 + 7)

    dp := make([][]int, m+1)
    prefix := make([][]int, m+1)
    prevDp := make([][]int, m+1)
    prevPrefix := make([][]int, m+1)

    for i := range dp {
        dp[i] = make([]int, k+1)
        prefix[i] = make([]int, k+1)
        prevDp[i] = make([]int, k+1)
        prevPrefix[i] = make([]int, k+1)
    }

    for j := 1; j <= m; j++ {
        prevDp[j][1] = 1
        prevPrefix[j][1] = j
    }

    for i := 2; i <= n; i++ {
        for maxNum := 1; maxNum <= m; maxNum++ {
            for cost := 1; cost <= k; cost++ {
                dp[maxNum][cost] = (maxNum * prevDp[maxNum][cost]) % mod

                if maxNum > 1 && cost > 1 {
                    dp[maxNum][cost] = (dp[maxNum][cost] + prevPrefix[maxNum-1][cost-1]) % mod
                }

                prefix[maxNum][cost] = (prefix[maxNum-1][cost] + dp[maxNum][cost]) % mod
            }
        }

        for j := 1; j <= m; j++ {
            copy(prevDp[j], dp[j])
            copy(prevPrefix[j], prefix[j])
        }
    }

    return prefix[m][k]
}