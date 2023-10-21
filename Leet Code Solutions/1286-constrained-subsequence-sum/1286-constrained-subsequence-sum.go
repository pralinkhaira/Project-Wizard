func constrainedSubsetSum(nums []int, k int) int {
    var dq []int
    for i := range nums {
        if len(dq) != 0 {
            nums[i] += nums[dq[0]]
        }
        
        for len(dq) != 0 && (i - dq[0] >= k || nums[i] >= nums[dq[len(dq) - 1]]) {
            if nums[i] >= nums[dq[len(dq) - 1]] {
                dq = dq[:len(dq)-1]
            } else {
                dq = dq[1:]
            }
        }

        if nums[i] > 0 {
            dq = append(dq, i)
        }
    }
    return max(nums)
}

func max(arr []int) int {
    maxVal := arr[0]
    for _, val := range arr {
        if val > maxVal {
            maxVal = val
        }
    }
    return maxVal
}