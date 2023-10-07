impl Solution {
    pub fn num_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;

        let mut dp = vec![vec![0; (k + 1) as usize]; (m + 1) as usize];
        let mut prefix = vec![vec![0; (k + 1) as usize]; (m + 1) as usize];
        let mut prevDp = vec![vec![0; (k + 1) as usize]; (m + 1) as usize];
        let mut prevPrefix = vec![vec![0; (k + 1) as usize]; (m + 1) as usize];

        for j in 1..=m {
            prevDp[j as usize][1] = 1;
            prevPrefix[j as usize][1] = j;
        }

        for _ in 2..=n {
            for maxNum in 1..=m {
                for cost in 1..=k {
                    dp[maxNum as usize][cost as usize] = 
                        ((maxNum as i64 * prevDp[maxNum as usize][cost as usize] as i64) % MOD as i64) as i32;
                    
                    if maxNum > 1 && cost > 1 {
                        dp[maxNum as usize][cost as usize] = 
                            (dp[maxNum as usize][cost as usize] + prevPrefix[(maxNum-1) as usize][(cost-1) as usize]) % MOD;
                    }

                    prefix[maxNum as usize][cost as usize] = 
                        (prefix[(maxNum-1) as usize][cost as usize] + dp[maxNum as usize][cost as usize]) % MOD;
                }
            }

            prevDp = dp.clone();
            prevPrefix = prefix.clone();
        }

        prefix[m as usize][k as usize]
    }
}