class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        majority_count = 0

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            if count[num] > majority_count:
                majority_count = count[num]
                majority = num
        
        return majority