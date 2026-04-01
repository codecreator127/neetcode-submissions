class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # out = []
        # subset = []

        # nums.sort()

        # def dfs(i):
            
        #     if i >= len(nums):
        #         if subset not in out:
        #             out.append(subset.copy())
        #         return

        #     subset.append(nums[i])
        #     dfs(i + 1)

        #     subset.pop()

        #     dfs(i + 1)

        # dfs(0)

        # return out

        nums.sort()
        out = []

        def backtrack(i, subset):
            out.append(subset[::])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                
                subset.append(nums[j])
                backtrack(j + 1, subset)
                subset.pop()

        backtrack(0, [])

        return out


