
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_ind = 0
        for even_ind in range(len(A)):
            if A[even_ind] % 2 == 0:
                A[even_ind], A[odd_ind] = A[odd_ind], A[even_ind]
                odd_ind += 1
        return A

if __name__ == "__main__":
    sol = Solution()
    A = [3, 1, 2, 4]
    print(sol.sortArrayByParity(A))