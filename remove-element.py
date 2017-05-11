
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tail = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == val:
                nums[i], nums[tail] = nums[tail], nums[i]
                tail -= 1

        return tail + 1

if __name__ == '__main__':
    sol = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    print sol.removeElement(nums, val)
