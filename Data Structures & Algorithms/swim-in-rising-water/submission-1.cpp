class Solution {
public:
    int swimInWater(vector<vector<int>>& grid) {
        int n = grid.size();

        // minHeap: {time, row, col}
        priority_queue<
            vector<int>,
            vector<vector<int>>,
            greater<vector<int>>
        > minHeap;

        vector<vector<bool>> visited(n, vector<bool>(n, false));

        minHeap.push({grid[0][0], 0, 0});

        vector<pair<int,int>> directions = {
            {1,0}, {-1,0}, {0,1}, {0,-1}
        };

        while (!minHeap.empty()) {
            auto curr = minHeap.top();
            minHeap.pop();

            int time = curr[0];
            int r = curr[1];
            int c = curr[2];

            if (visited[r][c]) continue;

            visited[r][c] = true;

            // reached destination
            if (r == n - 1 && c == n - 1) {
                return time;
            }

            for (auto& dir : directions) {
                int nr = r + dir.first;
                int nc = c + dir.second;

                if (nr >= 0 && nr < n &&
                    nc >= 0 && nc < n &&
                    !visited[nr][nc]) {

                    int newTime = max(time, grid[nr][nc]);

                    minHeap.push({newTime, nr, nc});
                }
            }
        }

        return -1;
    }
};