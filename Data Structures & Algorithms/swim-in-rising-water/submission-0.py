import heapq

class Solution:
    def swimInWater(self, grid):
        n = len(grid)

        visited = set()
        minHeap = [(grid[0][0], 0, 0)]  # (time, row, col)

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while minHeap:
            time, r, c = heapq.heappop(minHeap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # reached destination
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    newTime = max(time, grid[nr][nc])
                    heapq.heappush(minHeap, (newTime, nr, nc))