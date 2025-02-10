from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        # nums1 must be smaller or equal
        left, right = 0, len(nums1) - 1
        total = len(nums1) + len(nums2)
        half = total // 2
        while True:
            mid1 = (left + right) // 2 
            mid2 = half - mid1 - 2
            leftOfMid1 = nums1[mid1] if mid1 >= 0 else -1_000_000
            rightOfMid1 = nums1[mid1+1] if (mid1+1) < len(nums1) else 1_000_000
            leftOfMid2 = nums2[mid2] if mid2 >= 0 else -1_000_000
            rightOfMid2 = nums2[mid2+1] if (mid2+1) < len(nums2) else 1_000_000            
            if leftOfMid1 <= rightOfMid2 and leftOfMid2 <= rightOfMid1:
                if total % 2:
                    return min(rightOfMid1, rightOfMid2)
                else:
                    return (min(rightOfMid2, rightOfMid1) + max(leftOfMid1, leftOfMid2)) / 2
            elif leftOfMid2 > rightOfMid1:
                left = mid1 + 1
            else:
                right = mid1 - 1

input1 = \
[2]

input2 = \
[]
result = Solution().findMedianSortedArrays(input1, input2)
print(result)