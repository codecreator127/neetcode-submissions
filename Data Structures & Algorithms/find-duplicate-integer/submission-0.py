class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ## basic use hashset to find duplicate

        seen = {}

        for num in nums:
            if num in seen:
                return num
            else:
                seen[num] = 1
        

