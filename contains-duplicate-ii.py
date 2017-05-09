
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        index = dict()

        for i in range(len(nums)):
            if index.has_key(nums[i]):
                index[nums[i]].append(i)
                dif = index[nums[i]][-1] - index[nums[i]][-2]
                if dif <= k:
                    return True
            else:
                index[nums[i]] = [i]

        return False
        