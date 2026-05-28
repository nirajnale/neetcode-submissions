from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:

        freq = Counter(s)

        maxOdd = 0
        minEven = float('inf')

        for count in freq.values():

            if count % 2 == 1:
                maxOdd = max(maxOdd, count)

            else:
                minEven = min(minEven, count)

        return maxOdd - minEven
        