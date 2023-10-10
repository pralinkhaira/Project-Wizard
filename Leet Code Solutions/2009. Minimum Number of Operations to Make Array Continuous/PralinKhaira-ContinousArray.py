class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = sys.maxsize

        for i, s in enumerate(nums):
            e = s + n - 1
            idx = bisect_right(nums, e)

            ans = min(ans, n - (idx - i))
        return ans