from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        # build graph with reverse sorted destinations
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        
        path = []

        def dfs(airport):
            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            path.append(airport)  # post-order

        dfs("JFK")
        return path[::-1]