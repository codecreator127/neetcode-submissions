class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ## binary search

        l = 0
        r = len(nums) - 1

        while l <= r:
            half = (l + r) // 2

            print(half)

            if nums[half] == target:
                return half
            
            if nums[half] > target:
                r = half - 1
            elif nums[half] < target:
                l = half + 1

        return l