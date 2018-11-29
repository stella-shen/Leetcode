class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        
        diff = 0
        ind = 0
        for ind in range(1, len(A)):
            diff = A[ind] - A[ind - 1]
            if diff == 0:
                continue
            if diff > 0 or diff < 0:
                break
            return True
        
        for i in range(ind, len(A)):
            cur_diff = A[i] - A[i - 1]
            if cur_diff * diff >= 0:
                continue
            else:
                return False
            return True
        return True

if __name__ == "__main__":
    A = [1, 3, 2]
    sol = Solution()
    print(sol.isMonotonic(A))