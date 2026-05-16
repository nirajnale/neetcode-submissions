import heapq

class Solution:
    def minInterval(self, intervals, queries):

        intervals.sort()

        # (query value, original index)
        sortedQueries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        res = [-1] * len(queries)

        minHeap = []

        i = 0

        for q, idx in sortedQueries:

            # add all intervals starting before query
            while i < len(intervals) and intervals[i][0] <= q:

                left, right = intervals[i]

                length = right - left + 1

                heapq.heappush(minHeap, (length, right))

                i += 1

            # remove invalid intervals
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)

            # smallest valid interval
            if minHeap:
                res[idx] = minHeap[0][0]

        return res