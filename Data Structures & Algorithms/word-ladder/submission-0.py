from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        # Build intermediate patterns
        patternMap = defaultdict(list)
        L = len(beginWord)
        for word in wordSet:
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                patternMap[pattern].append(word)

        # BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            word, level = queue.popleft()
            for i in range(L):
                pattern = word[:i] + '*' + word[i+1:]
                for nextWord in patternMap[pattern]:
                    if nextWord == endWord:
                        return level + 1
                    if nextWord not in visited:
                        visited.add(nextWord)
                        queue.append((nextWord, level + 1))
                # Optional: clear to prevent reprocessing
                patternMap[pattern] = []
        return 0