public class Solution {
    public int MinOperations(int[] nums) {
        Array.Sort(nums);
        List<int> list = new List<int>();
        
        for (int i = 0; i < nums.Length; i++)
        {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            list.Add(nums[i]);
        }

        int max = 0;
        
        for (int i = 0; i < list.Count; i++)
        {
            int target = list[i] + nums.Length - 1;
            int index = list.BinarySearch(target);
            
            if (index < 0)
                index = (~index) - 1;
            
            max = Math.Max(max, index - i + 1);
        }
        
        return nums.Length - max;
    }
}