class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        l = 0

        while l < len(nums):
            for i in range(l, len(nums)):
                if nums[i] < nums[l]:
                    nums[l], nums[i] = nums[i], nums[l]
            
            l += 1
        
        return nums