from collections import Counter

class Solution:
    def makeEqual(self, words):

        freq = Counter()

        for word in words:
            freq.update(word)

        n = len(words)

        for count in freq.values():
            if count % n != 0:
                return False

        return True