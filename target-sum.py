
class Solution(object):
    count = 0
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.calculate(nums, 0, 0, S)
        return self.count

    def calculate(self, nums, i, s, S):
        if i == len(nums):
            if s == S:
                self.count += 1
                return
        else:
            self.calculate(nums, i + 1, s + nums[i], S)
            self.calculate(nums, i + 1, s - nums[i], S)

if __name__ == '__main__':
    sol = Solution()
    print sol.findTargetSumWays([1, 1, 1, 1, 1], 3)
