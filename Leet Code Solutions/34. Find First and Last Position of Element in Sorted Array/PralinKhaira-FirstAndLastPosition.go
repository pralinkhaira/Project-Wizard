func searchRange(nums []int, target int) []int {
    left := findLeft(nums, target)
    right := findRight(nums, target)

    if left <= right {
        return []int{left, right}
    } else {
        return []int{-1, -1}
    }
}

func findLeft(nums []int, target int) int {
    left, right := 0, len(nums)-1
    index := -1

    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] == target {
            index = mid
            right = mid - 1
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return index
}

func findRight(nums []int, target int) int {
    left, right := 0, len(nums)-1
    index := -1

    for left <= right {
        mid := left + (right-left)/2
        if nums[mid] == target {
            index = mid
            left = mid + 1
        } else if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }

    return index
}