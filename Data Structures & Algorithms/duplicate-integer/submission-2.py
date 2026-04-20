class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ## use a set, but not num comparison

        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            
            num_set.add(n)
        
        return False