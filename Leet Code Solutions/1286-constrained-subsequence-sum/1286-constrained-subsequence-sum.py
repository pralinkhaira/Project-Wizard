class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dq = deque()
        for i in range(len(nums)):
            nums[i] += nums[dq[0]] if dq else 0
            
            while dq and (i - dq[0] >= k or nums[i] >= nums[dq[-1]]):
                dq.pop() if nums[i] >= nums[dq[-1]] else dq.popleft()
                
            if nums[i] > 0:
                dq.append(i)
                
        return max(nums)