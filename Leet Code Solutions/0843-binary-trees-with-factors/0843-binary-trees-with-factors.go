package main

import (
	"math"
	"sort"
)

const MOD int64 = 1e9 + 7

func numFactoredBinaryTrees(arr []int) int {
	sort.Ints(arr)
	s := make(map[int]bool)
	for _, x := range arr {
		s[x] = true
	}

	dp := make(map[int]int64)
	for _, x := range arr {
		dp[x] = 1
	}

	for _, i := range arr {
		for _, j := range arr {
			if j > int(math.Sqrt(float64(i))) {
				break
			}
			if i%j == 0 && s[i/j] {
				temp := (dp[j] * dp[i/j]) % MOD
				if i/j == j {
					dp[i] = (dp[i] + temp) % MOD
				} else {
					dp[i] = (dp[i] + temp*2) % MOD
				}
			}
		}
	}

	res := int64(0)
	for _, v := range dp {
		res = (res + v) % MOD
	}
	return int(res)
}