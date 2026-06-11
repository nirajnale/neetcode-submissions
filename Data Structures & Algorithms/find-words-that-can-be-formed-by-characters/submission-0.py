from collections import Counter

class Solution:
    def countCharacters(self, words, chars):

        charsFreq = Counter(chars)
        ans = 0

        for word in words:

            wordFreq = Counter(word)

            good = True

            for ch in wordFreq:
                if wordFreq[ch] > charsFreq[ch]:
                    good = False
                    break

            if good:
                ans += len(word)

        return ans