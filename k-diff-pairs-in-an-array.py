
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        cnt = dict()
        ret = 0

        for n in nums:
            if cnt.has_key(n):
                cnt[n] += 1
            else:
                cnt[n] = 1

        for key in cnt.iterkeys():
            if k == 0:
                if cnt[key] > 1:
                    ret += 1
            elif cnt.has_key(key + k):
                ret += 1

        return ret

if __name__ == '__main__':
    sol = Solution()
    nums = [1,3,1,5,4]
    k = 0
    print sol.findPairs(nums, k)
