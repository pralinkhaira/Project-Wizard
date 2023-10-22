impl Solution {
    pub fn maximum_score(nums: Vec<i32>, k: i32) -> i32 {
        let mut left = k as usize;
        let mut right = k as usize;
        let mut min_val = nums[k as usize];
        let mut max_score = min_val;

        while left > 0 || right < nums.len() - 1 {
            if left == 0 || (right < nums.len() - 1 && nums[right + 1] > nums[left - 1]) {
                right += 1;
            } else {
                left -= 1;
            }
            min_val = min_val.min(nums[left].min(nums[right]));
            max_score = max_score.max(min_val * (right as i32 - left as i32 + 1));
        }
        
        max_score
    }
}