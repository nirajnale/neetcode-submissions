class Solution:
    def findMissingAndRepeatedValues(self, grid):

        n = len(grid)
        N = n * n

        freq = [0] * (N + 1)

        for row in grid:
            for num in row:
                freq[num] += 1

        repeated = missing = -1

        for i in range(1, N + 1):

            if freq[i] == 2:
                repeated = i

            elif freq[i] == 0:
                missing = i

        return [repeated, missing]