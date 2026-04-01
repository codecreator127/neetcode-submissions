class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        buckets = [0] * k

        total = sum(nums)

        if total % k != 0:
            return False

        def backtrack(i):
            if i == len(nums):
                return True

            
            out = True

            for j in range(k):
                if buckets[j] + nums[i] <= total // k:
                    buckets[j] += nums[i]
                    if backtrack(i + 1):
                        return True

                    buckets[j] -= nums[i]

                if buckets[j] == 0:
                    break

            return False
            
        return backtrack(0)

