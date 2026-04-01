class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and j != i and abs(i - j) <= k:
                    return True
        
        return False