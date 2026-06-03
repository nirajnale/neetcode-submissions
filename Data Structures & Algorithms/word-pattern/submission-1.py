class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for ch, word in zip(pattern, words):

            if ch in charToWord:
                if charToWord[ch] != word:
                    return False

            else:
                charToWord[ch] = word

            if word in wordToChar:
                if wordToChar[word] != ch:
                    return False

            else:
                wordToChar[word] = ch

        return True