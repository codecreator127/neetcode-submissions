class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## use complement approach

        seen = {}

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[curr] = i
        