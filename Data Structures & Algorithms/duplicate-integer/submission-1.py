class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # just convert to a set and then compare the size to original list

        return len(set(nums)) != len(nums)