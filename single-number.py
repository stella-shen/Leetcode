
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for x in nums:
            ans = ans ^ x
        return ans

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 1, 2, 2, 3]
    print sol.singleNumber(nums)
