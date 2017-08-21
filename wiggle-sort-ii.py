import random

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def idx(i, n):
            return (1 + 2 * i) % (n | 1)
        
        n = len(nums)
        if n < 2:
            return

        median = self.findKthLargest(nums, n / 2)
        i, j, k = 0, 0, n - 1
        while j <= k:
            if nums[idx(j, n)] > median:
                nums[idx(i, n)], nums[idx(j, n)] = nums[idx(j, n)], nums[idx(i, n)]
                i += 1
                j += 1
            elif nums[idx(j, n)] < median:
                nums[idx(j, n)], nums[idx(k, n)] = nums[idx(k, n)], nums[idx(j, n)]
                k -= 1
            else:
                j += 1

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        random.shuffle(nums)
        while left <= right:
            pivot = random.randint(left, right)
            new_pivot = self.partition(nums, left, right, pivot)
            if new_pivot == k - 1:
                return nums[new_pivot]
            elif new_pivot > k - 1:
                right = new_pivot - 1
            elif new_pivot < k - 1:
                left = new_pivot + 1
        
    def partition(self, nums, left, right, pivot):
        key = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        new_pivot = left
        for i in xrange(left, right):
            if nums[i] > key:
                nums[new_pivot], nums[i] = nums[i], nums[new_pivot]
                new_pivot += 1
        nums[right], nums[new_pivot] = nums[new_pivot], nums[right]
        return new_pivot

if __name__ == '__main__':
    Solution().wiggleSort([1, 3, 2, 2, 3, 1])
