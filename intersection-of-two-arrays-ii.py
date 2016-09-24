import collections

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        #Solution 1
        """
        nums1.sort()
        nums2.sort()
        ret = list()
        i1 = 0
        i2 = 0
        while i1 != len(nums1) and i2 != len(nums2):
            if nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                ret.append(nums1[i1])
                i1 += 1
                i2 += 1
        return ret
        """
        #Solution 2
        count = collections.Counter(nums1)
        ret = []
        for num in nums2:
            if count[num] > 0:
                ret.append(num)
                count[num] -= 1
        return ret


if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print sol.intersect(nums1, nums2)
