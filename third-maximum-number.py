
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cp = set(nums)
        if len(cp) < 3:
            return max(cp)

        cp.remove(max(cp))
        cp.remove(max(cp))
        return max(cp)
