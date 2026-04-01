class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.out = []
        self.backtrack(nums, 0)
        return self.out


    def backtrack(self, nums, index):
        if index == len(nums):
            self.out.append(nums[:])
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.backtrack(nums, index + 1)
            nums[index], nums[i] = nums[i], nums[index]