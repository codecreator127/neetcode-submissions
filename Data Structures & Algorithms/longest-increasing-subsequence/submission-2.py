class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        ## backtracking
        longest = 0

        def dfs(i, current):
            nonlocal longest

            longest = max(longest, len(current))

            if i >= len(nums):
                return

            if current and nums[i] > current[-1]:
                current.append(nums[i])
                longest = max(longest, len(current))

                dfs(i + 1, current)
                current.pop()
                dfs(i + 1, current)
            else:
                dfs(i + 1, current)


        for i in range(len(nums)):
            dfs(i, [nums[i]])

        return longest