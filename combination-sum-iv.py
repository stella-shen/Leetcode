
class Solution(object):
    count = 0
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0] * (target + 1)
        nums.sort()
        res[0] = 1
        for cur_sum in xrange(1, target + 1):
            for n in nums:
                if n <= cur_sum:
                    res[cur_sum] += res[cur_sum - n]
                else:
                    break
        return res[target]

if __name__ == '__main__':
    sol = Solution()
    print sol.combinationSum4([1, 2, 3], 4)
