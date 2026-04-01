class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        l, r = 0, 0
        if len(nums1) > len(nums2):
            r = len(nums2)
            A, B = nums2, nums1
        else:
            r = len(nums1)
            A, B = nums1, nums2

        while (l <= r):
            i = l + (r - l) // 2
            j = (total // 2) - i
            if i > 0 and j <= len(B) - 1 and A[i - 1] > B[j]:  # Case 1, arr A left partition is larger than arr B right partition
                r = i - 1
            elif j > 0 and i <= len(A) - 1 and A[i] < B[j - 1]:  # Case 2, flipped around
                l = i + 1
            else:
                a1 = A[i-1] if (0 < i <= len(A)) else -1
                a2 = A[i] if (0 <= i < len(A)) else 1001
                b1 = B[j-1] if (0 < j <= len(B)) else -1
                b2 = B[j] if (0 <= j < len(B)) else 1001
                if total % 2 == 0:
                    return float(max(a1, b1) + min(a2, b2)) / 2
                else:
                    return float(min(a2, b2))

            