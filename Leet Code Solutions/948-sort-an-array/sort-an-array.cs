public class Solution {
    private static Random rand = new Random();
    public int[] SortArray(int[] nums) {
        QuickSort(nums, 0, nums.Length - 1);
        return nums;
    }
    private void QuickSort(int[] nums, int low, int high) {
        if (low < high) {
            int pivotIndex = RandomizedPartition(nums, low, high);
            QuickSort(nums, low, pivotIndex);
            QuickSort(nums, pivotIndex + 1, high);
        }
    }

    private int RandomizedPartition(int[] nums, int low, int high) {
        int pivotIndex = rand.Next(low, high + 1);
        Swap(nums, pivotIndex, low);
        return Partition(nums, low, high);
    }

    private int Partition(int[] nums, int low, int high) {
        int pivot = nums[low];
        int i = low - 1;
        int j = high + 1;
        
        while (true) {
            do {
                i++;
            } while (nums[i] < pivot);
            
            do {
                j--;
            } while (nums[j] > pivot);
            
            if (i >= j) {
                return j;
            }
            
            Swap(nums, i, j);
        }
    }

    private void Swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}