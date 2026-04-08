class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ## simple method, use a hashmap and track nums
        ## if exceeds 1/3 then return that num

        seen = {}
        out = set()

        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1

            if seen[num] > (len(nums) // 3):
                out.add(num)
            
        return list(out)