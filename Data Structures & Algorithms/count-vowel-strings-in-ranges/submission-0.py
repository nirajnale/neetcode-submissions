class Solution:
    def vowelStrings(self, words, queries):

        vowels = {'a', 'e', 'i', 'o', 'u'}

        prefix = [0]

        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])

        ans = []

        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans