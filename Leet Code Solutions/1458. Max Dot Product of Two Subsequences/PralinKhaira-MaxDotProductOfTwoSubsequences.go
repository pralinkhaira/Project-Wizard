func maxDotProduct(nums1 []int, nums2 []int) int {
	dp := make([][]int, len(nums1))
	for i := range dp {
		dp[i] = make([]int, len(nums2))
	}
	dp[0][0] = nums1[0] * nums2[0]
	for i := 1; i < len(nums1); i++ {
		dp[i][0] = max(dp[i-1][0], nums1[i]*nums2[0])
	}
	for i := 1; i < len(nums2); i++ {
		dp[0][i] = max(dp[0][i-1], nums1[0]*nums2[i])
	}
	for i := 1; i < len(nums1); i++ {
		for j := 1; j < len(nums2); j++ {
			dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+nums1[i]*nums2[j], nums1[i]*nums2[j])
		}
	}
	return dp[len(nums1)-1][len(nums2)-1]
}

func max(first int, others ...int) int {
	maxValue := first
	for _, v := range others {
		if v > maxValue {
			maxValue = v
		}
	}
	return maxValue
}