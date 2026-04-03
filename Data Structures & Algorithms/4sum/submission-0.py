class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ## same as 3 sum, but set 2 nums, and reduce to 2 sum

        curr = set()
        out = []

        nums.sort()
        
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                l = b + 1
                r = len(nums) - 1

                while l < r:
                    foursum = nums[a] + nums[b] + nums[l] + nums[r]

                    if foursum == target:
                        curr = [nums[a], nums[b], nums[l], nums[r]]
                        if curr not in out:
                            out.append(curr)

                    if foursum > target:
                        r -= 1
                    else:
                        l += 1
        
        return out