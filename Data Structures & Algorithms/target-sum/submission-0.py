class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ### use dfs to find all possible paths

        def dfs(i, currSum):
            if currSum == target and i == len(nums):
                return 1

            if i >= len(nums):
                return 0
            
            return dfs(i + 1, currSum - nums[i]) + dfs(i + 1, currSum + nums[i])
        
        return dfs(0, 0)