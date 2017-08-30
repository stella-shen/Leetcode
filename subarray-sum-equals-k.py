import collections

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        cur_sum = 0
        lookup = collections.defaultdict(int)
        lookup[0] += 1
        for num in nums:
            cur_sum += num
            res += lookup[cur_sum - k]
            lookup[cur_sum] += 1
        return res
