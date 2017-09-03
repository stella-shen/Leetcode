import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        k, n, cnts = 3, len(nums), collections.defaultdict(int)

        for num in nums:
            cnts[num] += 1
            if len(cnts) == k:
                for j in cnts.keys():
                    cnts[j] -= 1
                    if cnts[j] == 0:
                        del cnts[j]
        for i in cnts.keys():
            cnts[i] = 0
        
        res = []
        for num in nums:
            if num in cnts:
                cnts[num] += 1
                if cnts[num] > n / k and num not in res:
                    res.append(num)

        return res
