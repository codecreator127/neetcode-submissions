class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## use a complement approach
        ## one pass through, return if we see the complement
        ## use hashmap to store the seen nums and their index

        seen = {}

        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr

            if complement in seen:
                return [seen[complement], i]

            seen[curr] = i
        
            