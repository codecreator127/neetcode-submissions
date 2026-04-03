class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        ## same as 3 sum, but set 2 nums, and reduce to 2 sum

        out = []

        nums.sort()
        
        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums)):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                l = b + 1
                r = len(nums) - 1

                while l < r:
                    foursum = nums[a] + nums[b] + nums[l] + nums[r]

                    if foursum == target:
                        curr = [nums[a], nums[b], nums[l], nums[r]]
                        out.append(curr)

                        l += 1
                        r -= 1

                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    

                    elif foursum > target:
                        r -= 1
                    else:
                        l += 1
        
        return out