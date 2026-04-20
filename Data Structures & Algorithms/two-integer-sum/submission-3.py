class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## use a complement approach
        ## one pass through, return if we see the complement
        ## use hashmap to store the seen nums and their index

        ## complement lookup + hashamp

        seen = {}

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target - nums[i]], i]

            seen[nums[i]] = i