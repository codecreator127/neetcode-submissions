class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ### use dfs to find all possible paths

        ## now optimize using a memo to avoid recalculations

        memo = {}

        def dfs(i, currSum):
            if currSum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0

            if (i, currSum) in memo:
                return memo[(i, currSum)]
            
            memo[(i, currSum)] = dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])

            return memo[(i, currSum)]
        
        return dfs(0, 0)