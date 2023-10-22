func maximumScore(nums []int, k int) int {
    left, right := k, k
    min_val := nums[k]
    max_score := min_val

    for left > 0 || right < len(nums) - 1 {
        if left == 0 || (right < len(nums) - 1 && nums[right+1] > nums[left-1]) {
            right++
        } else {
            left--
        }
        min_val = min(min_val, min(nums[left], nums[right]))
        max_score = max(max_score, min_val * (right - left + 1))
    }
    
    return max_score
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}