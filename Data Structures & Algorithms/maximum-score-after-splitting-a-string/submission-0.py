class Solution:
    def maxScore(self, s: str) -> int:

        leftZeros = 0
        rightOnes = s.count('1')

        ans = 0

        for i in range(len(s) - 1):

            if s[i] == '0':
                leftZeros += 1
            else:
                rightOnes -= 1

            ans = max(ans, leftZeros + rightOnes)

        return ans