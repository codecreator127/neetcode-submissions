class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        out = []
        curr = []

        def backtrack(i):
            if i == len(nums):
                out.append(curr.copy())
                return
            
            curr.append(nums[i])
            backtrack(i + 1)

            curr.pop()
            backtrack(i + 1)
        
        backtrack(0)

        return out

            