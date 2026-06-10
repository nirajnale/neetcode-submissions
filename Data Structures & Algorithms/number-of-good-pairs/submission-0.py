from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums):

        freq = defaultdict(int)
        pairs = 0

        for num in nums:
            pairs += freq[num]
            freq[num] += 1

        return pairs