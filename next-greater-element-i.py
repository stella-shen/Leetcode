
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = list()
        for num in findNums:
            index = nums.index(num)
            flag = True
            for i in range(index + 1, len(nums)):
                if nums[i] > num:
                    ret.append(nums[i])
                    flag = False
                    break
            if flag:
                ret.append(-1)
        return ret

if __name__ == '__main__':
    sol = Solution()
    print sol.nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
