public class Solution {
    public int ConstrainedSubsetSum(int[] nums, int k) {
        var dq = new LinkedList<int>();
        for (int i = 0; i < nums.Length; i++) {
            nums[i] += dq.Count > 0 ? nums[dq.First.Value] : 0;

            while (dq.Count > 0 && (i - dq.First.Value >= k || nums[i] >= nums[dq.Last.Value])) {
                if (nums[i] >= nums[dq.Last.Value]) dq.RemoveLast();
                else dq.RemoveFirst();
            }

            if (nums[i] > 0) {
                dq.AddLast(i);
            }
        }
        return nums.Max();
    }
}