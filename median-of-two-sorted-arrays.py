import math

class Solution(object):

    def findKthElement(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        len1 = len(nums1)
        len2 = len(nums2)
        if nums1[len1/2] >= nums2[len2/2]:
            if k > len1/2 + len2/2:
                return self.findKthElement(nums1, nums2[len2/2 + 1: ], k - len2/2 - 1)
            else:
                return self.findKthElement(nums1[:len1/2], nums2, k)
        else:
            return self.findKthElement(nums2, nums1, k)


    def findMedianSortedArrays(self, nums1, nums2):
        """

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        median = (len1 + len2) / 2
        median_l = math.ceil(median)
        median_s = int(median)
        if (len1 + len2) % 2 == 1:
            return self.findKthElement(nums1, nums2, median)
        else:
            s = self.findKthElement(nums1, nums2, median)
            l = self.findKthElement(nums1, nums2, median - 1)
            return (s + l) / 2.0

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print sol.findMedianSortedArrays(nums1, nums2)
