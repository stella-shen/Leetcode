
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = None
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            elif count == 0:
                count = 1
                candidate = num
            else:
                count -= 1
        return candidate

if __name__ == '__main__':
    sol = Solution()
    nums = [1, 2, 2, 3]
    print sol.majorityElement(nums)
