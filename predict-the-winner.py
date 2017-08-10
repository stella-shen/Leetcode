import numpy as np

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = np.zeros([len(nums)], dtype=int)
        for s in reversed(xrange(len(nums))):
            dp[s] = nums[s]
            for e in xrange(s + 1, len(nums)):
                a = nums[s] - dp[e]
                b = nums[e] - dp[e - 1]
                dp[e] = max(a, b)
        if dp[-1] >= 0:
            return True
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    print sol.PredictTheWinner([1, 5, 2])
