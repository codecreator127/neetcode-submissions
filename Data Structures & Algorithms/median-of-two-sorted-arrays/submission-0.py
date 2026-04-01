class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # brute force method:

        sorted_list = sorted(nums1 + nums2)

        print(sorted_list)

        if len(sorted_list) % 2 == 0:
            median = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
            return median
        else:
            return sorted_list[len(sorted_list) // 2]

