
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [
            #state 0's legal transfer
            {'digit': 1, 'sign': 2, '.': 3},
            #state 1
            {'digit': 1, 'e': 4, '.': 5},
            #state 2
            {'digit': 1, '.': 3},
            #state 3
            {'digit': 5},
            #state 4
            {'sign': 6, 'digit': 7},
            #state 5
            {'digit': 5, 'e': 4},
            #state 6
            {'digit': 7},
            #state 7
            {'digit': 7}
        ]
        s = s.strip()
        current_state = 0
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            elif c == '+' or c == '-':
                c = 'sign'
            if c not in state[current_state].keys():
                return False
            current_state = state[current_state][c]
        if current_state not in [1, 5, 7]:
            return False
        return True

if __name__ == '__main__':
    sol = Solution()
    print sol.isNumber('.e1')
