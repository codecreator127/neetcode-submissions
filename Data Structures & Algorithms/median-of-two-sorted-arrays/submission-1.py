class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # brute force method:

        # sorted_list = sorted(nums1 + nums2)

        # print(sorted_list)

        # if len(sorted_list) % 2 == 0:
        #     median = (sorted_list[len(sorted_list) // 2] + sorted_list[len(sorted_list) // 2 - 1]) / 2
        #     return median
        # else:
        #     return sorted_list[len(sorted_list) // 2]

        
        total = len(nums1) + len(nums2)

        smaller = nums1
        larger = nums2
        if len(nums1) > len(nums2):
            smaller = nums2
            larger = nums1
        
        # do binary search on smaller

        half = total // 2

        left = 0
        right = len(smaller) - 1

        while True:
            middle = (left + right) // 2
            j = half - middle - 2

            smallerLeft = smaller[middle] if middle >= 0 else float("-infinity")
            smallerRight = smaller[middle + 1] if (middle + 1) < len(smaller) else float("infinity")
            largerLeft = larger[j] if j >= 0 else float("-infinity")
            largerRight = larger[j + 1] if (j + 1) < len(larger) else float("infinity") 

            if smallerLeft <= largerRight and largerLeft <= smallerRight:
                
                if total % 2:
                    return min(smallerRight, largerRight)
                return (max(smallerLeft, largerLeft) + min(smallerRight, largerRight)) / 2
                
            elif smallerLeft > largerRight:
                right = middle - 1
            else:
                left = middle + 1







