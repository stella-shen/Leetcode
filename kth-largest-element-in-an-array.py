import random

class Solution(object):
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
