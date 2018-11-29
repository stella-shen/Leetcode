class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_ind = 1
        for even_ind in range(0, len(A), 2):
            if A[even_ind] % 2:
                while A[odd_ind] % 2:
                    odd_ind += 2
                A[even_ind], A[odd_ind] = A[odd_ind], A[even_ind]
        return A