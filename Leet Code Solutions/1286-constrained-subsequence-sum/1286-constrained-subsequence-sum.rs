impl Solution {
    pub fn constrained_subset_sum(mut nums: Vec<i32>, k: i32) -> i32 {
        let mut dq = std::collections::VecDeque::new();
        for i in 0..nums.len() {
            let val_to_add = if let Some(&front) = dq.front() {
                nums[front]
            } else {
                0
            };
            nums[i] += val_to_add;

            while let Some(&front) = dq.front() {
                if i as i32 - front as i32 >= k || nums[i] >= nums[*dq.back().unwrap()] {
                    if nums[i] >= nums[*dq.back().unwrap()] {
                        dq.pop_back();
                    } else {
                        dq.pop_front();
                    }
                } else {
                    break;
                }
            }

            if nums[i] > 0 {
                dq.push_back(i);
            }
        }
        *nums.iter().max().unwrap()
    }
}