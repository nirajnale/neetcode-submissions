from collections import Counter

class Solution:
    def findLucky(self, arr):
        freq = Counter(arr)

        ans = -1

        for num, count in freq.items():
            if num == count:
                ans = max(ans, num)

        return ans