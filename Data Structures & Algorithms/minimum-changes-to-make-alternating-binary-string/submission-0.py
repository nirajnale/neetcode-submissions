class Solution:
    def minOperations(self, s: str) -> int:

        pattern0 = 0
        pattern1 = 0

        for i in range(len(s)):

            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if s[i] != expected0:
                pattern0 += 1

            if s[i] != expected1:
                pattern1 += 1

        return min(pattern0, pattern1)