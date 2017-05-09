
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        ret = 0
        tail = len(nums) - 1
        while tail >= 0 and nums[tail] == val:
            tail -= 1
        if tail < 0:
            return 0

        for i in range(len(nums)):
            if i > tail:
                break
            if nums[i] != val:
                ret += 1
            else:
                temp = nums[i]
                nums[i] = nums[tail]
                nums[tail] = temp
                ret += 1
                while nums[tail] == val:
                    tail -= 1
                    if tail <= i:
                        break

        return ret

if __name__ == '__main__':
    sol = Solution()
    nums = [1]
    val = 1
    print sol.removeElement(nums, val)
