class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(x, y):
            if x + y > y + x:
                return 1
            else:
                return -1
        nums = [str(x) for x in nums]
        nums.sort(cmp=lambda x, y: cmp=compare(x, y))
        largest = ''.join(nums)
        return largest.lstrip('0') or '0'