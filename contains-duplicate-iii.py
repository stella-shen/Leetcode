import collections

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0: return False
        div = t + 1
        vis = {}
        for i, num in enumerate(nums):
            index = num / div
            if index in vis \
                    or index - 1 in vis and abs(vis[index - 1] - num) <= t \
                    or index + 1 in vis and abs(vis[index + 1] - num) <= t:
                return True
            vis[index] = num
            if i >= k: del vis[nums[i - k] / div]
        return False