class Solution:
    def countConsistentStrings(self, allowed, words):

        allowedSet = set(allowed)
        ans = 0

        for word in words:

            consistent = True

            for ch in word:
                if ch not in allowedSet:
                    consistent = False
                    break

            if consistent:
                ans += 1

        return ans