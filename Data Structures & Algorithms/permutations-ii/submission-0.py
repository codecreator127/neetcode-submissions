class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        out = set()
        def backtrack(perm):
            if len(perm) == len(nums):
                out.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] != None:
                    perm.append(nums[i])
                    nums[i] = None
                    backtrack(perm)
                    nums[i] = perm[-1]
                    perm.pop()
        
        backtrack([])

        return list(out)
            