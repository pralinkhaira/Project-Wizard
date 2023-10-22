public class Solution {
    public int MaximumScore(int[] nums, int k) {
        int left = k, right = k;
        int min_val = nums[k];
        int max_score = min_val;

        while (left > 0 || right < nums.Length - 1) {
            if (left == 0 || (right < nums.Length - 1 && nums[right + 1] > nums[left - 1])) {
                right++;
            } else {
                left--;
            }
            min_val = Math.Min(min_val, Math.Min(nums[left], nums[right]));
            max_score = Math.Max(max_score, min_val * (right - left + 1));
        }
        
        return max_score;
    }
}