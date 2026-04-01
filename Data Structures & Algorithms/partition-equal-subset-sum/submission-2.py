class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        n = len(nums)
        total = sum(nums)

        if total % 2 != 0:
            return False
        half = total // 2
        
        memo = [[None] * (half + 1) for _ in range(n)]

        ## backtracking, try to find half sum
        def dfs(i, current):

            if current == half:
                return True
                

            if i >= len(nums) or current > half:
                return False

            if memo[i][current] is not None:
                return memo[i][current]


            memo[i][current] = dfs(i + 1, current + nums[i]) or dfs(i + 1, current)

            return memo[i][current]
    
        return dfs(0, 0)