use std::cmp::max;

impl Solution {
    pub fn max_dot_product(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut curr = vec![i32::min_value(); nums2.len() + 1];
        for i in 1..nums1.len() + 1 {
            let prev = curr.to_vec();
            for j in 1..nums2.len() + 1 {
                curr[j] = max(
                    max(max(max(curr[j], prev[j]), prev[j - 1]), curr[j - 1]),
                    max(prev[j - 1], 0) + nums1[i - 1] * nums2[j - 1],
                )
            }
        }
        curr[nums2.len()]
    }
}