
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s / 2
        if target in nums:
            return True
        
        dp = set([0])
        for num in nums:
            for i in dp.copy():
                dp.add(i + num)
    
        if target in dp:
            return True
        return False

if __name__ == '__main__':
    print Solution().canPartition([1, 2, 5])
