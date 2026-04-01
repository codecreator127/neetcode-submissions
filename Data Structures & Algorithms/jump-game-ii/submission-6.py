class Solution:
    def jump(self, nums: List[int]) -> int:
        out = 0

        l = 0
        r = 0

        while r < len(nums) - 1:
            fartherest = 0
            for i in range(l, r + 1):
                fartherest = max(fartherest, i + nums[i])
            
            l = r + 1
            r = fartherest
            out += 1
        
        return out