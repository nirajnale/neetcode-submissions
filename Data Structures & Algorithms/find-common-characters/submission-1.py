from collections import Counter

class Solution:
    def commonChars(self, words):

        common = Counter(words[0])

        for word in words[1:]:
            common &= Counter(word)

        ans = []

        for ch, count in common.items():
            ans.extend([ch] * count)

        return ans