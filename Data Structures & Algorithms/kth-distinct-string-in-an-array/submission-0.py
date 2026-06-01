from collections import Counter

class Solution:
    def kthDistinct(self, arr, k):

        freq = Counter(arr)

        count = 0

        for word in arr:

            if freq[word] == 1:

                count += 1

                if count == k:
                    return word

        return ""
        