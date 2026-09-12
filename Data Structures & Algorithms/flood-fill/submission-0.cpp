class Solution {
public:
    int rows, cols;
    int original, newColor;

    void dfs(vector<vector<int>>& image, int r, int c) {
        // Out of bounds
        if (r < 0 || r >= rows || c < 0 || c >= cols) {
            return;
        }

        // Only fill cells with the original color
        if (image[r][c] != original) {
            return;
        }

        // Change the color
        image[r][c] = newColor;

        // Visit 4 directions
        dfs(image, r - 1, c); // Up
        dfs(image, r + 1, c); // Down
        dfs(image, r, c - 1); // Left
        dfs(image, r, c + 1); // Right
    }

    vector<vector<int>> floodFill(
        vector<vector<int>>& image,
        int sr,
        int sc,
        int color
    ) {
        rows = image.size();
        cols = image[0].size();

        original = image[sr][sc];
        newColor = color;

        if (original == newColor) {
            return image;
        }

        dfs(image, sr, sc);

        return image;
    }
};