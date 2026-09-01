class Solution {
public:
    int ans = 0;

    void solve(vector<int>& nums, int i, int currXor) {

        // Reached the end
        if (i == nums.size()) {
            ans += currXor;
            return;
        }

        // Don't take nums[i]
        solve(nums, i + 1, currXor);

        // Take nums[i]
        solve(nums, i + 1, currXor ^ nums[i]);
    }

    int subsetXORSum(vector<int>& nums) {

        solve(nums, 0, 0);

        return ans;
    }
};