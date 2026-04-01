class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        out = nums[0]

        if len(nums) == 1:
            return nums[0]

        while left <= right:

            if nums[left] < nums[right]:
                out = min(out, nums[left])
                break

            middle = (right - left) // 2 + left
            print(middle)

            out = min(out, nums[middle])

            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1

        return out