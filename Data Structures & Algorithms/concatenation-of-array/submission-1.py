class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        out = [0] * (2*n)

        for i, num in enumerate(nums):
            out[i] = out[i + n] = nums[i]

        
        return out