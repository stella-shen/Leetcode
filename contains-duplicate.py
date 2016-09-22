
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
        
if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 3, 4, 5]
    print sol.containsDuplicate(nums)
