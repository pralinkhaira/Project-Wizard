public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        int leftIndex = BinarySearch(nums, target, true);
        int rightIndex = BinarySearch(nums, target, false);

        if (leftIndex <= rightIndex) {
            return new int[] { leftIndex, rightIndex };
        } else {
            return new int[] { -1, -1 };
        }
    }

    private int BinarySearch(int[] nums, int target, bool findLeft) {
        int low = 0;
        int high = nums.Length - 1;
        int index = -1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (nums[mid] == target) {
                index = mid;
                if (findLeft) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return index;
    }
}