class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ## use a prefix sum
        ## create a prefix sum hashmap (key=prefix sum, value=freq)
        ## current_prefix - k in set()
        ## then += 1 since we have a valid subarray
        
        ## [0, 2, 1, 2, 4]

        ## create prefix sum hashmap to track freq
        prefix = defaultdict(int)
        prefix[0] = 1

        rolling_sum = 0
        ans = 0

        for num in nums:
            rolling_sum += num
            complement = rolling_sum - k
            if complement in prefix:
                ans += prefix[complement]
            
            prefix[rolling_sum] += 1



        return ans


        