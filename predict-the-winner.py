
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memo = list()
        for i in xrange(len(nums)):
            cur_list = list()
            for j in xrange(len(nums)):
                cur_list.append('False')
            memo.append(cur_list)
        if self.winner(nums, 0, len(nums) - 1, memo) >= 0:
            return True
        else:
            return False
        
    def winner(self, nums, s, e, memo):
        if s == e:
            memo[s][e] = nums[s]
            return memo[s][e]
        if memo[s][e] != 'False':
            return memo[s][e]
        a = nums[s] - self.winner(nums, s + 1, e, memo)
        b = nums[e] - self.winner(nums, s, e - 1, memo)
        memo[s][e] = max(a, b)
        return memo[s][e]

if __name__ == '__main__':
    sol = Solution()
    print sol.PredictTheWinner([1, 5, 2])
